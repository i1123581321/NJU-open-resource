# Automatic Reference Counting

swift 使用 ARC (Auto Reference Counting) 来管理内存，大部分情况下不需要关心 ARC 是怎么运作的，只有少部分的情况下 ARC 需要更多的信息来进行管理。ARC 只用于管理类的实例，structure 和 enumeration 是 value type，不通过引用来访问

## How ARC Works

每次创建一个类实例，ARC 会为其分配一块内存，而在实例消亡时 ARC 负责回收内存。为了避免在实例仍被使用时回收，只要还有一个活跃引用指向该实例，ARC 就不会回收这个实例。为了实现这一点，每当将一个类实例分配给一个属性，常量，变量，都会产生一个 strong reference，只要有强引用就不能回收实例

## Strong Reference Cycles

如果两个类实例彼此持有对方的引用，就会产生一个强引用的环，这样这两个实例的引用数永远不会等于 0

swift 提供了两种方式解决强引用环：弱引用（weak reference）和不拥有引用（unowned reference），弱引用用在被引用实例生命周期较短的情况，而不拥有引用用在被引用实例生命周期一样长或更长的情况

### Weak Reference

弱引用可以避免出现循环引用，只需要在声明属性或变量前加上 `weak` 关键字

由于弱引用指向的对象一般生命周期更短，且可能在运行时就被回收，故一般将其声明为 optional 的变量，在回收时其值自动设为 `nil`（此时不会触发 property observer）

### Unowned Reference

不拥有引用在声明前加上 `unowned` 关键字，与弱引用的区别在于，不拥有引用在持有期间不会被设为 `nil`

只有在确保被引用对象生命周期更长的情况下才使用 unowned reference，否则引用一个被回收的实例会产生一个运行时错误

如果执意要访问被回收后的位置，使用 `unowned(unsafe)` 关键字

也可以将一个不拥有引用设为 optional，此时其使用背景和弱引用一样，只是用户要自己确保其始终指向一个有效引用或手动被设为 `nil`

### Unowned References and Implicitly Unwrapped Optional Properties

在两个互相被引用的对象间可以存在三种关系

* 两个引用都可能为 `nil`
* 其中一个引用可以为 `nil` 而另一个必须有值
* 两个都必须有值

第一种情况可以使用弱引用，第二种情况可以使用不拥有引用，而第三种情况，为了避免循环引用，可以在一方使用不拥有引用，另一方使用隐式展开的 optional，这样双方都可以直接访问对方，同时避免循环引用

```swift
class Country {
    let name: String
    var capitalCity: City!
    init(name: String, capitalName: String) {
        self.name = name
        self.capitalCity = City(name: capitalName, country: self)
    }
}

class City {
    let name: String
    unowned let country: Country
    init(name: String, country: Country) {
        self.name = name
        self.country = country
    }
}
```

## Strong Reference Cycles for Closure

使用闭包也会导致循环引用，如将一个闭包分配给实例的一个属性，而闭包捕获了该实例本身。发生这种情况是因为闭包也是 reference type

想要解决这种情况的循环引用，只需要定义一个 capture list，用来指定捕获的引用为弱引用或不拥有引用。capture list 位于参数列表前

```swift
lazy var someClosure = {
    [unowned self, weak delegate = self.delegate]
    (index: Int, stringToProcess: String) -> String in
    // closure body goes here
}
```

如果闭包和其捕获的对象总是引用对方且同时被回收，则使用不拥有引用，而如果被捕获的实例可能为空，则使用弱引用