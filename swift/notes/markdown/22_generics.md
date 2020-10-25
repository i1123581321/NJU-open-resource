# Generics

泛型可以实现更加灵活的、对任意类型都适用的代码，是一种更高层面的抽象

## Generic Function

泛型的函数可以适用于任意类型，如

```swift
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

其中 `T` 为类型参数，不代表任何具体的类型，仅作占位符使用，可以提供多个类型参数，将其包在尖括号内并使用逗号分隔

如果类型参数是有意义的，则可以将其命名，如 `Dictionary<Key, Value>`

## Generic Type

swift 可以定义泛型类型，这些自定义的类型可以像 `Array/Dictionary` 一样使用任意类型

```swift
struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}
```

当使用 extension 扩展一个泛型类型时，不需要再写一遍类型参数列表，而是使用原有的

```swift
extension Stack {
    var topItem: Element? {
        return items.isEmpty ? nil : items[items.count - 1]
    }
}
```

## Generic Subscripts

subscript 可以是泛型的，在 `subscript` 关键字后引入类型参数，然后在类型和花括号之间加上 `where` 子句

```swift
extension Container {
    subscript<Indices: Sequence>(indices: Indices) -> [Item]
        where Indices.Iterator.Element == Int {
            var result = [Item]()
            for index in indices {
                result.append(self[index])
            }
            return result
    }
}
```

## Type Constraints

有时候需要对类型参数做出一些限制，指明使用的类型必须继承自某个类，或是实现某个 protocol，如 `Dictionary` 的 key 必须实现 `Hashable`

定义 constraint 的语法如下

```swift
func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
    // function body goes here
}
```

## Associated Types

当定义 protocol 时，可以定义一系列 associated type 作为占位符，实际的类型则等到实现时才能确定。使用 `associatedtype` 关键字定义

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

在类型实现时，可以用 `typealias` 来确定具体类型

```swift
typealias Item = Int
```

但这一声明不是必须的，swift 的类型推导功能可以推导出 `Item` 的类型

同样可以使用 extension 使一个现有类型实现带有 associated type 的 protocol

可以为 associated type 添加 constraint

```swift
protocol Container {
    associatedtype Item: Equatable
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

且一个 constraint 中可以包含 protocol 自身

```swift
protocol SuffixableContainer: Container {
    associatedtype Suffix: SuffixableContainer where Suffix.Item == Item
    func suffix(_ size: Int) -> Suffix
}
```

如实现了这个 protocol 的类型有一个 `suffix(_:)` 方法可以返回后面的 n 个元素，而返回的类型要求同样实现了这个 protocol，且其中 Item 的类型不能改变

## Generic Where Clauses

`where` 子句可以限定 associated type 必须满足的需求，如检查两个类型是否相等或是否满足了某个特定的 protocol

在函数中使用时将其写在类型之后，花括号之前

```swift
func allItemsMatch<C1: Container, C2: Container>
    (_ someContainer: C1, _ anotherContainer: C2) -> Bool
    where C1.Item == C2.Item, C1.Item: Equatable {

        // Check that both containers contain the same number of items.
        if someContainer.count != anotherContainer.count {
            return false
        }

        // Check each pair of items to see if they're equivalent.
        for i in 0..<someContainer.count {
            if someContainer[i] != anotherContainer[i] {
                return false
            }
        }

        // All items match, so return true.
        return true
}
```

可以在 extension 中使用 `where`

```swift
extension Stack where Element: Equatable {
    func isTop(_ item: Element) -> Bool {
        guard let topItem = items.last else {
            return false
        }
        return topItem == item
    }
}
```

在上下文中已经有泛型类型的情况下，也可以在没有 constraint 的情况下写 `where` 子句

```swift
extension Container {
    func average() -> Double where Item == Int {
        var sum = 0.0
        for index in 0..<count {
            sum += Double(self[index])
        }
        return sum / Double(count)
    }
    func endsWith(_ item: Item) -> Bool where Item: Equatable {
        return count >= 1 && self[count-1] == item
    }
}
```

同样可以将 associated type 与 `where` 结合

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }

    associatedtype Iterator: IteratorProtocol where Iterator.Element == Item
    func makeIterator() -> Iterator
}
```

包括继承 protocol 时也可以用 `where`

```swift
protocol ComparableContainer: Container where Item: Comparable { }
```

