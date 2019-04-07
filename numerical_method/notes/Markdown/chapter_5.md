## 第5章 解线性方程组的直接方法

### 5.1 引言与预备知识

#### 5.1.2 向量和矩阵

定义、基本运算、单位阵、非奇异矩阵、行列式

**行列式性质**

① $\det(\boldsymbol{AB})=\det(\boldsymbol{A})\det(\boldsymbol{B})​$

② $\det(\boldsymbol{A}^T)=\det(\boldsymbol{A})$

③ $\det(c\boldsymbol{A})=c^n\det(\boldsymbol{A})$

④ $\det(\boldsymbol{A})\ne 0\iff\boldsymbol{A}是非奇异矩阵​$

#### 5.1.3 矩阵的特征值与谱半径

**定义 1** 特征值、特征向量，A的全体特征值称为A的**谱**，记作$\sigma(\boldsymbol{A})=\{\lambda_1,\lambda_2,\cdots,\lambda_n\}​$，记
$$
\rho(\boldsymbol{A})=\max_{1\leq i\leq n}|\lambda_i|
$$
称为矩阵A的**谱半径**.

### 5.2 高斯消去法

#### 5.2.1 高斯消去法

**定理 5** (1) 如果$a_{kk}\ne 0(k=1,2,\cdots,n)$，则可通过高斯消去法将$\boldsymbol{Ax=b}$约化为等价的三角形线性方程组，且计算方式为

​	①消元计算

​	②回代计算

(2) 如果$\boldsymbol{A}$为**非奇异矩阵**，则可通过高斯消去法（及交换两行的初等变换）将$\boldsymbol{Ax=b}$约化为等价的三角形线性方程组

**定理 6** 约化的著元素$a_{ii}^{(i)}\ne 0(i=1,2,\cdots,k)$的充要条件式矩阵$\boldsymbol{A}$的顺序主子式$D_i\ne 0(i=1,2,\cdots,k)$

#### 5.2.2 矩阵的三角分解

高斯消去法的过程相当于左乘了一系列下三角初等矩阵， 从而可以联系到矩阵分解

**定理 7**（矩阵的LU分解） 设$\boldsymbol{A}$为$n$阶矩阵，如果$\boldsymbol{A}$的顺序主子式$D_i\ne0(i=1,2,\cdots,n-1)$，则$\boldsymbol{A}$可分解为一个单位下三角矩阵$\boldsymbol{L}$和一个上三角矩阵$\boldsymbol{U}$的乘积，且这种分解是**唯一**的

#### 5.2.3 列主元消去法

绝对值最大的元素作为主元，以使高斯消去法具有较好的数值稳定性

### 5.3 矩阵三角分解法

#### 5.3.1 直接三角分解法

*Doolittle分解*

1. $u_{1i}=a_{1i}(i=1,2,\cdots,n),l_{i1}=a_{i1}/u_{i1}(i=2,3,\cdots,n)$
2. $u_{ri}=a_{ri}-\sum_{k=1}^{r-1}l_{rk}u_{ki},i=r,r+1,\cdots,n​$
3. $l_{ir}=(a_{ir}-\sum_{k=1}^{r-1}u_{kr})/u_{rr},i=r+1,\cdots,n,\text{ and }r\ne n$
4. $\begin{cases}y_1=b_1,\\y_i=b_i-\sum_{k=1}^{i-1}l_{ik}y_k,i=r+1,\cdots,n;\end{cases}$
5. $\begin{cases}x_n=y_n/u_{nn},\\x_i=(y_i-\sum_{k=i+1}^nu_{ik}x_k)/u_{ii},i=n-1,n-2,\cdots,1.\end{cases}$

1, 2, 3计算L, U；4, 5解$\boldsymbol{Ly=b},\boldsymbol{Ux=y}​$

**形象化记忆**

<u>就是U一行，L一列这么算，联系合同变换</u>

1中先将A的第一行赋值给U第一行，L每行乘以U第一列等于L每行第一个乘以u11（因为U第一列只有一个元素非零），从而有了1后半个式子

2是给U的第r行赋值，ari就是L的第r行乘以U的第i列（都是到r-1，所以是之前已经计算好的值，当$r<k时,l_{rk}=0$），又有lii=1，对照**分解式**（见课本/课件），有$a_{ri}=\sum_{k=1}^{n}l_{rk}u_{ki}=\sum_{k=1}^{r-1}l_{rk}u_{ki}+1\cdot u_{ri},i=r,r+1,\cdots,n$，移项得出2式。再intuitive一点就是A(r, i)减去L和U对应行(r)和列(i)的乘积扣出来一个$1\times u_{ri}$得到扣出来的这个uri

3类似地，对照**分解式**有$a_{ri}=\sum_{k=1}^{n}l_{rk}u_{ki}=\sum_{k=1}^{r-1}l_{rk}u_{ki}+l_{kr}u_{rr}$

4，5两步同高斯消元法的回代计算，容易理解。

#### 5.3.2 平方根法

> **线代知识**
>
> **定理 5.2.1** 若$\boldsymbol{A}$为$n$阶的实对称矩阵，则下列条件互为等价：
>
> 1. $\boldsymbol{A}​$为正定矩阵；
> 2. $\boldsymbol{A}$的特征值均为正
> 3. $\boldsymbol{A}$的正惯性指数为$n$；
> 4. $\boldsymbol{A}$的各阶顺序主子式均为正.

**定理 9**（对称阵的三角分解定理）设$\boldsymbol{A}$为$n$阶对称矩阵，且$\boldsymbol{A}$的所有顺序主子式均不为零，则$\boldsymbol{A}$可唯一分解为
$$
\boldsymbol{A=LDL}^T,
$$
其中$\boldsymbol{L}​$为单位下三角矩阵，$\boldsymbol{D}​$为对角矩阵.

**单位矩阵** 

**定理 10**（对称正定矩阵的三角分解或Cholesky分解） 如果$\boldsymbol{A}$为$n$阶对称正定矩阵，则存在一个实的非奇异下三角矩阵$\boldsymbol{L}$使得$\boldsymbol{A=LL}^T$，当限定$\boldsymbol{L}$的对角元素为正时，这种分解时唯一的
$$
\boldsymbol{A}=
\begin{pmatrix}
l_{11}\\
l_{21} & l_{22}\\
\vdots&\vdots&\ddots\\
l_{n1}&l_{n2}&\cdots&l_{nn}
\end{pmatrix}
\begin{pmatrix}
l_{11}&l_{21}&\cdots&l_{n1}\\
 & l_{22} & \cdots &l_{n2}\\
~&~&\ddots&\vdots\\
&&&l_{nn}
\end{pmatrix}
$$
其中$l_{ii}>0(i=1,2,\cdots,n)​$.由矩阵乘法及$l_{jk}=0(j<k)​$得
$$
a_{ij}=\sum_{k=1}^nl_{ik}l_{jk}=\sum_{k=1}^{n-1}l_{ik}l_{jk}+l_{jj}l_{ii}
$$
于是有解对称正定方程组$\boldsymbol{Ax=b}$的平方根法计算公式：

​	对于$j=1,2,\cdots,n​$

1. $l_{jj}=(a_{jj}-\sum_{k=1}^{j-1}l_{jk}^2)^{\frac12}​$
2. $l_{ij}=(a_{ij}-\sum_{k=1}^{j-1}l_{ik}l_{jk})/l_{jj},i=j+1,\cdots,n$
3. $y_i=(b_i-\sum_{k=1}^{i-1}l_{ik}y_i)/l_{ii},i=1,2,\cdots,n​$
4. $x_i=(b_i-\sum_{k=i+1}^{n}l_{ki}x_k)/l_{ii},i=n,n-1,\cdots,1$

**形象化记忆**

首先有$a_{jj}$是L的第j行和L^T的第j列两个向量的内积，即L的第j行的模的平方，$a_{jj}=\sum_{k=1}^nl_{jk}^2=\sum_{k=1}^jl_{jk}^2（其余乘积为0）=\sum_{k=1}^{j-1}l_{jk}^2+l_{jj}^2（剥离）$，稍作调整即获得1式

对于2式要注意当$j<k$时，$l_{jk}=0$，所以$a_{ij}$作为L的两个行向量内积只会乘到非零元素较小的数量那么多次，同样扣除$l_{ij}\times l_{jj}$这一项出来，移项处以$l_{jj}$（1式算过），就可以算出$l_{ij}$

3，4式同样是回代计算解$\boldsymbol{Ly=b},\boldsymbol{L}^T\boldsymbol{x=y}$

**改进的平方根法没讲**

#### 5.3.3 追赶法

对角占优的三对角线方程组

**归纳法证明** 见课本

追赶法公式

1. 计算$\{\beta_i\}$的递推公式

$$
\beta_1=c_1/b_1
$$

$$
\beta_i=c_i/(b_i-a_i\beta_{i-1}),i=2,3,\cdots,n-1
$$

2. 解$\boldsymbol{Ly=f}​$

$$
y_1=f_1/b_1
$$

$$
y_i=(f_i-a_iy_{i-1})/(b_i-a_i\beta_{i-1}),i=2,3,\cdots,n
$$

3. 解$\boldsymbol{Ux=y}$

$$
x_n=y_n
$$

$$
x_i=y_i-\beta_ix_{i+1},i=n-1,n-2,\cdots,2,1
$$



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
证明见课本。

#### 5.4.2 矩阵范数

**定义 5**（矩阵的范数）

(1) 正定条件

(2) $|c\boldsymbol{A}|=|c|\lVert \boldsymbol{A}\rVert​$（齐次条件）

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

(2) $cond(c\boldsymbol{A})_v = cond(\boldsymbol{A})_v$

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