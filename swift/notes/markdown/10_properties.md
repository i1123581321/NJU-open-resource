# Properties

属性是将类和值关联起来的部分，存储属性将常量或变量的值存储作为类的一部分，而计算属性只是计算值不存储。class，structure，enumeration 都有计算属性，但 enumeration 没有存储属性

还有类属性，和类型而非类型的实例相关联

除此之外还可以添加 properties observer 以在属性的值变化时做出行动

可以用 properties wrapper 来复用代码

## Store Properties

可以是变量或常量，直接在类定义中使用 `var` 或 `let` 定义，在定义时可以为其提供默认值，也可以在构造器中再次修改（即使是常量）

如果创建了一个 structure 的实例并将其赋给一个常量，则不能修改其中的属性，即使属性被定义为变量，这种行为不适用于 class，因为是 reference type

在定义前加上 `lazy` 关键字可以使属性的初始化被推迟到第一次使用的时候（必须是 `var`，因为对属性的访问都在初始化后，而常量必须在实例初始化前就初始化），如果属性的值依赖于初始化时还不能决定的值，或是属性的初始化需要相当的计算代价，就要使用 lazy

> 多线程环境下，lazy 的属性不能保证只被初始化一次

## Computed Properties

比起直接存储值，计算属性提供一个 getter 和一个可选的 setter（用于修改其他值），计算属性只能定义为变量

```swift
struct Rect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) {
            origin.x = newCenter.x - (size.width / 2)
            origin.y = newCenter.y - (size.height / 2)
        }
    }
}
```

如果 setter 定义时不提供参数名，则使用默认值 `newValue`，而如果 getter 只有一行表达式，则默认返回该表达式的结果

如果没有给一个计算属性定义 setter，那么这个属性就是只读的，在这种情况下可以直接省去 getter

```swift
struct Cuboid {
    var width = 0.0, height = 0.0, depth = 0.0
    var volume: Double {
        return width * height * depth
    }
}
```

## Properties Observers

properties observer 观察属性的改变，每当属性被 set 时就被调用，可以为定义或继承的存储属性，或是继承的计算属性定义 properties observer（对于定义的计算属性，直接使用 setter）

可以定义两类 properties observer

* `willSet` 在值存储之前调用，传入的参数是新存储的值
* `didSet` 在值存储后调用，传入的参数是旧存储的值

```swift
class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newTotalSteps) {
            print("About to set totalSteps to \(newTotalSteps)")
        }
        didSet {
            if totalSteps > oldValue  {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}
```

需要注意的是将属性传给带有 inout 参数的函数时 observer 总会被调用

## Property Wrappers

复用代码，提供属性的存储和属性的定义之间的中间层

定义 property wrapper 需要定义一个 structure/enumeration/class，其中定义一个 `wrappedValue` 属性

```swift
@propertyWrapper
struct TwelveOrLess {
    private var number: Int
    init() { self.number = 0 }
    var wrappedValue: Int {
        get { return number }
        set { number = min(newValue, 12) }
    }
}
```

使用 wrapper 只需在属性定义之前加上 wrapper 名

```swift
struct SmallRectangle {
    @TwelveOrLess var height: Int
    @TwelveOrLess var width: Int
}
```

这样就不需要为一系列需要特殊操作的属性每个单独写 getter/setter，如果需要为属性添加初始值，则要求 wrapper 有一个构造器，可以属性赋初始值，编译器会将其解释为 wrapper 构造器的输入参数之一

wrapper 还可以实现额外的功能，只需要定义一个 `projectedValue`，使用 `$` + 变量名访问一个使用了 wrapper 的变量即可访问 wrapper 中的 `projectedValue`

wrapper 本质是 getter 和 setter 的语法糖

## Global and Local Variables

上述能力同样适用于全局变量和局部变量，这些变量都是存储变量

但同样可以定义计算变量，或是为存储变量定义 observer

全局常量变量都是默认 lazy 的，而局部常量变量从不 lazy

## Type Properties

type properties 类似其他语言中类的静态成员，与类型关联，不论实例数量都只有一份

存储类属性必须有初始值，因为类没有构造器，这些属性都是 lazy 的，且在多线程环境下也只会被访问一次

只需要在属性前加上 `static ` 关键字即可

```swift
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}
```

这些属性要求以类而非类的实例访问