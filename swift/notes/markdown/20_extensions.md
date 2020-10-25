# Extensions

extension 可以为现有的 class，structure，enumeration 或者 protocol 加入新的功能，包括没有权限访问源码的类型

extension 可以

* 添加计算的类属性或者实例属性
* 定义实例方法或者类方法
* 提供新构造器
* 定义 subscript
* 定义嵌套类型
* 让现有类型实现接口

## Syntax

使用 `extension` 关键字定义

```swift
extension SomeType: SomeProtocol, AnotherProtocol {
    // implementation of protocol requirements goes here
}
```

同样可以为泛型扩展

## Computed Properties

可以为现有类型扩展属性

```swift
extension Double {
    var km: Double { return self * 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
let oneInch = 25.4.mm
print("One inch is \(oneInch) meters")
// Prints "One inch is 0.0254 meters"
let threeFeet = 3.ft
print("Three feet is \(threeFeet) meters")
// Prints "Three feet is 0.914399970739201 meters"
```

## Initializer

同样可以为现有类型扩展构造器，可以接受自定义的参数。extension 可以添加 convenience initializer，但不能添加 designated initializer 或者析构器

如果是为没有自定义构造器的 value type 添加构造器，则可以调用其默认构造器和成员构造器

> 默认构造器为所有成员赋默认值，成员构造器可以将参数赋给指定成员，如果定义了构造器则不能使用这两种构造器，但是扩展的构造器不受此限制

## Methods

可以为现有类型添加新的方法

```swift
extension Int {
    func repetitions(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}
```

如果扩展方法要修改 value type 的值，则同样需要 `mutating` 关键字

## Subscript

同样可以为现有类型扩展 subscript

```swift
extension Int {
    subscript(digitIndex: Int) -> Int {
        var decimalBase = 1
        for _ in 0..<digitIndex {
            decimalBase *= 10
        }
        return (self / decimalBase) % 10
    }
}
746381295[0]
// returns 5
```

## Nested Types

可以在现有类型中定义嵌套类型

```swift
extension Int {
    enum Kind {
        case negative, zero, positive
    }
    var kind: Kind {
        switch self {
        case 0:
            return .zero
        case let x where x > 0:
            return .positive
        default:
            return .negative
        }
    }
}
```

