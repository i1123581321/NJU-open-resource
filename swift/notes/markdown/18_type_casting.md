# Type Casting

类型转换是一种检查实例类型，或是将实例转换到其基类或派生类的机制

在 swift 中提供 `is` 和 `as` 操作符，进行类型的检查和转换

## Checking Type

可以检查某个实例是否属于某个特定的类型，使用 `is` 操作符即可

```swift
for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}
```

## Down-casting

可以将一个类型引用向下转型为其子类的引用，使用 `as?` 或是 `as!` 操作符

向下转型是可能会失败的，如果使用 `as?`，则会返回目标类型的一个 optional，如果不能转型则其值为 `nil`，使用 `as!` 进行向下转型失败的话会触发一个 runtime error

```swift
for item in library {
    if let movie = item as? Movie {
        print("Movie: \(movie.name), dir. \(movie.director)")
    } else if let song = item as? Song {
        print("Song: \(song.name), by \(song.artist)")
    }
}
```

转型并不改变对象的类型，而是引用的类型

## Any and AnyObject

swift 提供了两种非特定类型

* `Any` 能代表任何类型的实例
* `AnyObject` 能代表任意类的实例

只有在真的需要的时候才使用这两种类型（如创建一个混合类型的数组）

```swift
var things = [Any]()

things.append(0)
things.append(0.0)
things.append(42)
things.append(3.14159)
things.append("hello")
things.append((3.0, 5.0))
things.append(Movie(name: "Ghostbusters", director: "Ivan Reitman"))
things.append({ (name: String) -> String in "Hello, \(name)" })
```

对于 `Any` 类型的变量，使用 switch 配合 is/as 来判断其具体类型