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

> 需注意 $\delta$ 的输出是一个集合，即 PDA 可以从中选出一个对，但是不能迁移到某个对的状态但是将栈中内容替换为另一个对的内容

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

Induction. If $I \vdash^{*} K, K \vdash J$ , then $I \vdash^{*} J$

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

设 PDA $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ ，则 language accepted by $P$ by final state 定义为
$$
L(P) = \{w : (q_{0}, w, Z_{0}) \vdash^{*} (q, \epsilon, \alpha) \}, q \in F
$$
即在输入结束后，PDA 到达接收状态，而此时栈中可以是任意内容

### Acceptance by Empty Stack

设 PDA $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ ，则 language accepted by $P$ by empty stack 定义为
$$
N(P) = \{w : (q_{0}, w, Z_{0}) \vdash^{*} (q, \epsilon, \epsilon) \}
$$
即输入结束后栈清空则视为接受，PDA 此时可以处于任意状态

### From Empty Stack to Final State

事实上，$L(P), N(P)$ 定义的语言集合是相同的，即 CFL。

If $L = N(P_{N})$ for some PDA $P_{N} = (Q, \Sigma, \Gamma, \delta_{N}, q_{0}, Z_{0}, F)$ , then there is a PDA $P_{F}$ such that $L = L(P_{F})$

> Proof.
>
> 引入一个新的符号 $X_{0} \notin \Gamma$ ，$X_{0}$ 是 $P_{F}$ 的开始符号，其思想在于当 $P_{F}$ 栈中仅有 $X_{0}$ 时，可以得知对于相同的输入，$P_{N}$ 会清空其栈，即接受该输入。
>
> 同样需要引入一个新的开始符号 $p_{0}$ ，用于将 $Z_{0}$ 压入栈中，在此之后 $P_{F}$ 将模拟 $P_{N}$ 的运行，直至栈顶为 $X_{0}$ ，此时代表 $P_{N}$ 对于同样的输入清空了栈，即接受该输入。引入一个新的状态 $p_{f}$ 用于在栈顶为 $X_{0}$ 且输入结束时转移到该状态。$p_{f}$ 是 $P_{F}$ 的唯一接受状态
>
> $P_{F}$ 的精确定义为
> $$
> P_{F} = (Q \cup \{p_{0}, p_{f} \}, \Sigma, \Gamma \cup \{X_{0} \}, \delta_{F}, p_{0}, X_{0}, \{p_{f}\})
> $$
> 其中 $\delta_{F}$ 的定义为
>
> * $\delta_{F}(p_{0}, \epsilon, X_{0}) = \{(q_{0}, Z_{0}X_{0}) \}$ ，即开始时 $P_{F}$ 将 $Z_{0}$ 压入栈中，同时转移到 $P_{N}$ 的开始状态
> * 对于所有 $q \in Q, a \in \Sigma, a = \epsilon, Y \in \Gamma$ ，有 $\delta_{N}(q, a, Y) \subseteq \delta_{F}(q, a, Y)$ ，即 $P_{F}$ 模拟 $P_{N}$ 的运行
> * 对于所有 $q \in Q$ ，有 $(p_{f},\epsilon) \in \delta_{F}(q, \epsilon, X_{0})$
>
> 只需证明
> $$
> w \in L(P_{F}) \iff w \in N(P_{N})
> $$
> ($\Leftarrow$): 已知 $(q_{0}, w, Z_{0}) \underset{P_{N}}{\vdash ^{*}} (q, \epsilon, \epsilon)$ ，则可以在栈底插入符号 $X_{0}$ ，即
> $$
> (q_{0}, w, Z_{0}X_{0}) \underset{P_{N}}{\vdash ^{*}} (q, \epsilon, X_{0})
> $$
> 而由于 $P_{F}$ 模拟了所有 $P_{N}$ 的运行，故有
> $$
> (q_{0}, w, Z_{0}X_{0}) \underset{P_{F}}{\vdash ^{*}} (q, \epsilon,  X_{0})
> $$
> 根据 $\delta_{F}$ 有
> $$
> (p_{0}, w, X_{0}) \underset{P_{F}}{\vdash} (q_{0}, w, Z_{0}X_{0}) \underset{P_{F}}{\vdash ^{*}} (q, \epsilon,  X_{0}) \underset{P_{F}}{\vdash} (p_{f}, \epsilon, \epsilon)
> $$
> 即 $(p_{0}, w, X_{0}) \underset{P_{F}}{\vdash^{*}} (p_{f}, \epsilon, \epsilon)$ ，可得 $w \in L(P_{F})$
>
> ($\Rightarrow$): 显然，对于 $P_{F}$ ，其第一步转换必然是 $(p_{0}, \epsilon, X_{0}) \vdash (q_{0}, Z_{0}X_{0})$ ，因为这是开始状态唯一的转换函数，且若其接受 string，其最后一步转换必然是 $(q, \epsilon, X_{0}) \vdash (p_{f}, \epsilon)$ ，因为 $p_{f}$ 是唯一的接受状态，且所有输出包含 $p_{f}$ 的转换函数其输入都要求栈中仅有 $X_{0}$ ，而显然 $X_{0}$ 仅会出现在栈底
>
> 这样任意接受 $w$ 的转换都有如下形式
> $$
> (p_{0}, w, X_{0}) \underset{P_{F}}{\vdash} (q_{0}, w, Z_{0}X_{0}) \underset{P_{F}}{\vdash ^{*}} (q, \epsilon, X_{0}) \underset{P_{F}}{\vdash} (p_{f}, \epsilon, \epsilon)
> $$
> 且除去开始的一步和结尾的一步，中间的转换都是 $P_{N}$ 的转换，且转换过程中 $X_{0}$ 都在栈的底部（$X_{0}$ 若出现在栈顶则下一步运行就会结束）。故可将 $X_{0}$ 去掉，得到
> $$
> (q_{0}, w, Z_{0}) \underset{P_{N}}{\vdash ^{*}} (q, \epsilon, \epsilon)
> $$
>  即 $w \in N(P_{N})$

### From Final State to Empty State

If $L = L(P_{F})$ for some PDA $P_{F} = (Q, \Sigma, \Gamma, \delta_{F}, q_{0}, Z_{0}, F)$ , then there is a PDA $P_{N}$ such that $L = N(P_{N})$

> Proof. 基本思想同样是用 $P_{N}$ 去模拟 $P_{F}$ 的运行，每当 $P_{F}$ 接受输入，$P_{N}$ 便将栈清空，接受同样的输入。
>
> 为了防止在 $P_{F}$ 运行过程中还未接受就将栈清空使得 $P_{N}$ 提前接受，引入新的符号 $X_{0} \notin \Gamma$ ，在开始时压入栈，这样无论如何模拟 $P_{F}$ 的运行都不会清空栈，直至其到达接受状态，再将栈中的剩余符号连同 $X_{0}$ 一起弹出
>
> $P_{N}$ 的精确定义为
> $$
> P_{N} = (Q \cup \{p_{0}, p \}, \Sigma, \Gamma \cup \{X_{0} \}, \delta_{N}, p_{0}, F)
> $$
> 其中 $\delta_{N}$ 的定义为
>
> * $\delta_{N}(p_{0}, \epsilon, X_{0}) = \{(q_{0}, Z_{0}X_{0})\}$ ，开始时 $P_{N}$ 将 $Z_{0}$ 压入栈中，转到 $P_{F}$ 的开始状态
> * 对于所有 $q \in Q, a \in \Sigma, a = \epsilon, Y \in \Gamma$ ，有 $\delta_{F}(q, a, Y) \subseteq \delta_{N}(q, a, Y)$ ，即 $P_{N}$ 模拟 $P_{F}$ 的运行
> * 对于所有 $q \in F, Y \in \Gamma, Y = X_{0}$ 有 $(p, \epsilon) \in \delta_{N}(q, \epsilon, Y)$ ，即当 $P_{F}$ 接受输入时，$P_{N}$ 开始将自己的栈清空，不再消耗输入
> * 对于所有的 $Y \in \Gamma, Y = X_{0}$ 有 $\delta_{N}(p, \epsilon, Y) = \{(p, \epsilon)\}$ ，即当进入状态 $p$ 后，$P_{N}$ 将栈中所有的符号弹出直至栈为空，然后接受该输入
>
> 只需证明
> $$
> w \in N(P_{N}) \iff w \in L(P_{F})
> $$
> ($\Leftarrow$): 已知 $(q_{0}, w, Z_{0}) \underset{P_{F}}{\vdash^{*}}(q, \epsilon, \alpha), q \in F$ ，显然每一步 $P_{F}$ 的转换都是 $P_{N}$ 的转换，且可以将 $X_{0}$ 插入栈底，故有
> $$
> (q_{0}, w, Z_{0}X_{0}) \underset{P_{N}}{\vdash^{*}}(q, \epsilon, \alpha X_{0})
> $$
> 则根据 $\delta_{N}$ 的定义有
> $$
> (p_{0}, w, X_{0}) \underset{P_{N}}{\vdash} (q_{0}, w, Z_{0}X_{0}) \underset{P_{N}}{\vdash^{*}}(q, \epsilon, \alpha X_{0}) \underset{P_{N}}{\vdash^{*}} (p, \epsilon, \epsilon)
> $$
> 于是有 $w \in N(P_{N})$
>
> ($\Rightarrow$): 考虑 $P_{N}$ 清空其栈的唯一条件是进入状态 $p$ ，因为 $X_{0}$ 在栈底，且 $P_{F}$ 的栈符号集 $\Gamma$ 中没有 $X_{0}$ 。而 $P_{N}$ 进入状态 $p$ 的条件是 $P_{F}$ 达到某个接受状态 $q$ ，而根据 $\delta_{N}$ 的定义，$P_{N}$ 的第一个动作一定是 $(p_{0}, w, X_{0}) \vdash (q_{0}, w, Z_{0}X_{0})$ 
>
> 故任意接受 $w$ 的转换都有如下的形式
> $$
> (p_{0}, w, X_{0}) \underset{P_{N}}{\vdash} (q_{0}, w, Z_{0}X_{0}) \underset{P_{N}}{\vdash^{*}}(q, \epsilon, \alpha X_{0}) \underset{P_{N}}{\vdash^{*}} (p, \epsilon, \epsilon)
> $$
> 而所有 $(q_{0}, w, Z_{0}X_{0}) \underset{P_{N}}{\vdash^{*}}(q, \epsilon, \alpha X_{0}) $ 之间的转换都是 $P_{F}$ 的转换，故 $P_{F}$ 也可以有同样的转换，且栈中没有符号 $X_{0}$ （因为 $X_{0}$ 在栈底且不会被 $P_{F}$ 的转换影响），即
> $$
> (q_{0}, w, Z_{0}) \underset{P_{F}}{\vdash^{*}}(q, \epsilon, \alpha), q \in F
> $$
> 即 $w \in L(P_{F})$

## Equivalence of PDA and CFG

正如 CFG 一样，PDA 定义的语言正好是 CFL（无论是 acceptance by empty stack 还是 acceptance by final state），这说明 PDA 和 CFG 表达能力是等价的

### From Grammars to Pushdown Automata

基本思路为，给出一个 CFG，可以构造一个 PDA 模拟其最左推导过程。而最左推导的每一步是由最左句型来完全表示的。

任何非 terminal string 的最左句型都可以写为 $xA\alpha$ ，其中 $A$ 是最左的 variable。称 $A\alpha$ 为句型的 **tail** ，对于一个仅包含 terminal 的最左句型，其 tail 为 $\epsilon$

使用 PDA 模拟最左推导的思路在于令最左句型 $xA\alpha$ 的 tail $A \alpha$ 出现在栈中，而 $x$ 是已经消耗的输入，考虑输入字符串 $w = xy$ ，$y$ 为剩余的输入，则 PDA 的 ID  $(q, y, A\alpha)$ 可以代表最左句型 $xA\alpha$ 。假设下一步用于展开 $A$ 的产生式为 $A \to \beta$ ，则 PDA 的动作是用 $\beta$ 替换栈顶的 $A$ ，ID 转换为 $(q, y, \beta \alpha)$ ，该 PDA 中只有一个状态 $q$ ，而现在的 ID 可能不能代表一个最左句型，因为 $\beta$ 可能有 terminal 作为前缀，因此需要消耗输入，同时从栈中移除对应的 terminal，直至有一个 variable 出现在了栈顶

若最终成功模拟了最左推导，则所有的 variable 都被展开，所有的 terminal 都与输入中的 symbol 匹配，最终栈为空，接受该输入

令 $G = (V, T, P, S)$ 为 CFG ，则可以构造 PDA $P$ ，有 $L(G) = N(P)$
$$
P = (\{q\}, T, V\cup T, \delta, q, S, F)
$$

其中 $\delta$ 的定义为

* 对于每个 variable $A$ 
  $$
  \delta(q, \epsilon, A) = \{(q, \beta) : A \to \beta \in P\}
  $$

* 对于每个 terminal $a$
  $$
  \delta(q, a, a) = \{(q, \epsilon)\}
  $$

按照上述方法构造出的 PDA $P$ ，有 $L(G) = N(P)$

> Proof.
> $$
> w \in N(P) \iff w \in L(G)
> $$
> ($\Leftarrow$): 如果 $w \in L(G)$ ，则存在一个最左推导序列
> $$
> S = \gamma_{1} \underset{\text{lm}}{\Rightarrow} \gamma_{2} \underset{\text{lm}}{\Rightarrow} \dots \underset{\text{lm}}{\Rightarrow} \gamma_{n} = w 
> $$
> 则有 $(q, w, S) \underset{P}{\vdash^{*}} (q, y_{i}, \alpha_{i})$ ，其中 $(q, y_{i}, \alpha_{i})$ 代表了最左句型 $\gamma_{i}$ （$\gamma_{i} = x_{i}\alpha_{i}, w = x_{i}y_{i}$），其证明基于对 $i$ 的归纳
>
> Basis. 当  $i = 1$ 时，有 $\gamma_{1} = S, x_{1} = \epsilon, y_{1} = w$ ，显然有 $(q, w, S) \vdash^{*} (q, w, S)$
>
> Induction. 假设 $(q, w, S) \vdash^{*} (q, y_{i}, \alpha_{i})$ ，由于 $\alpha_{i}$ 是 tail，其第一个 symbol 是某个 variable $A$ ，在最左推导 $\gamma_{i} \Rightarrow \gamma_{i+1}$ 中，使用 $A$ 的一个产生式 $A \to \beta$ 将其展开，而根据 PDA 的构造过程，可以使用 $\beta$ 替代栈顶的 $A$ ，然后利用输入中的 terminal 将栈中的 terminal 弹出，直到栈顶为下一个 variable，达到 $(q, y_{i+1}, \alpha_{i+1})$ ，即 $(q, w, S) \vdash^{*} (q, y_{i+1}, \alpha_{i+1})$
>
> 当 $i = n$ 时，$\alpha_{n} = \epsilon$ ，于是有 $(q, w, S) \vdash^{*} (q, \epsilon, \epsilon)$ ，$P$ 接受 $w$
>
> ($\Rightarrow$): 需要证明：当 $P$ 进行一系列操作后，将栈顶的 variable $A$ 弹出，同时没有涉及到 $A$ 以下的栈内容（称其**净效应**为弹出 $A$），则 $A$ 可以推导出在此过程中消耗的所有输入，即
> $$
> (q, x, A) \underset{P}{\vdash^{*}}(q, \epsilon, \epsilon) \Rightarrow A \underset{G}{\overset{*}{\Rightarrow}} x
> $$
> 证明将基于 $P$ 操作的步数
>
> Basis. 只有一步操作，则唯一的可能是 $A \to \epsilon \in P$ ，则根据 $\delta$ 的定义，有 $(q, \epsilon, A) \vdash (q, \epsilon, \epsilon)$ ，即 $x = \epsilon$ ，显然 $A \Rightarrow x$
>
> Induction. 考虑 $P$ 操作了 $n$ 步，则第一步一定是用 $A$ 的某个产生式体替换了栈顶的 $A$ ，假设用来替换的产生式是 $A \to Y_{1}Y_{2}\dots Y_{k}$
>
> 则接下来的 $n-1$ 步一定是从输入中消耗了 $x$ ，并且其净效应为逐个弹出 $Y_{1}, Y_{2} \dots$ ，则可以将 $x$ 分为 $x_{1}x_{2}\dots x_{k}$ ，其中 $x_{i}$ 代表了从弹出 $Y_{i-1}$ 到弹出 $Y_{i}$ 之间消耗的输入（即栈顶从 $Y_{i}$ 变为 $Y_{i+1}$） ，则对于所有 $i$ 有
> $$
> (q, x_{i}x_{i+1}\dots x_{k}, Y_{i}) \vdash^{*} (q, x_{i+1}\dots x_{k}, \epsilon)
> $$
> 由于这其中操作步数都不会超过 $n-1$ ，根据 I. H. 有 $Y_{i} \overset{*}{\Rightarrow} x_{i}$
>
> 于是有推导
> $$
> A \Rightarrow Y_{1}Y_{2}\dots Y_{k} \overset{*}{\Rightarrow} x_{1}Y_{2}\dots Y_{k} \overset{*}{\Rightarrow} \dots \overset{*}{\Rightarrow} x_{1}x_{2}\dots x_{k} = x
> $$
> 即 $A \overset{*}{\Rightarrow} x$
>
> 令 $A = S, x = w$ ，由于 $w \in N(P)$ ，有 $(q, w, S) \vdash^{*} (q, \epsilon, \epsilon)$ ，则根据上述结论，有 $S \overset{*}{\Rightarrow} w$ ，即 $w \in L(G)$

### From PDA to Grammars

对任意 PDA $P$ 都存在一个 CFG $G$ 使得 $L(G) = N(P)$

基本思想是文法中的 variable 代表了 PDA 运行中的一个 event，即 variable $[pXq]$ 代表了

* 净效应为从栈中弹出 $X$ ，即弹出 $X$ 的过程不涉及 $X$ 以下的栈内容
* 当 $X$ 从栈中被弹出的同时，状态也从开始的 $p$ 转换到了 $q$

而这个 variable 产生的 string 即是在 event 中被消耗的输入

更为详细的构造为，令 $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0} ,F)$ 为 PDA ，则构造
$$
G = (V, \Sigma, R, S)
$$
其中 $V$ 包含

* 特殊的开始符号 $S$
* 其余符号都形如 $[pXq], p, q \in Q, X \in \Gamma$

对于 $G$ 中的产生式

* 对所有状态 $p$ ，$G$ 中有产生式 $S \to [q_{0}Z_{0}p]$ ，即 $[q_{0}Z_{0}p]$ 产生的 string $w$ 可以将 $Z_{0}$ 从栈中弹出，同时状态转移到 $p$ ，即 $(q_{0}, w, Z_{0}) \vdash^{*} (p, \epsilon, \epsilon)$ 。即 $S$ 将产生所有能让 PDA 清空其栈的 string

* 若 $(r, Y_{1}Y_{2} \dots Y_{k}) \in \delta(q, a, X)$ ，其中 $a \in \Sigma \text { or } a = \epsilon, k = 0, 1, \dots$ ，则对于任意状态 $r_{1}, r_{2}, \dots r_{k}$ ，有产生式
  $$
  [qXr_{k}] \to a[rY_{1}r_{1}][r_{1}Y_{2}r_{2}]\dots [r_{k-1}Y_{k}r_{k}]
  $$
  即从栈中弹出 $X$ 的方法可以是读入 $a$ 后逐个弹出 $Y_{1}, Y_{2} ,\dots Y_{k}$ ，而期间的状态转换可以是任意状态。若 $k = 0$ ，则为 $[qXr] \to a$

可以证明 $[qXp] \overset{*}{\Rightarrow} w \iff (q, w, X) \vdash^{*}(p, \epsilon, \epsilon)$

> Proof.
>
> ($\Leftarrow$): 已知 $(q, w, X) \vdash^{*} (p, \epsilon, \epsilon)$ ，则基于 PDA 的行动数归纳
>
> Basis. 行动一步，则 $(p, \epsilon) \in \delta(q, w, X)$ ，而 $w$ 为一个 symbol 或是 $\epsilon$ 。根据上述产生式的构造规则，有 $[qXp] \to w$ ，故 $[qXp] \Rightarrow w$
>
> Induction. 考虑操作了 $n$ 步，则其形式类似
> $$
> (q, w, X) \vdash (r_{0}, x, Y_{1}Y_{2}\dots Y_{k}) \vdash^{*} (p, \epsilon, \epsilon)
> $$
>  其中 $w = ax, a \in \Sigma \text{ or } a = \epsilon$
>
> 故 $(r, Y_{1}Y_{2} \dots Y_{k}) \in \delta(q, a, X)$ ，根据产生式构造规则，有
> $$
> [qXr_{k}] \to a[r_{0}Y_{1}r_{1}][r_{1}Y_{2}r_{2}]\dots [r_{k-1}Y_{k}r_{k}]
> $$
> 其中 $r_{k} = p$ 而其余 $r_{1}, r_{2} ,\dots ,r_{k-1}$ 可以为任意状态
>
> 对任意 $i$ ，$r_{i}$ 是在 $Y_{i}$ 被弹出时转换到的状态，可以令 $x = w_{1}w_{2} \dots w_{k}$ ，其中 $w_{i}$ 为从 $Y_{i-1}$ 弹出到 $Y_{i}$ 弹出期间消耗的输入，则有 $(r_{i-1}, w_{i}, Y_{i}) \vdash^{*} (r_{i}, \epsilon, \epsilon)$ 。由于这些转换都不可能有 $n$ 步，则根据 I. H. 有 $[r_{i-1}Yr_{i}] \overset{*}{\Rightarrow} w_{i}$
>
> 故有
> $$
> \begin{array}{l}{\left[q X r_{k}\right] \Rightarrow a\left[r_{0} Y_{1} r_{1}\right]\left[r_{1} Y_{1} r_{2}\right] \cdots\left[r_{k-1} Y_{k} r_{k}\right] \stackrel{*}{\Rightarrow}} \\ {a w_{1}\left[r_{1} Y_{2} r_{2}\right]\left[r_{2} Y_{3} r_{3}\right] \cdots\left[r_{k-1} Y_{k} r_{k}\right] \Rightarrow} \\ {a w_{1} w_{2}\left[r_{2} Y_{3} r_{3}\right] \cdots\left[r_{k-1} Y_{k} r_{k}\right] \Rightarrow} \\ {\cdots} \\ {a w_{1} u_{2} \cdots w_{k}=w}\end{array}
> $$
> ($\Rightarrow$): 证明基于对推导步数的归纳
>
> Basis. 仅有一步推导，则一定有产生式 $[qXp] \to w$ ，而根据构造规则，能产生这样的产生式一定说明 $(p, \epsilon) \in \delta(q, a, X)$ ，其中 $a = w$ ，则有 $(q, w, X) \vdash^{*}(p, \epsilon, \epsilon)$
>
> Induction. 考虑 $[qXp] \overset{*}{\Rightarrow} w$ 推导用了 $n$ 步，则其形式形如
> $$
> [qXr_{k}] \Rightarrow a[r_{0}Y_{1}r_{1}][r_{1}Y_{2}r_{2}]\dots [r_{k-1}Y_{k}r_{k}]\overset{*}{\Rightarrow} w
> $$
> 其中 $r_{k} = p$ ，而产生这样的产生式，根据构造规则，一定说明 $(r_{0}, Y_{1}Y_{2}\dots Y_{k}) \in \delta(q, a, X)$
>
> 则可以将 $w$ 写作 $aw_{1}w_{2} \dots w_{k}$ ，满足 $[r_{i-1}Yr_{i}] \overset{*}{\Rightarrow} w_{i}$ ，由于这些推导步数都不会超过 $n$ 步，则根据 I. H. 有
> $$
> (r_{i-1}, w_{i}, Y_{i}) \vdash^{*} (r_{i}, \epsilon, \epsilon)
> $$
> 由于可以在输入后和栈底添上任意符号串，即
> $$
> (r_{i-1}, w_{i}w_{i+1}\dots w_{k} , Y_{i}Y_{i+1} \dots Y_{k}) \vdash^{*} (r_{i}, w_{i+1}\dots w_{k}, Y_{i+1} \dots Y_{k})
> $$
> 即可得
> $$
> \begin{align}
> (q, aw_{1}w_{2}\dots w_{k}, X) &\vdash (r_{0}, w_{1}w_{2}\dots w_{k}, Y_{1}Y_{2} \dots Y_{k}) \\
> &\vdash^{*} (r_{2}, w_{2}\dots w_{k}, Y_{2} \dots Y_{k}) \\
> &\vdash^{*} \dots\\
> &\vdash^{*} (r_{k}, \epsilon, \epsilon)
> \end{align}
> $$
> 由于 $r_{k} = p$ ，我们得到了 $(q, w, X) \vdash^{*} (p, \epsilon, \epsilon)$

则根据上述结论
$$
S \overset{*}{\Rightarrow} w \iff \exists p \in Q, [q_{0}Z_{0}p] \overset{*}{\Rightarrow} w \iff (q_{0}, w, Z_{0}) \vdash^{*} (p, \epsilon, \epsilon) \iff w \in N(P)
$$

## Deterministic Pushdown Automata

PDA 默认即是 Nondeterministic 的，而实际上 deterministic 的 PDA 也有重要的作用

### Definition

一个 PDA $P = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ 是 DPDA (Deterministic PDA) 当且仅当满足

* 对于任何 $q \in Q, a \in \Sigma, a = \epsilon, X \in \Gamma$ ，$\delta(q, a, X)$ 只有一个元素
* 若对 $a \in \Sigma$ 有 $\delta(q, a, X)$ 非空，则 $\delta(q, \epsilon, X)$ 一定是空的 

### Regular language and DPDA

DPDA 接受的语言集合在正则语言和 CFL 之间，首先可以证明所有的正则语言都可以被 DPDA 接受

如果 $L$ 是正则语言，则存在 DPDA $P$ 使得 $L = L(P)$

> Proof. 显然，只需要利用 DPDA 中 DFA 的部分即可
>
> 令 DFA $A = (Q, \Sigma, \delta_{A}, q_{0}, F)$ ，则可以构造一个 DPDA
> $$
> P = (Q, \Sigma, \{Z_{0}\}, \delta_{P}, q_{0}, Z_{0}, F)
> $$
> 对于所有满足 $\delta(q, a) = p$ 的 $p, q \in Q$ ，令 $\delta_{P}(q, a, Z_{0}) = \{(p, Z_{0})\}$ 即可
>
> 显然 $(q_{0}, w, Z_{0}) \vdash^{*} (p, \epsilon, Z_{0}) \iff \delta_{A}(q_{0}, w) = p$ ，证明基于 $w$ 的长度归纳即可

Prefix Property: 没有两个不同的字符串满足其中一个是另一个的前缀

则有定理：对某个 DPDA $P$ 来说如果语言 $L = N(P)$ 当且仅当 $L$ 有 prefix property 并且存在 DPDA $P^{\prime}$ 满足 $L = L(P^{\prime})$

故可以看出正则语言可以由 acceptance by final state 的 DPDA 描述，但不一定能由 acceptance by empty stack 的 DPDA 描述，即对于 DPDA 来说 $L(P)$ 的描述能力是强于 $N(P)$ 的，两者并不等价

### DPDA and Context-Free Language

虽然 DPDA 能接受形如 $\{wcw^{R}\}$ 这样的非正则的语言，但是也存在 CFL $L$ 满足不存在 DPDA $P$ 使得 $L = L(P)$ ，如 $\{ww^{R}\}$ ，当读完 $w$ 的时候栈已清空，没有信息用于识别后续的 $w^{R}$ 

故对于 DPDA 来说， $L(P)$ 识别的语言集合是正则语言的超集，CFL 的子集

### DPDA and Ambiguous Grammars

如果对 DPDA $P$ 有 $L = N(P)$ ，那么这个语言存在一个无歧义的文法

如果对 DPDA $P$ 有 $L = L(P)$ ，那么这个语言存在一个无歧义的文法

上述定理的证明可以见课本 P.255-256