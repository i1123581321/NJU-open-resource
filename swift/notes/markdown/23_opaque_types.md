# Opaque Types

如果一个函数的返回值是 opaque type，则其隐藏了返回值的具体类型，而是返回一个以 protocol 描述的类型。不同于直接返回 protocol，返回 opaque type 时编译器是知道具体的类型的，只是调用者不知道

## Returning an Opaque Type

opaque type 可以认为是反向的泛型

```swift
func makeTrapezoid() -> some Shape {
    let top = Triangle(size: 2)
    let middle = Square(size: 2)
    let bottom = FlippedShape(shape: top)
    let trapezoid = JoinedShape(
        top: top,
        bottom: JoinedShape(top: middle, bottom: bottom)
    )
    return trapezoid
}
```

这个函数返回的类型是 `some Shape`，表示返回了某个实现了 Shape 的类型

可以将 opaque type 和泛型结合在一起使用

```swift
func flip<T: Shape>(_ shape: T) -> some Shape {
    return FlippedShape(shape: shape)
}
func join<T: Shape, U: Shape>(_ top: T, _ bottom: U) -> some Shape {
    JoinedShape(top: top, bottom: bottom)
}
```

但是如果有多个返回类型，其必须是同一个类型

```swift
func invalidFlip<T: Shape>(_ shape: T) -> some Shape {
    if shape is Square {
        return shape // Error: return types don't match
    }
    return FlippedShape(shape: shape) // Error: return types don't match
}
```

## Difference Between Opaque Types and Protocol Types

虽然返回 opaque type 看起来和返回 protocol type 十分相似，但是其对待具体类型的方式不同。

* opaque type 只能指向具体的某个类型，即使调用者不知道这个类型
* protocol type 可以指向所有实现了该 protocol 的类型

相比之下 protocol type 更灵活，限制也更宽松，但丢失的信息也更多

不仅如此，返回 protocol 的函数不能嵌套，因为一个 protocol 类型的值没有实现该 protocol