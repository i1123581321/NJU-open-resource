# Memory Safety

swift 提供了很多保证内存被正确访问的机制，如变量访问前必须初始化，内存在回收后不能访问，数组访问前检查下标

swift 同样提供了用于互斥访问的机制

## Conflicting Access to Memory

对内存的访问发生在赋值或传参等场合，如果代码的不同部分试图访问内存的同一个位置就会发生冲突

单线程的代码中仍有可能发生冲突，swift 保证能显示编译器错误或是运行时错误

在考虑访问冲突时，有三个要考虑的变量：访问是读还是写；访问的时间长短；访问的位置

如果两个不同的内存访问满足以下条件，就会发生冲突

* 至少有一个是写访问或是非原子的访问
* 访问内存的同一位置
* 访问时间重叠

对于 swift 来说，只有使用了 C 原子操作的才是原子的，否则都是非原子的访问。对于一个瞬时的访存，没有代码能在其结束之前开始运行，大部分读写操作都是瞬时的，但也有长时间的访存操作

访存相互重叠的情况一般发生在使用 in-out 参数的函数或是 mutating 的方法

## Conflicting Access to In-Out Parameters

函数对所有 in-out 参数的写访问都是长期的，写访问从所有非 in-out 的参数计算完成开始，直到函数调用完成结束，如果有多个 in-out 参数，写访问的开始顺序和参数顺序相同

此时不能访问被作为参数传入的原变量

```swift
var stepSize = 1

func increment(_ number: inout Int) {
    number += stepSize
}

increment(&stepSize)
// Error: conflicting accesses to stepSize
```

解决方法是使用显式的副本

```swift
// Make an explicit copy.
var copyOfStepSize = stepSize
increment(&copyOfStepSize)

// Update the original.
stepSize = copyOfStepSize
// stepSize is now 2
```

如果用一个变量作为多个 in-out 参数，同样会产生冲突

```swift
func balance(_ x: inout Int, _ y: inout Int) {
    let sum = x + y
    x = sum / 2
    y = sum - x
}
var playerOneScore = 42
var playerTwoScore = 30
balance(&playerOneScore, &playerTwoScore)  // OK
balance(&playerOneScore, &playerOneScore)
// Error: conflicting accesses to playerOneScore
```

## Conflicting Access to self in Methods

一个 mutating 方法在其函数调用期间对 `self` 有写访问，此时如果有另一个对实例的访问则会产生冲突，如将这个实例作为 in-out 参数传入函数

```swift
extension Player {
    mutating func shareHealth(with teammate: inout Player) {
        balance(&teammate.health, &health)
    }
}

var oscar = Player(name: "Oscar", health: 10, energy: 10)
var maria = Player(name: "Maria", health: 5, energy: 10)
oscar.shareHealth(with: &maria)  // OK
oscar.shareHealth(with: &oscar)
// Error: conflicting accesses to oscar
```

## Conflicting Access to Properties

structure 的属性和 tuple 的分量都是 value，对其一个分量的访问需要对整体的写访问，这同样会导致访问冲突

```swift
var playerInformation = (health: 10, energy: 20)
balance(&playerInformation.health, &playerInformation.energy)
// Error: conflicting access to properties of playerInformation

var holly = Player(name: "Holly", health: 10, energy: 10)
balance(&holly.health, &holly.energy)  // Error
```

互斥访问和比内存安全更严格，一段代码可能违反了互斥访问但仍能保证内存安全，如果编译器能确保内存安全就会允许代码运行，比如对 structure 的属性的重叠访问如果能保证如下条件则能安全运行

* 只访问存储属性而不是计算属性或类属性
* structure 是局部变量而非全局变量
* structure 没有被任何闭包捕获，或是只被 non-escaping 闭包捕获