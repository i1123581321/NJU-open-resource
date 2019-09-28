[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# Regular Expressions

## Regular expression

### Definition

Regular expressions describe language(regular languages)

If $E$ is a regular expression, $L(E)$ is the language it defines

RE 的定义是递归的。RE 使用三种基本操作：Union, Concatenation, Kleene Star

* Union: $L \cup M$
* Concatenation: $LM = \{wx:w \in L \text{ and } x \in M\}$
* Kleene Star: $L^{*} = \{\epsilon\} \cup L \cup LL \cup \dots$

Basis.

* Basis 1: If $a$ is any symbol, then $a$ is a RE, $L(a) = \{a\}$
* Basis 2: $\epsilon$ is a RE, $L(\epsilon) = \{\epsilon\}$
* Basis 3: $\varnothing$ is a RE, $L(\varnothing) = \varnothing$

Induction.

* Induction 1: If $E_1, E_2$ are RE, $E_{1} + E_{2}$ is a RE, $L(E_{1} + E_{2}) = L(E_{1}) \cup L(E_{2})$
* Induction 2:  If $E_1, E_2$ are RE, $E_{1}E_{2}$ is a RE, $L(E_{1}E_{2}) = L(E_{1}) L(E_{2})$
* Induction 3: If $E$ is a RE, then $E^{*}$ is a RE, $L(E^{*}) = (L(E))^{*}$

操作优先级由高到低是 $*, \text{concatenation}, +$

### Equivalence of RE and FA

#### RE to FA

For every RE, there is a FA that accepts the same language

Pick $\epsilon$-NFA

Basis.

$\epsilon$ 

![2019-09-12_11-29-28.png](https://i.loli.net/2019/09/12/jYezot9VKlbcJiH.png)

$a$

![2019-09-12_11-30-04.png](https://i.loli.net/2019/09/12/2wLVpajeXlzKRbv.png)

Induction. 假设正则表达式 $s, t$ 的 NFA 为 $N(s), N(t)$ 

运算 $s \mid t$ 

![2019-09-12_11-30-25.png](https://i.loli.net/2019/09/12/1DUqmgXzQ43aPls.png)

运算 $st$

![2019-09-12_11-30-43.png](https://i.loli.net/2019/09/12/T5hetbCRwro8qf9.png)

运算 $s^*$

![2019-09-12_11-31-16.png](https://i.loli.net/2019/09/12/VrByIch5gMbNA2O.png)

#### FA to RE

For every FA, there is a RE defining its language

Pick DFA

使用归纳。假设 DFA 的状态为 $1,2, \dots, n$

定义 $k$-Path: A $k$-Path is a path through the graph of the DFA that goes through **no state numbered higher than** $k$

$k$-path 的 endpoint 没有限制，$n$-path 可以是任意路径

则该 DFA 对应的 RE 是所有从开始状态到接受状态的 $n$-path 的 RE 的集合

其正确性的证明基于对 $k$ 的归纳，令 $R_{ij}^{k}$ 为从状态 $i$ 到状态 $j$ 的 $k$-path 上的 label 表示的 RE

Basis. $k = 0$ ，此时 $R_{ij}^{0}$ 是从 $i$ 到 $j$ 所有边上的标号的和

* 若没有边，则为 $\varnothing$
* 若 $i = j$ ，则需要加上 $\epsilon$

Induction. 从 $i$ 到 $j$ 的 $k$-path，或者经过状态 $k$ （一次或多次），或者不经过状态 $k$

* 经过状态 $k$ ：$R_{ik}^{k-1}(R_{kk}^{k-1})^{*}R_{kj}^{k-1}$
* 不经过状态 $k$ ：$R_{ij}^{k-1}$

故
$$
R_{ij}^{k} = R_{ij}^{k-1} + R_{ik}^{k-1}(R_{kk}^{k-1})^{*}R_{kj}^{k-1}
$$
The RE with the same language as the DFA is the union of $R_{ij}^{n}$ where

* $n$ is the number of states
* $i$ is the start state
* $j$ is one of the final states

### Algebraic Laws for RE

* Union is commutative and associative, concatenation is associative

* Concatenation distributes over union
* $\varnothing$ is the identity for +, $\varnothing + R = R + \varnothing = R$
* $\epsilon$ is the identity for concatenation, $\epsilon R = R \epsilon = R$
* $\varnothing$ is the annihilator for concatenation, $\varnothing R = R\varnothing = \varnothing$

## Properties of Regular Languages

### Properties

A **language class** is a set of languages

Language classes have two important kinds of properties

* Decision properties （判定性）
* Closure properties （封闭性）

Closure properties: given languages in the class, an operation produces another language in the same class

**Decision properties**: an **algorithm** that takes a formal description of a language and tells whether or not some property holds

* Membership problem: is string $w$ in regular language $L$
* Emptiness problem: does the language contain any string at all

### Pumping Lemma

Let $L$ be a regular language. Then there exists a constant $n$ (which depends on $L$) such that for every string $w$ in $L$ such that $|w| \geqslant n$ , we can break $w$ into three strings, $w = xyz$ , such that:

1. $y \neq \epsilon$
2. $|xy| \leqslant n$
3. For all $k \geqslant 0$, the string $xy^{k}z$ is also in $L$

### Decision Properties of Regular Language

#### The membership problem

Problem: Given a string $w$ and a regular language $L$ , is $w$ in $L$

Algorithm: Simulate the DFA, if the DFA ends in an accepting state, the answer is "yes", otherwise the answer is "no"

#### The emptiness problem

Problem: Given a regular language, does the language contain any string at all

Algorithm: Compute the set of states **reachable** from the start state. If at least one final state is reachable, then yes, else no.

> Basis. The start state is surely reachable from the start state.
>
> Induction. If state $q$ is reachable from the start state, and there is an arc from $q$ to $p$ with any label (input or $\epsilon$), then $p$ is reachable

如果语言由 RE 给出，则可根据以下递归规则判断是否为空

> Basis. $\varnothing$ denotes the empty language, $\epsilon$ and $a$ for any input symbol $a$ do not.
>
> Induction. Suppose $R$ is a RE. There are four cases to consider.
>
> 1. $R = R_{1} + R_{2}$. Then $L(R)$ is empty $\iff$ $L(R_{1})$ is empty **and** $L(R_{2})$ is empty
> 2. $R = R_{1}R_{2}$. Then $L(R)$ is empty $\iff$ $L(R_{1})$ is empty **or** $L(R_{2})$ is empty
> 3. $R = R_{1}^{*}$. Then $L(R)$ is not empty, it always includes at least $\epsilon$
> 4. $R = (R_{1})$. Then $L(R)$ is empty $\iff$ $L(R_{1})$ is empty

#### The infiniteness problem

Problem: Is a given language infinite?

Key Idea: if the DFA has $n$ states, and the language contains ant string of length $n$ or more, then the language is infinite.

> Suppose that $L$ is a regular language accepted by a DFA with $n$ states. Then $L$ is infinite $\iff$ $L$ contains a word whose length is at least $n$.
>
> $\Leftarrow$: 如果一个有 $n$ 个状态的 DFA 接受一个长度至少为 $n$ 的字符串 $w$，则在其路径上至少有一个状态出现两次（PHP）。设其路径为
> $$
> s_{1}s_{2}\dots s_{i}\dots s_{i}\dots s_{n}
> $$
> 设从 $s_{1}$ 到第一个 $s_{i}$ 的标号组成串 $x$ ，从第一个 $s_{i}$ 到第二个 $s_{i}$ 的标号组成串 $y$ ，从第二个 $s_{i}$ 到 $s_{n}$ 组成字符串 $z$ ，则该 DFA 可接受所有形如 $xy^{i}z(i\geqslant 0)$ 的字符串 (i. e. pumping lemma)
>
> $\Rightarrow$: trivial

However, there are an infinite number of strings of length $> n$ , and we can't test them all

Key Idea: if there is a string of length $\geqslant n$ in $L$ , then there is a string of length between $n$ and $2n-1$

> Suppose that $L$ is a regular language accepted by a DFA with $n$ states. Then $L$ is infinite $\iff$ $L$ contains a word whose length is between $n$ and $2n-1$.
>
> $\Rightarrow$: 因为 $L$ 是 infinite，其包含一个 string 长度至少为 $n$ ，设 $w$ 为 $L$ 包含的长度至少为 $n$ 的 string 中最短的
> $$
> w = w_{1}w_{2}\dots w_{N}
> $$
> 设 DFA 接受其的状态顺序为 $a_{0}a_{1}\dots a_{N}$ ，根据 PHP ，其中必有一个状态至少出现两次，设其为 $a_{i}$ ，且 $a_i = a_{j}(i < j)$ ，故 $z = w_{1}w_{2}\dots w_{i}w_{j+1}\dots w_{N}$ 也属于 $L$ 。根据 $w$ 的定义，有 $|z| < n$ ，又 $|w| = z + j - i$ 且 $j - i \leqslant n$ ，故 $|w| < 2n$ 。根据其定义 $|w| \geqslant n$ ，故可得
> $$
> n \leqslant |w| \leqslant 2n-1
> $$
> $\Leftarrow$: 同上（pumping lemma）

根据以上两个 key idea，检查所有长度在 $n$ 到 $2n-1$ 之间的串即可

然而在实际中这样的算法代价也是不可接受的。所以一般是通过检查 DFA 对应的图中是否有环来判断语言是否 infinite。具体而言分为以下几步

1. Eliminate states not reachable from the start state
2. Eliminate states that do not reach a final state
3. Test if the remaining transition graph has any cycles

#### The equivalence problem

Problem: Given regular languages $L$ and $M$, is $L = M$

Algorithm: Constructing the **product DFA** from DFA for $L, M$

设 $L$ 与 $M$ 的 DFA 有状态集合 $Q$ 与 $R$ ，则 product DFA 有状态集合 $Q \times R$

对于 product DFA 而言

* start state: $[q_{0}, r_{0}]$
* transition: $\delta([q, r], a) = [\delta_{L}(q, a), \delta_{M}(r, a)]$
* final states: states $[q, r]$ that exactly one of $q$ and $r$ is a final state of its own DFA

由于 product DFA 的 accept state 是两个状态中有且仅有一个是原本的 accept state，则如果一个 string $w$ 被 product DFA 接受，说明其被一个 DFA 接受而不被另一个 DFA 接受

$L = M \iff$ the product DFA's language is empty

#### The containment problem

Problem: Given regular languages $L$ and $M$ , is $L \subseteq M$

Algorithm: use the product DFA

final state: states $[q, r]$ that $q$ is the final state, $r$ is not

$L \subseteq M \iff$ the product DFA's language is empty

### The Minimum-State DFA for a Regular Language

#### Equivalence of states

Given a DFA $A$, find the DFA with the fewest states accepting $L(A)$ (equivalence)

> Equivalence of states: states $p$ and $q$ are *equivalent* if
>
> For all input strings $w$ , $\delta(p, w)$ is an accepting state $\iff$ $\delta(q, w)$ is an accepting state
>
> If two states are not equivalent, then we say they are *distinguishable*. That
> is, state $p$ is distinguishable from state $q$ if there is at least one string $w$ such
> that one of $\delta(p, w)$ and  $\delta(q, w)$ is accepting, and the other is not accepting.

Algorithm: table-filling algorithm

* Construct a table with all pairs of states
* If you find a string that **distinguishes** two states (takes exactly one to an accepting state), mark that pair
* Algorithm is a **recursion** on the length of the shortest distinguishing string

> Basis. If $p$ is an accepting state and $q$ is non-accepting, then the pair $[p, q]$ is distinguishable
>
> Induction. Let $p$ and $q$ be states such that for some input symbol $a$, $r = \delta(p, a)$ and $s = \delta(q, a)$ are a pair of states known to be distinguishable. Then $[p, q]$ is a pair of distinguishable states.

在算法结束后，所有未被标记的 pair 是等价的状态

> If two states are not distinguished by the table-filling algorithm, then the states are equivalent.
>
> Proof. 假设命题错误，故存在至少一对状态 $p, q$ 满足
>
> * $p, q$ is distinguishable.
> * the algorithm does not find $p$ and $q$ to be distinguishable
>
> 令这样的状态对为 bad pair。则对于所有 bad pairs，都存在一个 string 来区分两个状态。令其中 string 最短的 pair 为 $[p, q]$ ，区分其的最短 string 为 $w = a_{1}a_{2}\dots a_{n}$
>
> 显然 $w \neq \epsilon$ ，否则在 Basis 阶段就被区分，即 $n \geqslant 1$。考虑 $r = \delta(p, a_{1}), s = \delta(q, a_{1})$ ，显然，$a_{2}a_{3}\dots a_{n}$ 区分 $[r, s]$ ，但是 $a_{2}a_{3}\dots a_{n}$ 比任何能区分 bad pair 的 string 都短，故 $[r, s]$ 不是 bad pair，算法将其标记为 distinguishable。于是根据 Induction 的部分，算法发现 $[p, q]$ 是 distinguishable，因为 $r = \delta(p, a_{1}), s = \delta(q, a_{1})$ 是 distinguishable。矛盾。故原命题正确

> 对于 Equivalence problem，也可以通过这个算法解决。若判断两个 regular languages $L, M$ 是否等价，可以将其状态合并，即 $Q \cup R$ ，然后对其应用 table-filling algorithm
>
> $L = M \iff$ 两个 DFA 的开始状态 $q_{0}, r_{0}$ 等价

#### Minimize DFA

要最小化一个 DFA ，首先要合并所有不可区分的状态

状态的合并可按照如下步骤

* 假设 $q_{1}, q_{2}, \dots q_{k}$ 是不可区分的
* 将其用一个代表状态 $q$ 代替
* 显然 $\delta(q_{1}, a), \delta(q_{2}, a), \dots \delta(q_{k}, a)$ 也是不可区分的（否则其中必有至少一对被算法标记为 distinguishable）
* 令 $\delta(q, a)$ 为 $\{p: p = \delta(q_{i}, a), i = 1, 2, \dots k \}$ 的代表元素

合并之后，还要去掉所有从开始状态不可达的状态

事实上，状态的等价是一种等价关系，所以所有等价的状态将状态集划分为多个不相交的等价类

> The equivalence of states is transitive
>
> Proof. 假设 $[p, q]$ 与 $[q. r]$ 是等价的，但 $[p, r]$ 不等价。根据定义，存在一个输入 string $w$ 满足 $\delta(p, w)$ 与 $\delta(r, w)$ 中有且仅有一个是接收状态
>
> w. l. o. g. $\delta(p, w)$ 是接收状态。考虑 $\delta(q, w)$ ，若其为接收状态，$[q, r]$ 为 distinguishable，若其为非接受状态，$[p, q]$ 为 distinguishable。均与假设矛盾

故最小化 DFA 即为

* 消去所有从开始不可达的状态
* 将状态根据等价关系（由 table-filling algorithm 得到）划分为等价类
* 将含有不止一个状态的等价类合并为一个代表状态
* 合并状态转移

包含开始状态的等价类为新 DFA 的开始状态，包含接受状态的等价类为新 DFA 的接收状态

#### Minimized DFA can't be beaten

> If $A$ is a DFA, and $M$ the DFA constructed from $A$ by the algorithm of minimizing DFA, then $M$ has as few states as any DFA equivalent to $A$

事实上，对于一个 DFA $A$ ，其所有最小的 DFA 都是同构的

> Proof. 假设 $A$ 是一个 DFA，最小化其得到 DFA $M$，假设存在一个 DFA $N$ 与 $A, M$ 接受一样的 language，但有更少的状态。考虑 $M,N$ 组合的 DFA，首先
>
> * $M, N$ 的开始状态是等价的，因为 $L(M) =L(N)$
> * 若状态 $[p, q]$ 等价，则 $[\delta(p, a), \delta(q, a)]$ 等价
>
> > 对于每个 $M$ 中的状态 $q$ ， 其与 $N$ 中至少一个状态等价：
> >
> > Proof: by induction
> >
> > Basis. 如果 $q$ 是 $M$ 的开始状态，其与 $N$ 的开始状态等价
> >
> > 假设从 $M$ 的开始状态到达 $q$ 的最短路径长度为 $k$
> >
> > I. H. 若从 $M$ 的开始状态到达 $q$ 的最短路径长度短于 $k$ ，则存在一个 $N$ 中的状态与其等价
> >
> > Induction. 假设从 $M$ 的开始状态到 $q$ 的最短路径的 string 为 $w = x a$ ，长为 $k$。假设从 $M$ 开始状态出发沿 $x$ 到达 $r$ ，从 $N$ 开始状态出发沿 $x$ 到达 $p$ ，根据 I. H. ，$[p, r]$ 等价。故 $[\delta_{M}(r, a), \delta_{N}(p, a)]$ 等价
>
> 由于根据前提，$N$ 状态数少于 $M$，故至少有两个 $M$ 中的状态与 $N$ 中的同一个状态等价。因此这两个状态等价，这与 $M$ 中所有状态都不等价矛盾，故前提错误，不存在这样的 $N$

