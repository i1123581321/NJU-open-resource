# 高级 MapReduce 编程技术

## 复合键值对使用

利用 MapReduce 框架对 key 排序的性质，将 value 中需要排序的部分加入 key 组成复合的键值对

需要实现自定义的 partitioner 保证 key 相同的键值对被分到同一个节点

也可以把小的键值对合成大的键值对

## 用户自定义类型

如果用户自定义数据类型，作为 value 需要实现 Writable 接口，作为 key 需要实现 WritableComparable 接口

## 用户自定义输入输出格式

可以自定义 InputFormat 和 RecordReader

实现 InputFormat 需要继承原本的 FileInputFormat，实现 RecordReader 的工厂方法

同理输出

## 用户自定义 Partitioner 和 Combiner

定制 partitioner 可以改变 map 输出结果到 reduce 的分区方式

定制 combiner 可以合并 map 的输出，减少网络数据传送量

## 迭代 MapReduce 计算

一些求解需要多次迭代以逼近结果，如 pagerank 算法

## 组合式 MapReduce

可以将多个 MapReduce 子任务串起来执行，需要为每个 job 提供独立的 conf

如果任务间有依赖关系，可以在程序中设定，使用 JobControl 类

也可以使用链式的 mapper 或者 reducer

## 多数据源的连接

MapReduce 没有实现 join 操作，需要用户自己实现，常用方法有 map 端的 join 和 reduce 端的 join

reduce 端 join 将需要 join 的键作为 key，其余列作为 value 发送，在 reduce 端完成 join

可以使用 DataJoin 类

当 join 一方比较小时，也可以用文件共享的方式实现 map 端 join，减少通信开销

## 全局参数的传递

传递全局参数可以在 configuration 里设定

如果是比较大的文件可以使用 distributed cache 技术

## 其他技术

一些计算相关的信息可以在 Configuration 对象中查到

可以用 MultipleOutputFormat 将输出划分为多个文件

可以用 DBInputFormat 和 DBOutputFormat 与数据库通信

