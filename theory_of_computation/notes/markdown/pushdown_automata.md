# Pushdown Automata

## Definition

Informal: PDA is a $\epsilon$-NFA with a stack

Formal: A PDA is a 7-tuple
$$
P  = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)
$$
where

* $Q$ : a finite set of states
* $\Sigma$ : a finite set of input symbols
* $\Gamma$ : a finite stack alphabet
* $\delta$ : the transition function
* $q_{0}$ : the start state
* $Z_{0}$ : the start symbol in stack
* $F$ : the set of accepting states

考虑 PDA 的迁移函数 $\delta$ ，其接受三个参数 $(q, a, X)$ ，其中

1. $q$ 是 $Q$ 中的状态
2. $a$ 是 $\Sigma$ 中的符号或是 $\epsilon$
3. $X$ 是 $\Gamma$ 中的符号

其输出为有序对 $(p, \gamma)$ 的集合，其中 $p$ 是一个新状态，而 $\gamma$ 是一个 stack symbol 的 string，用于**取代** $X$ ，当 $\gamma = \epsilon$ ，表示弹出 $X$ ，而当 $\gamma = X$ 则不变，若 $\gamma = Y Z$ ，则将 $X$ 替换为 $Z$，再将 $Y$ 压入。

> 需注意 $\delta$ 的输出是一个集合，即 PDA 可以从中选出一个对，但是不能迁移到某个对的状态但是将栈中内容替换为另一个对的内容

PDA 也可以像 FA 一样使用图表示，其中

* 节点代表 PDA 的 states
* 两个圈的节点表示接收状态
* 一条标号为 $a, X/ \alpha$ 的从 $q$ 到 $p$ 的边表示 $(p, \alpha) \in \delta(q, a, X)$

## Instantaneous Descriptions

不同于 FA，描述状态机的运行的只有状态，PDA 的运行包括了状态与栈的内容，故定义 Instantaneous Description 为一个 3-tuple $(q, w, \gamma)$

* $q$ 是一个状态
* $w$ 是余下的输入
* $\gamma$ 是栈的内容

PDA 的 ID 可以完全表示其运行时某一个时刻的格局。

为了描述 ID 随着 PDA 的运行而发生的转换，定义 $\vdash$ 。若 $\delta(q, a, X)$ 包含 $(p, \alpha)$ ，则对于任意 $w \in \Sigma^{*}, \beta \in  \Gamma^{*}$ 有
$$
(q, aw, X\beta) \vdash (p, w, \alpha\beta)
$$
显然，余下的输入和栈中剩余的部分不影响 ID 的转换

$\vdash$ 表示 PDA 的一步动作，可以定义 $\vdash^{*}$ 表示 0 步或多步动作

Basis. $I \vdash^{*} I$ for any ID $I$

Induction. If $I \vdash^{*} K, K \vdash J$ , then $I \vdash^{*} J$

对于 ID 的 transition，有

If $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ is a PDA, and $(q, x, \alpha) \vdash^{*} (p, y, \beta)$ , then for any strings $w \in \Sigma^{*}$ and $\gamma \in \Gamma^{*}$, it is also true that
$$
(q, xw, \alpha \gamma) \vdash^{*} (p, yw, \beta \gamma)
$$

> Proof. 对 ID 的转换步数归纳。由于 PDA 未读入的输入不会影响其行为，故在输入后添加后缀 $w$ 不会改变其行为。同样的，在原本的转换中，没有用到 $\alpha$ 以外的内容，故在栈底加入 $\gamma$ 也不会改变其行为

同样的，有

If $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ is a PDA, and
$$
(q, xw, \alpha) \vdash^{*} (p, yw, \beta)
$$
then $(q, x, \alpha) \vdash^{*} (p, y, \beta)$

需要注意的是未读入的输入不会对 PDA 产生影响，故可以将其共同的后缀去除，但是不能将栈共同的后缀去除，考虑转换前栈中为 $\alpha \gamma$ ，转换后为 $\beta \gamma$ ，在转换的过程中可能弹出了 $\gamma$ 中的符号，然后之后又将其压入，若将 $\gamma$ 去除则转换不能成立

> 添加或删除输入串的后缀不影响转换，但只能添加栈底内容而不能删除

## The Language of a PDA

有两种方式可以让一个 PDA 接受输入

* acceptance by final state: 当输入结束时，PDA 状态停止在接收状态
* acceptance by empty stack: 当输入结束时，PDA 栈空

可以得出这两种方式是等价的，即给定一个语言 $L$ ，存在一个 PDA 以 acceptance by final state 的方式定义 $L$ ，也存在一个 PDA 以 acceptance by empty stack 的方式定义 $L$ 。但对于同一个 PDA 而言，以两种方式定义的语言一般是不同的

### Acceptance by Final State

