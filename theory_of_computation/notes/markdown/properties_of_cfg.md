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
> 考虑最长路径，设其长度为 $k+1(k \geqslant m)$ ，则其路径上出现了 $k + 1$ 个 variable ，记为 $A_{0}, A_{1}, \dots , A_{k}$ ，而 $G$ 中有 $m$ 个不同的 variable，根据 PHP，路径上至少有两个 variable 是相同的