# Error Handling

swift 提供了完整的抛出，捕获，传递，操作可恢复错误的机制

## Representing and Throwing Errors

swift 中的错误是实现了 `Error` 接口的类型，实现该接口表示这个类型可以被用作错误处理

enumeration 很适合组织起一系列错误类型

```swift
enum VendingMachineError: Error {
    case invalidSelection
    case insufficientFunds(coinsNeeded: Int)
    case outOfStock
}
```

用 `throw` 关键字来抛出错误

## Handling Errors

swift 中有四类处理错误的方法

* 将函数中的异常传递到其调用者
* 使用 `do-catch` 语句处理异常
* 使用 optional value
* 使用 assert 来终止程序

在可能会抛出异常的语句/调用前使用 `try` 关键字

### Propagation Errors

如果一个函数可能会抛出异常，在其参数后添加 `throws` 关键字

```swift
func canThrowErrors() throws -> String
```

这个函数会将其内部抛出的异常传递到调用其的域

`throw` 类似 `return`，会立即改变函数的控制流。调用该函数的域必须处理抛出的异常或者将自己声明为 `throws`，然后继续传递

### Do-Catch

使用 do-catch 可以用一段代码来处理异常，如果 do 中的语句抛出了异常，会被 catch 的语句捕获并处理

```swift
do{
    try expression
} catch pattern1{
    statements
} catch pattern2 where condition {
    statements
} catch pattern3, pattern4 where condition {
    statements
} catch {
    statements
}
```

如果一个 catch 没有 pattern，则其会捕获任意异常，并将其绑定到局部变量 `error`

catch 不是必须要处理异常，如果没有匹配的话可以将其继续传递，但是异常必须在某个域被处理，否则产生一个 runtime error

同时处理多种异常，可以将其用逗号分隔开

### Converting Errors to Optional Values

使用 `try?` 可以将一个 error 转换为 optional，如果有异常被抛出，则其值为 `nil`

```swift
let x = try? someThrowingFunction()
```

这种方法可以写出更精确的代码（`try` 显然不会在意表达式的返回值）

### Disabling Error Propagation

如果能够确信一个函数不会在运行时抛出异常，则在其前面加上 `try!` ，这会关闭异常的传播，如果确实发生了异常，则会得到一个 runtime error

## Specifying Cleanup Actions

如果代码有必要的清理工作，使用 `defer` 关键字，其中的代码会在当前块执行结束后执行，而结束方式可以是任何一种，无论是正常返回还是抛出异常，`defer` 定义的语句会在当前域结束的时候执行，而其中不能有任何控制转移语句。可以将 defer 块放在函数的任意位置，如果定义了多个 defer 块，会按照从下往上的顺序执行。

