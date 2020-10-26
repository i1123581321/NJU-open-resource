# Access Control

访问控制可以用于实现封装，swift 可以为不同的实体提供不同的访问权限

swift 的访问控制模型基于 module 和源文件，一个 module 是一个代码分发的基本单位，如一个框架或是一个应用。module 可以用 `import` 关键字导入

一个源文件是一个单独的 swift 源代码文件，其中可以定义多个类型或函数

## Access Levels

swift 提供了五种不同的访问级别，这些访问级别是跟定义实体的源代码文件与 module 相关的

* open access 和 public access 可以让实体在任何源文件内都可用
* internal access 限制只有 module 内的源文件可以任意使用实体
* file-private access 限制实体只能在其定义的源文件内使用
* private access 限制实体只能在定义的域和同一文件内的 extension 中使用

在定义 swift 的访问级别时有一个基本原则：不能用一个访问更严格的实体来定义实体，如不能用一个 internal/file-private/private 的类型来定义一个 public 的变量，一个函数的访问级别不能高于其参数和返回类型

绝大多数实体默认的访问级别是 internal access

## Access Control Syntax

用如下语法定义不同访问级别的实体

```swift
public class SomePublicClass {}
internal class SomeInternalClass {}
fileprivate class SomeFilePrivateClass {}
private class SomePrivateClass {}

public var somePublicVariable = 0
internal let someInternalConstant = 0
fileprivate func someFilePrivateFunction() {}
private func somePrivateFunction() {}
```

访问级别还会影响类型内部成员默认的访问级别，如果类型为 private/file-private，则其成员也有相同的访问级别，而如果定义类型为 public，其成员默认为 internal

对于 tuple 来说，其访问级别是所有成员中最严格的访问级别，对于函数来说，其访问级别是所有参数和返回类型中最严格的访问级别，如果函数的访问级别和上下文默认的不符，必须显式地在声明时指出

```swift
private func someFunction() -> (SomeInternalClass, SomePrivateClass) {
    // function implementation goes here
}
```

enumeration 的 case 和其定义有相同的访问级别，而其 raw value 和 associated value 的访问级别必须至少和 enumeration 一样高

嵌套类型的访问级别和包含类型的一致，除非包含类型是 public，则其访问级别默认为 internal

泛型的访问级别是其自身和 constraints 的访问级别的最小值

type alias 的访问级别可以比原类型低

## Subclassing

在同一 module 中，可以派生在当前上下文中可访问的类，而如果类是从别的 module 导入，则只能派生访问级别为 open 的类（这也是 open 和 public 的区别）

派生类的访问级别不能高于基类

覆写的规则和派生是一致的，在同一 module 内可以覆写所有可见的成员，而在别的 module 中只能覆写访问级别为 open 的成员。覆写可以提升访问级别

```swift
public class A {
    fileprivate func someMethod() {}
}

internal class B: A {
    override internal func someMethod() {}
}
```

甚至可以在覆写的方法内调用访问级别更低的方法，只要定义方法的上下文中该方法可用即可

```swift
public class A {
    fileprivate func someMethod() {}
}

internal class B: A {
    override internal func someMethod() {
        super.someMethod()
    }
}
```

## Constants, Variables, Properties, and Subscripts

常量/变量/属性的访问级别不能超过其类型的访问级别，对于 subscript 来说，其访问级别不能超过 index 或返回类型的访问级别

```swift
private var privateInstance = SomePrivateClass()
```

getter 和 setter 默认访问级别和其关联的实体一致，也可以显式定义更低的访问级别来限制读写域

```swift
struct TrackedString {
    private(set) var numberOfEdits = 0
    var value: String = "" {
        didSet {
            numberOfEdits += 1
        }
    }
}
```

## Initializers

自定义的构造器访问级别不高于其类型的访问级别，除了 required initializer，其访问级别必须和其所属的类相同

构造器和其参数的访问级别关系与函数相同。默认构造器的访问级别和其类型相同，但如果类型的访问级别是 public，默认构造器的访问级别是 internal，如果想要 public 的访问级别则需要显式提供

对于 structure 来说，默认的成员构造器和访问级别最低的成员一致

## Protocols

为 protocol 定义访问级别可以让其只能在满足访问级别的上下文被实现，protocol 内部的 requirements 自动获得与 protocol 相同的访问级别，不能自定义，这保证了所有 requirements 对于所有实现了 protocol 的类型都是可见的

继承的 protocol 访问级别不能高于原本的 protocol

一个类型可以实现一个访问级别不高于其的 protocol，其实现的部分的访问级别必须不低于 protocol 的访问级别，比如一个 public 的类型实现了 internal 的 protocol，则其内部实现必须至少有 internal 的访问级别

## Extensions

可以在任意可访问类型的上下文对类型进行扩展，扩展的成员有原成员一样的访问级别，可以显式为 extension 标记访问级别，这样扩展的成员默认有被标记的访问级别

如果是在类型定义的文件进行 extension，则扩展被看作是声明的一部分，这使得声明可以以更有条理的方式组织

```swift
struct SomeStruct {
    private var privateVariable = 12
}

extension SomeStruct: SomeProtocol {
    func doSomething() {
        print(privateVariable)
    }
}
```

