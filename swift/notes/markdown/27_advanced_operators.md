# Advanced Operators

swift 提供了许多更高级的运算符，如位运算符，支持溢出的运算符，运算符重载，甚至自定义运算符

## Bitwise Operators

位运算符可以操作数据结构内部的 bit，swift 支持

* 按位非 `~`
* 按位与 `&`
* 按位或 `|`
* 按位异或 `^`
* 左移和右移 `<</>>`

## Overflow Operators

一般来说如果运算或者赋值的结果超过了对应类型所能描述的范围，swift 会产生一个运行时错误，但是如果想要使用二进制数的溢出效果，则需要使用对应的溢出运算符

* `&+`
* `&-`
* `&*`

溢出可以是正向的或者反向的

## Operator Methods

class 和 structure 可以重载运算符，使用一般重载的语法即可

```swift
struct Vector2D {
    var x = 0.0, y = 0.0
}

extension Vector2D {
    static func + (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y + right.y)
    }
}
```

除了一般的二元运算符，也可以重载一元运算符

```swift
extension Vector2D {
    static prefix func - (vector: Vector2D) -> Vector2D {
        return Vector2D(x: -vector.x, y: -vector.y)
    }
}
```

或者重载组合运算符（左边的参数需要是 in-out）

```swift
extension Vector2D {
    static func += (left: inout Vector2D, right: Vector2D) {
        left = left + right
    }
}
```

不能重载赋值运算符或是三元运算符

实现了 `Equatable` protocol 后可以重载等价运算符

```swift
extension Vector2D: Equatable {
    static func == (left: Vector2D, right: Vector2D) -> Bool {
        return (left.x == right.x) && (left.y == right.y)
    }
}
```

然后自动获得 `!=` 的实现，但大部分情况都是使用自动实现

## Custom Operators

可以自己定义操作符，具体能用作操作符的符号参见 [Operators](https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html#ID418)，使用 `operator` 关键字定义，`prefix/infix/postfix` 决定其类型

```swift
prefix operator +++

extension Vector2D {
    static prefix func +++ (vector: inout Vector2D) -> Vector2D {
        vector += vector
        return vector
    }
}

var toBeDoubled = Vector2D(x: 1.0, y: 4.0)
let afterDoubling = +++toBeDoubled
```

自定义的操作符默认的优先级高于三元运算符，也可以显式声明其优先级

```swift
infix operator +-: AdditionPrecedence
```

