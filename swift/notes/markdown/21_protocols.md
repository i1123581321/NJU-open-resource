# Protocols

protocol 定义为满足某些功能所需的方法和属性，然后可以被某些类型实现

protocol 同样可以扩展

## Syntax

使用 `protocol` 关键字来定义，其形式非常类似 class/structure 的定义

```swift
protocol SomeProtocol {
    // protocol definition goes here
}
```

实现 protocol 的类型需要在类型名后显式声明

```swift
class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
    // class definition goes here
}
```

可以用 `is` 关键字来检查某个类型是否实现了 protocol，或是使用 `as` 进行向下转型

## Requirements

### Properties Requirements

protocol 可以要求任何实现其的类型提供特定名称和类型的属性（无论是类型属性还是实例属性），同时也定义其是 gettable 或是还需要 settable

```swift
protocol SomeProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
}
```

如果需要实现类属性，则加上 `static` 关键字

```swift
protocol AnotherProtocol {
    static var someTypeProperty: Int { get set }
}
```

如果 protocol 没有被按要求满足，则会产生一个编译期错误

### Method Requirements

protocol 可以要求实现其的类型提供特定方法，这些方法的定义形式类似一般方法，但是没有花括号包起来的实现体。protocol 定义的方法不能有默认参数

同样，如果需要类方法，在方法定义前加上 `static` 关键字

如果方法需要修改实例，则在定义前加上 `mutating` 关键字，这使得 structure/enumeration 可以实现该 protocol，如此定义后在 class 实现该接口时可以不用写 `mutating` 关键字。

### Initializer Requirements

protocol 可以要求特定的构造器

```swift
protocol SomeProtocol {
    init(someParameter: Int)
}
```

对于 class 来说，可以将其实现为 designated initializer 或是 convenience initializer，但是必须要加上 `required` 关键字以使得子类也实现该构造器（除非类是 final 的）

在派生类实现该构造器时，加上 `required` 和 `override`

protocol 同样可以定义 failable 的构造器

## Protocol as Types

Protocol 可以作为类型，就和正常类型一样，因此 protocol 名同样需要首字母大写。

* 作为参数类型或者返回类型
* 作为常量，变量或者属性的类型
* 作为容器中元素的类型

可以将 protocol 向下转型为实际类型来使用额外方法

将 protocol 作为类型可以实现多态

## Delegation

委托模式是设计模式的一种，一个对象可以将其职责委托给其他对象，可以使用一个 protocol 定义委托的需求，然后实现该 protocol 的类型可以处理委托

具体实例见 swift 文档

## Adding Protocol Conformance with an Extension

如果想让现有类型实现 protocol，可以使用 extension 的语法

```swift
extension Dice: TextRepresentable {
    var textualDescription: String {
        return "A \(sides)-sided dice"
    }
}
```

如果类型是泛型，需要在某些特定情况下实现 protocol，则可以采用条件的形式

```swift
extension Array: TextRepresentable where Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}
```

而如果类型本身已经满足了 protocol，则可以定义一个空的 extension 来显式指明这一事实

## Adopting a Protocol Using a Synthesized Implementation

如果类型的实现满足某些条件，则可以自动实现某些 protocol，这免去了繁杂的代码编写

如 swift 的 `Equatable`

* 只有存储属性的 structure 实现 Equatable
* 只有实现了 Equable 的 associated type 或者没有 associated type 的 enumeration 实现 Equatable

然后显式声明实现了 Equatable 即可自动获得 `==` 和 `!=` 的实现

```swift
struct Vector3D: Equatable {
    var x = 0.0, y = 0.0, z = 0.0
}

let twoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
let anotherTwoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
if twoThreeFour == anotherTwoThreeFour {
    print("These two vectors are also equivalent.")
}
```

对于 Hashable，条件和 Equable 相同，类型实现满足条件的话声明实现了 Hashable 则可获得 `hash(into:)` 的实现

对于 Comparable，如果 enumeration 没有 raw value，且 associated type 均实现了 Comparable，则其实现 Comparable，声明后获得 `</<=/>/>=` 的实现

## Protocol Inheritance

一个 protocol 可以继承一个或多个 protocol，语法类似类型的继承

```swift
protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
    // protocol definition goes here
}
```

继承可以扩展 protocol 的需求

如果想要限定一个 protocol 只能被 class 实现，可以在继承列表中加上 `AnyObject`

## Protocol Composition

protocol 同样可以组合，组合不会产生新的 protocol。组合的 protocol 通过 `&` 连接起来

```swift
protocol Named {
    var name: String { get }
}
protocol Aged {
    var age: Int { get }
}
struct Person: Named, Aged {
    var name: String
    var age: Int
}
func wishHappyBirthday(to celebrator: Named & Aged) {
    print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
}
let birthdayPerson = Person(name: "Malcolm", age: 21)
wishHappyBirthday(to: birthdayPerson)
```

## Optional Protocol Requirements

可以在 protocol 中定义可选的需求，这些需求不是一定要被实现，这样的需求是为了和 oc 的代码互操作，可选的需求前面加 `optional` 关键字，同时 protocol 和 `optional` 前加 `@objc`

optional protocol 只能在继承自 oc 的类上使用

```swift
@objc protocol CounterDataSource {
    @objc optional func increment(forCount count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}
```

如果要调用一个 optional protocol，使用 optional chaining

## Protocol Extensions

同样可以使用 extension 来扩展 protocol 的内容，这样可以为 protocol 添加方法，构造器，subscript 或是计算属性，实现 protocol 的类型也会获得这些内容

```swift
extension RandomNumberGenerator {
    func randomBool() -> Bool {
        return random() > 0.5
    }
}
```

扩展能添加实现，却不能让 protocol 继承自别的 protocol

使用 extension 也可以为已有的需求添加默认的实现，或是使用 `where` 添加限制

```swift
extension Collection where Element: Equatable {
    func allEqual() -> Bool {
        for element in self {
            if element != self.first {
                return false
            }
        }
        return true
    }
}
```

