# Subscripts

class，enumeration，structure 可以定义 subscript，用来访问集合中的元素

可以为一个类型定义多种 subscript，使用哪个取决于输入参数，也可以定义多参数的 subscript

## Syntax

定义 subscript 的语法类似方法的定义和计算属性的定义，指明输入输出后可以设置为只读或读写的

```swift
subscript(index: Int) -> Int {
    get {
        // Return an appropriate subscript value here.
    }
    set(newValue) {
        // Perform a suitable setting action here.
    }
}
```

如果是只读的，不需要 setter，因此可以省去 getter，直接将表达式写在大括号内

```swift
struct TimesTable {
    let multiplier: Int
    subscript(index: Int) -> Int {
        return multiplier * index
    }
}
```

## Subscript Options

subscript 可以接受任意数量的参数，这些参数可以是任意种类，同理，返回值也可以是任意种类

输入参数类似 function，但是没有 in-out parameter

subscript 可以重载，通过输入参数来与具体的绑定

同样可以定义与类型而非实例关联的 subscript

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
    static subscript(n: Int) -> Planet {
        return Planet(rawValue: n)!
    }
}
```

