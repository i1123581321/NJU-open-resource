[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# Properties of Context-Free Grammar

## The Pumping Lemma for CFL

### Parse tree

考虑一个 CNF 文法 $G = (V, T, P, S)$ 的 parse tree，且其 yield 为 $w$ ，若最长路径长度为 $n$ ，则有 $|w| \leqslant 2^{n-1}$

> Proof. 根据 $n$ 归纳即可
>
> Basis. $n = 1$ ，最长路径长为 1 的 parse tree 只有一个 root 和一个标记为 terminal 的叶节点，故 $|w| = 1$ ，而 $2^{n-1} = 2^{0} = 1, |w| \leqslant 2^{n-1}$
>
> Induction. 考虑最长路径为 $n$ ，则根节点一定使用了产生式 $A \to BC$ ，则任意子树中最长路径都不超过 $n-1$ ，根据 I. H. ，两颗子树的 yield 长度均不超过 $2^{n-2}$ ，则整棵树的 yield 长度不超过 $2^{n-1}$

### Pumping Lemma

令 $L$ 为一个 CFL，则存在常数 $n$ ，对于任意属于 $L$ 的 string $z$ ，若 $|z| \geqslant n$ ，则可以将 $z$ 写作 $uvwxy$ ，并且满足

* $|vwx| \leqslant n$
* $|vx| > 0$
* 对任意 $i \geqslant 0$ ，有 $uv^{i}wx^{i}y \in L$ 

> Proof. 
>
> 考虑 $L$ 的 CNF 文法 $G = (V, T, P, S)$ ，满足 $L - \{\epsilon\} = L(G)$ ，则假设 $G$ 中有 $m$ 个 variable，令 $n = 2^{m}$ ，令 $z$ 为 $L$ 中长度至少为 $n$ 的 string，根据上文的结论，任何最长路径为 $m$ 的 parse tree 其 yield 长度不超过 $2^{m-1} = n / 2$ ，则 yield 为 $z$ 的 parse tree 最长路径至少为 $m+1$ 
>
> 考虑最长路径，设其长度为 $k+1(k \geqslant m)$ ，则其路径上出现了 $k + 1$ 个 variable ，记为 $A_{0}, A_{1}, \dots , A_{k}$ ，而 $G$ 中有 $m$ 个不同的 variable，根据 PHP，路径上至少有两个 variable 是相同的，考虑路径上的最后 $m+1$ 个 variable，即 $A_{k-m}$ 到 $A_{k}$ ，设 $A_{i} = A_{j}, k-m \leqslant i < j \leqslant k$ 
>
> 则可以划分 parse tree 的 yield，令 $w$ 为子树 $A_{j}$ 的 yield，令 $vwx$ 为子树 $A_{i}$ 的 yield，令 $uvwxy$ 为整棵树的 yield。由于 CNF 没有 unit production，故 $v, x$ 不同时为 $\epsilon$ 
>
> 因此可以构造新的 parse tree，如使用 $A_{j}$ 的子树代替 $A_{i}$的子树，则 yield 为 $uwy$ ，对应 $uv^{i}wx^{i}y$ 中 $i=0$ 的情况。或是可以用 $A_{i}$ 的子树代替 $A_{j}$ 的子树，即 $uv^{2}wx^{2}y$ ，同理可以得到 $uv^{3}wx^{3}y, uv^{4}wx^{4}y ,\dots$ 
>
> 同时由于选择的是最后 $m+1$ 个 variable，即 $k - m \leqslant i \leqslant k$ ，则 $A_{i}$ 的子树中最长路径不会超过 $m+1$ ，则其产生的 string $|vwx| \leqslant 2^{m} = n$

Pumping Lemma 可以用于证明某 language 不是 CFL

## Closure Properties of CFL

### Substitutions

考虑 alphabet $\Sigma$ ，为其中每个元素 $a$ 选择一个语言 $L_{a}$ ，这个语言可以是定义在任意 alphabet 上的任意语言，则可以定义一个函数 $L_{a} = s(a)$ 。对于 string $w = a_{1}a_{2} \dots a_{n}$ 
$$
s(w) = \{x_{1}x_{2}\dots x_{n} : x_{i} \in s(a_{i})\}
$$
即 $s(w)$ 是一系列 language $s(a_{1}), s(a_{2}), \dots , s(a_{n})$ 的 concatenation，则对一个语言 $L$
$$
s(L) = \bigcup_{w \in L}s(w)
$$
则有：若 $L$ 是一个定义在 $\Sigma$ 的 CFL ，且对于每个 $a \in \Sigma$ ，有 $s(a)$ 为 CFL，则 $s(L)$ 是 CFL

> Proof. 基本思路为根据 $L$ 的 CFG，将其中每个 terminal $a$ 替换为 $s(a)$ 的 CFG 的开始符号
>
> 设 $L$ 的 CFG 为 $G = (V, T, P, S)$ ，而 $s(a)$ 的 CFG 为 $G_{a} = (V_{a}, T_{a}, P_{a} ,S_{a})$ ，且为了便于讨论，设 $V$ 以及任意 $V_{a}$ 的元素不重名。
>
> 则可以为 $s(L)$ 构造一个新的 CFG $G^{\prime} = (V^{\prime}, T^{\prime}, P^{\prime}, S)$ ，其中
>
> * $V^{\prime}$ 是 $V$ 与所有 $V_{a}$ 的 union
> * $T^{\prime}$ 是所有 $T_{a}$ 的 union
> * $P^{\prime}$ 包含
>   * 所有 $P_{a}$ 的产生式
>   * 所有 $P$ 的产生式，但将所有 terminal $a$ 用 $S_{a}$ 代替
>
> 则只需证明 $w \in L(G^{\prime}) \iff w \in s(L)$
>
> ($\Leftarrow$): 考虑 $w \in s(L)$ ，则设 $x = a_{1}a_{2} \dots a_{n} \in L$ ，且 $x_{i} \in s(a_{i})$ ，则有 $w = x_{1}x_{2} \dots x_{n}$ ，则原本从 $G$ 推导出的 $a_{1}a_{2} \dots a_{n}$ 在 $G^{\prime}$ 中将推导出 $S_{a_{1}}S_{a_{2}} \dots S_{a_{n}}$ 。由于 $G^{\prime}$ 包含所有 $G_{a}$ 中的产生式，则 $S_{a_{i}} \overset{*}{\Rightarrow} x_{i}$ 同样是 $G^{\prime}$ 中的推导，故有 $S \overset{*}{\Rightarrow} x_{1}x_{2} \dots x_{n} = w$ ，即 $w \in L(G^{\prime})$
>
> ($\Rightarrow$): 若 $w \in L(G^{\prime})$ ，则在推导过程中一定有 $S \overset{*}{\Rightarrow} S_{a_{1}}S_{a_{2}} \dots S_{a_{n}}$ ，因为在推导的开始将只使用 $G$ 中的产生式，直至推导出某个 $S_{a}$ ，而在 $S_{a}$ 的子树中将只使用 $G_{a}$ 中的产生式，因此根据该推导过程的 parse tree，可以得到一个字符串 $a_{1}a_{2} \dots a_{n} \in L(G)$ ，且 $x_{i} \in s(a_{i})$ ，满足
>
> * $w = x_{1}x_{2} \dots x_{n}$ 
> * 在 parse tree 中删除某些子树，其 yield 为 $S_{a_{i}}S_{a_{2}} \dots S_{a_{n}}$ 
>
> 由于 $x_{i} \in s(a_{i})$ ，故易得 $w \in s(L)$

### Applications of the Substitution Theorem

根据 substitution 的封闭性，可以得出 CFL 对于下列操作是封闭的

* union
* concatenation
* closure ($^*$) and positive closure ($^+$)
* homomorphism

> Proof. 只需构造特定的 substitution 即可
>
> * union：对于 CFL $L_{1}, L_{2}$ ，$L_{1} \cup L_{2} = s(L)$ ，其中 $L = \{1, 2\}, s(1) = L_{1}, s(2) = L_{2}$
> * concatenation：对于 CFL $L_{1}, L_{2}$ ，$L_{1} \cup L_{2} = s(L)$ ，其中 $L = \{12\}, s(1) = L_{1}, s(2) = L_{2}$
> * closure and positive closure：考虑 CFL $L_{1}$ ，令 $L = \{1\}^{*}, s(1) = L_{1}$ ，则 $L_{1}^{*} = s(L)$ ，同理，若 $L = \{1\}^{+}$ ，则 $L_{1}^{+} = s(L)$
> * homomorphism：考虑 $L$ 是定义在 $\Sigma$ 的 CFL，而 $h$ 是定义在 $\Sigma$ 的 homomorphism ，则对于任意 $a \in \Sigma$ ，定义 $s(a) = \{h(a)\}$ ，则 $h(L) = s(L)$

### Reversal

如果 $L$ 是 CFL，则 $L^{R}$ 也是 CFL

> Proof. 构造 $L$ 的文法 $G = (V, T, P, S)$ 使得 $L = L(G)$ ，则对于 $L^{R}$ 其 CFG 为 $G^{R} = (V, T, P^{R}, S)$ ，其中 $P^{R}$ 为每个产生式的 reversal，即若 $A \to \alpha \in G$ ，则 $A \to \alpha^{R} \in G^{R}$ 
>
> 对推导长度归纳即可得出 $L(G^{R}) = L^{R}$

### Intersection

CFL 对 intersection 是不封闭的，考虑
$$
L_{1} = \{0^{n}1^{n}2^{i}: n \geqslant 1, i \geqslant 1 \}\\
L_{2} = \{0^{i}1^{n}2^{n}: n \geqslant 1, i \geqslant 1\}
$$
上述两个语言都是 CFL，可以为其构造出对应的文法，但是其 intersection
$$
L = L_{1} \cap L_{2} = \{0^{n}1^{n}2^{n}:n \geqslant 1 \}
$$
不是 CFL（pumping lemma 即可证明）

但是 CFL 和 正则语言的 intersection 仍是 CFL，即

对于 CFL $L$ 和正则语言 $R$ ，$L \cap R$ 仍是 CFL

> Proof. 只需要平行地运行 PDA 和 DFA 即可
>
> 令 PDA $P = (Q_{P}, \Sigma, \Gamma, \delta_{P}, q_{P}, Z_{0}, F_{P})$ 满足 $L = L(P)$，令 DFA $A = (Q_{A}, \Sigma, \delta_{A}, q_{A}, F_{A})$ 满足 $R = L(A)$ 
>
> 则可构造 PDA
> $$
> P^{\prime} = (Q_{P} \times Q_{A}, \Sigma, \Gamma, \delta, (q_{P}, q_{A}), Z_{0}, F_{P} \times F_{A})
> $$
> 定义
> $$
> \delta((q, p), a, X) = \{((r, s), \gamma) : s = \delta_{A}(p, a) \text{ and } (r, \gamma) \in \delta_{P}(q, a, X)  \}
> $$
> 注意当 PDA 在 $\epsilon$ 上转换时，DFA 不改变状态
>
> 根据推导步数的归纳可以得出、
> $$
> (q_{P}, w, Z_{0}) \underset{P}{\vdash^{*}} (q, \epsilon, \gamma) \text{ and } \delta_{A}(q_{A}, w) = p \iff ((q_{P}, q_{A}), w, Z_{0})\underset{P^{\prime}}{\vdash^{*}} ((q, p), \epsilon, \gamma)
> $$
> 且 $(q, p)$ 为接收状态 $\iff q \in F_{P} \text{ and } p \in F_{A}$ ，故 $w \in L(P^{\prime}) \iff w\ \in L \text{ and } w \in A$
>
> 可以得出 $L(P^{\prime}) = L \cap R$

同样可以得出对于 CFL $L, L_{1}, L_{2}$ 和正则语言 $R$ 满足

* $L - R$ 是 CFL
* $\overline{L}$ 不一定是 CFL
* $L_{1} - L_{2}$ 不一定是 CFL

> Proof. 
>
> * $L - R = L \cap \overline{R}$ ，而 $\overline{R}$ 是正则
> * 若 $\overline{L}$ 总是 CFL，则考虑 $L_{1} \cap L_{2} = \overline{\overline{L_{1}} \cup \overline{L_{2}}}$ ，这与上述结论矛盾
> * 若 $L_{1} - L_{2}$ 总是 CFL，则 $\Sigma^{*} - L = \overline{L}$ 也是 CFL，这与上述结论矛盾 

### Inverse Homomorphism

证明思路类似证明正则语言对 inverse homomorphism 是封闭的。构造一个 PDA，每当读入一个输入 $a$ ，则将 $h(a)$ 放入一个 buffer 中，每次读取其中一个符号，用于模拟 PDA 的运行，直至读入结束，再读入下一个符号

考虑 CFL $L$ 和 homomorphism $h$ ，则 $h^{-1}(L)$ 也是 CFL

> Proof. 假设 $h$ 定义在 $\Sigma$ 上，且输出的 string 属于 $T^{*}$ ，且假设 $L$ 是定义在 $T$ 上的语言，则有 PDA $P = (Q, T, \Gamma, \delta, q_{0}, Z_{0}, F)$ 满足 $L = L(P)$ ，则构造一个新的 PDA
> $$
> P^{\prime} = (Q^{\prime}, \Sigma, \Gamma, \delta^{\prime}, (q_{0}, \epsilon), Z_{0}, F \times \{\epsilon\})
> $$
> 其中
>
> $Q^{\prime}$ 中的元素 $(q, x)$ 满足 $q \in Q$ 且 $x$ 是某个 $h(a)$ 的后缀，即用 $x$ 来模拟 buffer
>
> 由于 $a \in \Sigma$ 是有限的，故 $h(a)$ 也是有限的，则 $Q^{\prime}$ 中的状态也是有限的
>
> 对于 $\delta^{\prime}$ ，其定义分为两种情况
>
> * buffer 为空，即 $\delta^{\prime}((q, \epsilon), a, X) = \{((q, h(a)), X)\}$ ，此处的 $a \neq \epsilon$ 。即当 buffer 为空，$P^{\prime}$ 读入下一个输入 $a$ 并将 $h(a)$ 放入 buffer
>
> * buffer 不为空，则若 $(p, \gamma) \in \delta(q, b, X), b \in T \text{ or } b = \epsilon $ ，则
>   $$
>   ((p, x), \gamma) \in \delta^{\prime}((q, bx), \epsilon, X)
>   $$
>   即 $P^{\prime}$ 用 buffer 中第一个 symbol 模拟 $P$ 的运行
>
> 则有
> $$
> (q_{0}, h(w), Z_{0}) \underset{P}{\vdash^{*}} (p, \epsilon, \gamma) \iff ((q_{0}, \epsilon), w, Z_{0}) \underset{P^{\prime}}{\vdash^{*}}((p, \epsilon), \epsilon, \gamma)
> $$
> 证明基于对推导步数的归纳即可。需要注意的是 $P^{\prime}$ 在 buffer 非空时一定模拟 $P$ 的运行，但是当 buffer 为空时仍有可能继续模拟 $P$ 的运行
>
> 故 $w \in L(P^{\prime}) \iff h(w) \in L(P)$ ，即 $L(P^{\prime}) = h^{-1}(L(P))$

## Decision Properties of CFL

