# Structures and Classes

structure 和 class 是用于用户自定义类型的数据结构

## Comparing

structure 和 class 有多种相似的要素

* 都能定义属性来存储值
* 都能定义方法来提供功能
* 可以用下标方式访问值
* 有构造器
* 可以扩展
* 可以实现 protocol

不同之处在于 class 可以继承，且支持转型。class 还有析构器，引用计数可以让一个 class instance 有多个引用

一般来说 class 的复杂性提升了消耗，只有在必要时才定义 class

structure 用 `struct` 关键字定义，class 用 `class` 关键字定义，然后可以根据名称创建实例

定义属性可以直接在内部定义，使用 `var` 或是 `let`，访问时使用 `.` 运算符

structure 有一个默认的成员构造器，可以用此构造器为属性赋初始值

## Value type vs. Reference type

structure 和 enumeration 都是 value type，即分配给变量或者常量或是作为参数传递给函数时，拷贝整个 instance。swift 为常用的 value type 做了优化，在分配后拷贝的实例和原本的共享内存空间，直到其中一个被修改后才执行拷贝

不同的是 class 是 reference type，当分配给变量，常量或作为参数时， 不复制原本的实例，而是复制对原本实例的又一个引用

因为一个 class instance 可以有多个引用，所以需要判断两个 reference 是否指向同一 instance，swift 提供了两个操作符：`===/!==` ，而 `==` 的含义则是由类的设计者决定的

