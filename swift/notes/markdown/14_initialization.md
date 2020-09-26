# Initialization

初始化即创建类型的实例，这一过程通过定义一个构造器实现。构造器不返回值，其作用是确保类型被正确初始化

class 类可以定义析构器，用于执行清理工作

## Setting Initial Value

class 和 structure 必须在创建实例时设定所有存储属性的值，可以在定义时就设定为一个默认值，或是在构造器中初始化（初始化时不触发 observer）

构造器的形式为

```swift
init() {
    // perform some initialization here
}
```

构造器可以有参数，其语法和函数的参数语法相同，构造器不能省去 argument label

如果类型中的属性在构造器调用时也不能确定值，则将其声明为 optional 的，这些属性会初始化为 `nil`

在构造器中同样可以为常量的属性赋值，这一过程只能由常量所属类实现，不能由派生类操作

## Default Initializers

如果一个类型为所有属性提供了初始值，且没有提供构造器，swift 会生成一个默认的构造器，生成一个属性均为默认值的实例

structure 在没有提供构造器时会获得成员构造器，即使有属性没有默认值。这种情况下可以将初始化值作为参数传入构造器

```swift
struct Size {
    var width = 0.0, height = 0.0
}
let twoByTwo = Size(width: 2.0, height: 2.0)
```

## Initializer Delegation

构造器可以调用其他构造器，这种过程称为 initializer delegation

对于 value type，由于不能继承，所以调用其他构造器就是调用其他类的构造器

class 可以调用基类的构造器，用 `super.init` 引用

如果提供了一个显式的构造器，就不能使用默认构造器或成员构造器

## Inheritance and Initialization

class 中所有属性必须在构造器中初始化，swift 提供了两种构造器

* designated initializer
* convenience initializer

designated initializer 是基本的构造器，初始化所有属性，且调用基类的构造器。每个类至少有一个

convenience initializer 是辅助的构造器，可以调用 designated initializer 并为某些参数提供默认值，也可以直接创建实例

两种定义的语法如下

```swift
init(parameters) {
    statements
}
convenience init(parameters) {
    statements
}
```

swift 对于类的构造器有以下三条规则

* 一个 designated initializer 必须调用其基类的 designated initializer
* 一个 convenience initializer 必须调用同类里的其他构造器
* 一个 convenience initializer 最终必须调用一个 designated initializer

## Two-Phase Initialization

class 的构造分两个阶段，第一个阶段为所有存储属性设置一个初始值，第二阶段由各类自定义其属性。两步初始化保证了初始化过程的安全，确保属性在被访问前都被初始化

swift 编译器进行以下检查

* designated initializer 必须确保所有定义的属性都被初始化，然后再调用基类的构造器
* 在给继承的属性赋值时，designated initializer 必须先调用基类构造器
* 在给任意属性赋值时，convenience initializer 必须先调用其他构造器
* 构造器不能调用实例方法。或是访问实例属性，或是访问 `self`（除非所有属性都被赋了初值）

两个阶段的细节如下

* phase 1
  * 调用构造器
  * 为新的实例分配内存
  * designated initializer 确保所有属性都有了初值（本类定义的）
  * 调用基类构造器，直到达到继承链顶端
  * 到达顶端后所有内存区域都被初始化，第一步结束
* phase 2
  * 从继承链顶端向下返回，每个 designated initializer 有机会再次自定义，此时可以访问 `self`，访问实力属性，访问实例方法
  * 然后返回至可选的 convenience initializer

## Initializer Inheritance and Overriding

派生类不会默认继承基类的构造器，需要手动调用

可以重写基类的 designated initializer，此时必须显式注明 `override`，包括重写自动提供的默认构造器时

重写基类的 convenience initializer 时，由于这个构造器不可能被子类调用，故不用写 `override`

虽然派生类不默认继承基类的构造器，但是有一些例外情况，假设为派生类所有新属性提供了默认值

* 如果派生类没有定义 designated initializer，自动继承所有基类的 designated initializer
* 如果派生类为所有基类的 designated initializer 提供了实现（或是根据上一条规则自动继承，或是重写），则其自动继承所有基类的 convenience initializer

即使派生类自定义了 convenience initializer，上述规则仍生效

## Failable Initializer

有些情况下构造器可能会失败（如输入参数不合法），这种情况可以定义 failable initializer，只需将 `init` 替换为 `init?`

不能定义两个参数相同的 failable initializer 和 non-failable initializer

failable 的构造器会返回一个 optional 的变量

```swift
struct Animal {
    let species: String
    init?(species: String) {
        if species.isEmpty { return nil }
        self.species = species
    }
}
```

可以为 enumeration 定义 failable initializer，如果 enumeration 有 raw value，则会自动获得一个

构造失败可以传递，如果被调用的构造器失败了，则后续不会再进行，直接返回失败

派生类可以将基类的 failable initializer 重写为正常的构造器，这种情况要消除基类可能 fail 的原因

同样可以构造 `init!` 的构造器

## Required Initializer

在构造器前加上 `required` 指明所有派生类必须实现该构造器

```swift
class SomeClass {
    required init() {
        // initializer implementation goes here
    }
}

class SomeSubclass: SomeClass {
    required init() {
        // subclass implementation of the required initializer goes here
    }
}
```

在子类的构造器前也要加 `required`

## Initializer and Closure

可以用 closure 来定制属性的默认值

```swift
class SomeClass {
    let someProperty: SomeType = {
        // create a default value for someProperty inside this closure
        // someValue must be of the same type as SomeType
        return someValue
    }()
}
```

注意不能省略末尾的括号，这种情况是立即调用 closure 而非将其赋给这个属性