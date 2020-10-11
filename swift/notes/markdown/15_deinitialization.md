# Deinitialization

当一个类实例消亡前会调用析构器，使用 `deinit` 来定义。只有 class 类型有析构器

## How Deinitialization Works

swift 的 GC 实现方式为 ARC（Automatic Reference Counting），一般不需要手动清理。但是有时候需要进行一些自定义的清理工作时就需要析构器了，其定义为

```swift
deinit {
    // perform the deinitialization
}
```

析构器一个类只能有一个，不接受参数，在 GC 发生前自动调用，当继承时，基类的析构器自动在派生类析构器调用末尾调用。析构器可以访问实例是所有属性