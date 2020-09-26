# Methods

method 是与特定类型相关的函数，structure，class，enumeration 都可以定义实例方法和类方法

## Instance Methods

实例方法是与具体的类型实例结合的函数，与一般函数有相同的语法

实例方法可以访问同一类内的实例方法和属性

每个实例方法有一个隐含的属性 `self`，是对调用其的实例的引用。一般不用显式指明，除非参数名和类型内的属性名相同，此时需要显式注明 `self` 避免歧义

structure 和 enumeration 都是 value type，而 value type 的属性不能由实例方法更改，如果想在实例方法内更改属性，需要在函数前加上 `mutating` 关键字，这个方法会创建一个新的实例然后在方法结束后代替原本的实例

```swift
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
}
```

不能对常量调用 mutating 方法。如果是 enumeration，mutating 方法可以给 `self` 设置一个新的 case

## Type Methods

类方法是与类型本身关联的方法，在定义前加上 `static` 关键字（如果是 class 的话可以用 `class` 关键字，以让子类覆写这个方法）

调用类方法要用类型名而非具体实例，此时 `self` 指向的是类型本身，可以用来调用类属性和类方法

