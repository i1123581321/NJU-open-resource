[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# Preliminaries

## Mathematical Preliminaries

### Sets

集合根据元素数量可分为 finite set 和 infinite set

Universal set: all possible elements

集合的操作：$\cup$ (Union), $\cap$ (Intersection), $-$ (Difference), $\overline{A}$ (Complement)

De Morgan's Law: 
$$
\overline{A \cup B} = \overline{A} \cap \overline{B}\\
\overline{A \cap B} = \overline{A} \cup \overline{B}
$$
Null set: $\varnothing$

Subset: $A \subseteq B$ , 如果 $A \neq B$ 即为 proper subset，记为 $A \subset B$

Disjoint Sets: $A \cap B = \varnothing$

集合中元素的数量称为集合的势（Cardinality），记为 $|A|$

**Power set**s: a set of sets, 是所有子集的集合，记为 $P(S), 2^{S}$ ，有 $|2^{S}| = 2^{|S|}$

Cartesian Product: 笛卡尔积，$|A \times B| = |A| \cdot |B|$ 

### Functions

给定集合 $A, B$ ，函数 $f$ ，函数将每个 $A$ 中的元素映射到至多一个 $B$ 中的元素，记为
$$
f: A \to B
$$
total function: $A = $ domain

injective function: $\forall a, a' \in A, a \neq a' \to f(a) \neq f(a')$

surjective function: $\forall b \in B, \exist a \in A, f(a) = b$

**bijective function**: total, injective and surjective

Big O notation: 参见 [Asymptotic](https://i1123581321.github.io/NJU-open-resource/algorithm_design_and_analysis/notes/L_2.pdf)

### Relations

Given two sets, $A, B$ , a **relation** $R$ is any subset of $A \times B$

Equivalence Relations: Reflexive, Symmetric and Transitive

对于一个等价关系 $R$ ，可定义 Equivalence Class
$$
[x]_{R} = \{y: x R y\}
$$
两个等价类之间的关系只有相等或 disjoint

对于 $A$ 上的关系 $R$ ，有

* Partial order: Reflexive, Transitive and **Antisymmetric**
* Total order: partial order and $\forall a, b \in A$ , either $aRb$ or $bRa$, also called **linear order**

### Graphs

a directive graph $G = <V,E>$

* Walk: a sequence of adjacent edges
* Path: a walk where no edge is repeated
* Simple path: a path where no node is repeated
* Cycle: a walk from a node to itself
* Simple cycle: only the base node is repeated

A
**tree** is a directed graph that has no **cycle**.

### Proof Techniques

归纳法 or 归谬法

鸽笼原理

## String and Languages

### Alphabet and string

Alphabet: 符号的有限集合，记为 $\Sigma$

String: alphabet 中的符号组成的序列（有穷？）

空串即没有符号的 string ，记为 $\lambda$ 或是 $\epsilon$

$\Sigma^{*}$: the set of all possible strings from alphabet $\Sigma$ (including $\lambda$)

$\Sigma^{+}$: the set of all possible strings from alphabet $\Sigma$ except $\lambda$ , $\Sigma^{+} = \Sigma^{*} - \{\lambda\}$

string 有几种运算，对于 string $w = a_{1}a_{2}\dots a_{n}, v = b_{1}b_{2}\dots b_{m}$

* concatenation: $wv = a_{1}a_{2}\dots a_{n}b_{1}b_{2}\dots b_{m}$
* reverse: $w^{R} = a_n\dots a_{2}a_{1}$
* length: The length of a string $x$ is the number of
  symbols contained in the string $x$, denoted by $|x|$. $|w| = n, |wv| = |w| + |v|, |\lambda| = 0$
* substring: $s$ is a substring of $x$ if there exist strings $y$ and $z$ such that $x = ysz$ ($y, z$ can be empty string) 
* prefix: when $x = sz(y = \epsilon)$ , $s$ is called a prefix of $x$
* suffix: when $x = ys(z = \epsilon)$ , $s$ is called a suffix of $x$
* $w^{n}=\underbrace{w w \cdots w}_{n} , w^{0} = \lambda$

解决字符串相关的问题时，一般根据其**长度**进行分情况讨论

### Languages

Language 是 string 的集合，即 $\Sigma^{*}$ 的子集

> e.g. $L = \{a^{n}b^{n}:n \geqslant 0\}$ ，这个 Language 不能通过正则描述

由于 Language 本质是集合，故集合的操作同样适用于 Language（Union，Intersection，Difference，Complement），$\overline{L} = \Sigma^{*} - L$

除此之外还有一些 Language 独有的操作

* reverse: $L^{R} = \{w^{R} :w \in L\}$
* concatenation: $L_{1}L_{2} = \{xy: x \in L_{1}, y \in L_{2}\}$
* $L^{n}=\underbrace{L L \cdots L}_{n}, L^{0} = \{\lambda\}$
* Kleene Closure: $L^{*} = \bigcup_{i=0}^{\infin}L^{i}$
* Positive Closure: $L^{+} = \bigcup_{i=1}^{\infin}L^{i} = L^{*} - \{\lambda\}$