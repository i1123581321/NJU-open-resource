# Proof By Induction

## Proof by Induction

考虑证明 0 是加法右单位元的情况

```
Theorem plus_n_O_firsttry : ∀ n:nat,
  n = n + 0.
```

不能简单地用 `reflexivity` 证明，因为 n 作为任意数字在 + 里不能化简

用 `destruct` 来分情况讨论也不能证明，当证明 `n = S n'` 的 subgoal 时对于 `n'` 遇到了一样的问题

对于递归定义的集合上的性质可以用归纳证明

```
Theorem plus_n_O : ∀ n:nat, n = n + 0.
Proof.
  intros n. induction n as [| n' IHn'].
  - (* n = 0 *) reflexivity.
  - (* n = S n' *) simpl. rewrite <- IHn'. reflexivity. Qed.
```

`induction` 和 `destruct` 使用同样的 pattern 来引入变量，第二个 subgoal 里引入了归纳假说

## Proof Within Proofs

可以通过 `assert` 提供一些过于显然且 trivial 的定理及其证明过程，不用按照流程先定义再证明

```
Theorem mult_0_plus' : ∀ n m : nat,
  (0 + n) × m = n × m.
Proof.
  intros n m.
  assert (H: 0 + n = n). { reflexivity. }
  rewrite → H.
  reflexivity. Qed.
```

`assert` 引入两个 subgoal，一个是 assert 本身（用 `H:` 标记），另一个是调用 assert 时本身的 goal，但是唯一的不同在于现在多了个 assert 的条件

用花括号包起来对 assert 的证明可以提高可读性

## Formal vs. Informal Proof

形式化证明：代码

非形式化证明：算法（自然语言描述）

在人类间交流思想的时候形式化的证明交流效率较低

 