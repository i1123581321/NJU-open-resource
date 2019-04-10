[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# Model of Computation

## RAM Model

### Computing

什么是计算？

* 将信息编码为 0/1
* 对 0/1 进行简单的处理
* 将 0/1 解码

计算是基于有限种操作的组合来完成复杂的任务

**算法**：算法就是一组计算机操作的序列，遵循算法的指示，计算机对任意合法输入执行一系列操作，并给出正确输出

### 计算模型

建立一个机器无关、语言无关的抽象模型——RAM（Random Access Machine）

RAM 的基本构成：

* 只读的输入纸带，由一个个空位组成，每个空位存储一个整数
* 只写的输出纸带，由一个个空位组成
* 存储空间
* 程序：指令的序列
  * 简单操作：现实计算机上常见的合理的简单操作，如比较整数，比较字符，结点染色等
  * 复杂操作：循环，子程序调用
  * 访存：内存的读和写，属于简单操作

单位代价 RAM （unit-cost RAM）：每个简单操作均可在单位时间内完成

某些时候为了更准确的分析需要对数代价 RAM （log-cost RAM）

### Further reading - 更精确的计算模型

外部存储模型（external memory model）

PRAM （Parallel Random Access Machine）

## Algorithm Design

### Specification

明确定义算法问题（algorithmic problem）

> **定义 1.1** 算法问题规约（specification）：一个算法问题的规约主要包括两部分
>
> * 输入：明确规定了算法接受的所有合法输入
> * 输出：明确规定了对于所有合法输入值，相应的输出值应该是什么

### Correctness - Mathematical Induction

要证明一个可数无穷多的集合中的每个元素均满足某种性质，主要手段即是数学归纳法

> **定义 1.2** 弱数学归纳法：假设 $P$ 是一个定义在自然数集合 $\N$ 上的命题
>
> 如果：
>
> * $P(1)​$ 为 TRUE
> * $\forall k \in \N, P(k) \rightarrow P(k + 1)$
>
> 则对所有自然数 $n$，$P(n)​$ 为 TRUE

>**定义 1.3** 强数学归纳法：假设 $P$ 是一个定义在自然数集合 $\N$ 上的命题
>
>如果：
>
>* $P(1)$ 为 TRUE
>* $\forall k \in  \N, P(1) \wedge P(2) \wedge \dots P(k) \rightarrow P(k+1)$
>
>则对所有自然数 $n$，$P(n)$ 为 TRUE

以数学归纳法证明算法正确性的关键：**将算法无穷多的输入情况按某种原则变成无限个关于自然数的命题**

**良序原理与数学归纳法是等价的**，[Well-ordering theorem](https://en.wikipedia.org/wiki/Well-ordering_theorem)， [Well-ordering principle](https://en.wikipedia.org/wiki/Well-ordering_principle)（Tuturial 1 详细讲解）

## Algorithm Analysis

### 算法的性能指标

如何测量？

测量不能过于精确 $\rightarrow$ 依赖因素过多：机器/编程语言/编程范式/具体实现 $\rightarrow$ 神奇的 RAM 模型

对于时间复杂度，统计简单操作的个数，对于空间复杂度，统计使用的存储单元数量，**将算法分析转变为计数问题**

实际分析中算法时间复杂度的分析不是统计简单操作而是统计 **关键操作（critical operation）** 

|     算法问题     |      关键操作      |
| :--------------: | :----------------: |
| 排序、选择、查找 |     元素的比较     |
|      图遍历      |   结点信息的处理   |
|      串匹配      |     字符的比较     |
|     矩阵运算     | 两个矩阵元素的运算 |

算法分析的本质：得到输入规模 $n$ 到算法复杂度的函数关系 $f(n)$

### Worst-case Complexity

$W(n)$ ：最坏情况时间复杂度，时间复杂度的上界

> 当问题输入规模为 $n$ 时，算法所有可能的输入集合记为 $D_n$ ，一个具体的算法输入实例记为 $I$ ，$f(I)$ 表示对具体的输入 $I$ 的算法的时间复杂度，则一个算法的最坏情况时间复杂度为：
> $$
> W(n) = \max_{I \in D_n}f(I)
> $$

### Average-case Complexity

$A(n)$ ：平均情况时间复杂度，加权平均值（期望）

> 假设算法的所有可能输入服从某个概率分布，算法的时间复杂度成为随机变量，而它的期望值 $A(n)$ 定义为算法的 **平均情况时间复杂度** 。记每个输入 $I$ 出现的概率为 $\Pr\{I\}$
> $$
> A(n) = \sum_{I \in D_n}\Pr\{I\} \times f(i)
> $$

### Further Reading - Advanced topics of algorithm analysis

Lower Bound

优化（贪心/动态规划）

Computation complexity

Approximate/online/randomized algorithms