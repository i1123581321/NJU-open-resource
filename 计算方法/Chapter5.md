## 第5章 解线性方程组的直接方法

### 5.2 高斯消去法

#### 5.2.1 高斯消去法

#### 5.2.2 矩阵的三角分解

#### 5.2.3 列主元消去法

### 5.3 矩阵三角分解法

#### 5.3.1 直接三角分解法

Doolittle

#### 5.3.2 平方根法

#### 5.3.3 追赶法

### 5.4 向量和矩阵的范数

#### 5.4.1 向量范数

**向量线性无关**
$$
k_1\alpha_1+k_2\alpha_2+\cdots+k_n\alpha_n=0\iff k_1=k_2=\cdots=k_n=0
$$
**定义3** （向量的范数）

(1) $\lVert x\rVert\geq 0$（正定条件）

(2) $\lVert\alpha x\rVert=|\alpha| \lVert x\rVert$

(3) $\lVert x+y\rVert \leq \lVert x\rVert +\lVert y\rVert$（三角不等式）

**常用范数**

∞

1

2

p
$$
\lVert x\rVert_p=(\sum_{i=1}^n|x_i|^p)^{\frac{1}{p}}
$$
**连续性**

**定理 14**（向量范数的等价性）
$$
\exists c_1,c_2>0,\forall x\in\R^n,\ c_1||x||_s\leq||x||_t\leq c_2||x||_s
$$

先不管证明。

#### 5.4.2 矩阵范数

**定义 5**（矩阵的范数）

(1) 正定条件

(2) $|c\boldsymbol{A}|=|c|\lVert \boldsymbol{A}\rVert$（齐次条件）

(3) 三角不等式

(4) $\lVert\boldsymbol{A}\boldsymbol{B}\rVert\leq\lVert\boldsymbol{A}\rVert\lVert\boldsymbol{B}\rVert$

**定义 6**（矩阵的算子范数）
$$
\lVert \boldsymbol{A}\rVert_v=\max_{x\ne 0}\frac{\lVert\boldsymbol{A}x\rVert_v}{\lVert \boldsymbol{x}\rVert_v}
$$
称为**算子范数/从属范数**

**定理 16** 向量范数，生成矩阵范数，且满足相容条件
$$
\lVert\boldsymbol{A}x\rVert_v\leq \lVert\boldsymbol{A}\rVert_v\ \lVert \boldsymbol{x}\rVert_v
$$
**定理 17** 行范数（∞）、列范数（1）、2-范数

**定理 18**
$$
\rho(\boldsymbol{A})\leq\lVert\boldsymbol{A}\rVert
$$
对任意算子范数成立

**定理 19** 对称矩阵，
$$
\lVert\boldsymbol{A}\rVert_2=\rho(\boldsymbol{A})
$$
**定理 20** 好像课堂没涉及

### 5.5 误差分析

#### 5.5.1 矩阵的条件数

**定义 7** 病态良态

**定义 8** 非奇异阵，条件数$cond(\boldsymbol{A})_v=\lVert\boldsymbol{A}^{-1}\rVert_v\ \lVert\boldsymbol{A}\rVert_v(v=1,2 \text{ or }\infty)$

**性质**

(1) $cond(\boldsymbol{A}) \geq 1$

(2) $cond(c\boldsymbol{A})_v = cond(\boldsymbol{A})_v​$

(3) 正交矩阵A，$cond(\boldsymbol{A})_2$；如果A为非奇异矩阵，R为正交矩阵，则
$$
cond(\boldsymbol{RA})_2=cond(\boldsymbol{AR})_2=cond(\boldsymbol{A})_2
$$
**发现病态**

算cond

课件中讲的是**“一般由经验得出”**

**缓解病态**

1. 高精度
2. 预处理，$cond(\boldsymbol{PAQ})<cond{(\boldsymbol{A})}$
3. 平衡方法——乘一个Diag，**归一化**

#### 5.5.2 迭代改善法（课上没讲）
