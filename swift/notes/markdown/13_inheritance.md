# Inheritance

class 可以继承，从基类中获取属性，方法等特性，也可以对基类的方法，属性等重写

不继承其他类的类就是基类，swift 的类没有类似 Java 的 `Object` 这样的共有基类

继承一个基类，在定义派生类时将基类名写在类名后，冒号分割

```swift
class SomeSubclass: SomeSuperclass {
    // subclass definition goes here
}
```

## Overriding

对于继承自基类的实例方法，类方法，实例属性，类属性，subscript，派生类都可以提供自己的实现以代替基类的实现，这种行为称为重写（override）

重写时在方法定义前加上 `override` 关键字，这个关键字确保重写的正确性，避免意外地重写

如果想要调用基类的现有方法/属性，使用 `super` 引用

一个重写方法的例子如下

```swift
class Train: Vehicle {
    override func makeNoise() {
        print("Choo Choo")
    }
}
```

也可以重写属性的 getter 和 setter，必须写清属性名和类型，以便于编译器检查

```swift
class Car: Vehicle {
    var gear = 1
    override var description: String {
        return super.description + " in gear \(gear)"
    }
}
```

同样可以重写属性的 observer，但是不能同时重写 setter 和 observer

```swift
class AutomaticCar: Car {
    override var currentSpeed: Double {
        didSet {
            gear = Int(currentSpeed / 10.0) + 1
        }
    }
}
```

## Preventing Overrides

将方法/属性声明为 `final` 可以防止被派生类重写

将类声明为 `final` 可以防止被派生