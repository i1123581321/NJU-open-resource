[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# 随机向量及其分布

若随机变量 $X_{1}, X_{2}, \dots X_{n}$ 定义在同一样本空间 $\Omega$ 上，则称 $(X_{1}, X_{2}, \dots , X_{n})$ 为 $n$ 维随机变量

## 二维随机向量及其分布函数

### 分布函数

类似研究随机变量，可以为二维随机向量定义其 cdf

设 $(X, Y)$ 是二维随机向量，对任意实数 $x, y$ ，二元函数
$$
F(x, y) = P(X \leqslant x, Y \leqslant y)
$$
称为二维随机向量的分布函数，或称为 $X, Y$ 的**联合分布函数**

易得
$$
P(x_{1} < X \leqslant x_{2}, y_{1} < Y \leqslant y_{2}) = F(x_{2}, y_{2}) - F(x_{1}, y_{2}) - F(x_{2}, y_{1}) + F(x_{1}, y_{1})
$$
分布函数 $F(x, y)$ 有如下性质

1. $F(x, y)$ 对于 $x, y$ 都是单调不减的
2. $0 \leqslant F(x, y) \leqslant 1$ ，且对于固定的 $y$ 有 $F(-\infin, y) = 0$ ，对于固定的 $x$ 有 $F(x, -\infin) = 0$ 。$F(-\infin, -\infin) = 0, F(+\infin, +\infin) = 1$
3. $F(x+0, y) = F(x, y), F(x, y+0) = F(x, y)$ ，即 $F(x, y)$ 关于 $x, y$ 都是右连续的
4. 对于任意实数 $x_{1} \leqslant x_{2}, y_{1} \leqslant y_{2}$ 有 $F(x_{2}, y_{2}) - F(x_{1}, y_{2}) - F(x_{2}, y_{1}) + F(x_{1}, y_{1}) \geqslant 0$

满足以上性质的二元函数一定是某个二维随机向量的联合分布函数

根据联合分布函数，也可以得到两个分量各自的分布函数
$$
F_{X}(x) = P(X \leqslant x) = P(X \leqslant x, Y \leqslant +\infin) = F(x, +\infin)
$$
同理
$$
F_{Y}(y) = F(+\infin, y)
$$
将 $X， Y$ 的分布函数称为**边缘分布函数**

### 二维离散型随机向量

若二维随机向量 $(X, Y)$ 的每个分量都是离散型随机变量，称其为二维离散型随机向量

设二维离散型随机向量 $(X, Y)$ 取值可能为 $(x_{i}, y_{j}), i, j = 1, 2, \dots$ ，则
$$
P(X = x_{i}, Y = y_{j}) = p_{ij} \quad i,j = 1, 2, \dots
$$
称为 $(X, Y)$ 的联合分布律。

类比离散型随机变量，联合分布律有性质

* $p_{ij} \geqslant 0, i, j = 1, 2, \dots$
* $\sum_{i=1}^{+\infin}\sum_{j=1}^{+\infin} = 1$

> 二维离散型随机向量有两种重要的分布：多项分布，多元超几何分布。这两种分布分别是二项分布和超几何分布的推广
>
> 多项分布：在 $n$ 次重复独立实验中有三种不同结果，分别为 $A_{1}, A_{2}, A_{3}$ ，且 $P(A_{i}) = p_{i}$ 。以 $X_{1}, X_{2}$ 记录 $A_{1}, A_{2}$ 发生的概率，则有
> $$
> P(X_{1} = k_{1}, X_{2} = k_{2}) = \frac{n!}{k_{1}!k_{2}!(n-k_{1}-k_{2})!}p_{1}^{k_{1}}p_{2}^{k_{2}}(1 - p_{1} - p_{2})^{n - k_{1} -k_{2}}
> $$
> 记为 $(X_1, X_{2}) \sim M(n;p_{1}, p_{2}, p_{3})$
>
> 多元超几何分布：袋子中有三种球，分别有 $N_{1}, N_{2}, N_{3}$ 个，一共有 $N$ 个球，设 $X_{1}, X_{2}$ 记录不放回摸取 $n$ 个球时摸到 $1, 2$ 中球的个数，则有
> $$
> P(X_{1} = n_{1}, X_{2} = n_{2}) = \frac{C_{N_{1}}^{n_{1}}C_{N_{2}}^{n_{2}}C_{N_{3}}^{n_{3}}}{C_{N}^{n}}
> $$

二维离散型随机向量的联合分布函数为
$$
F(x, y) = P(X \leqslant x, Y \leqslant y) = \underset{x_{i} \leqslant x, y_{j} \leqslant y}{\sum}p_{ij}
$$
可定义其边缘分布律
$$
P(X = x_{i}) = \sum_{j=1}^{+\infin}p_{ij} = p_{i \cdot}\\
P(Y = y_{j}) = \sum_{i=1}^{+\infin}p_{ij} = p_{\cdot j}
$$

### 二维连续型随机变量

设二维随机向量 $(X, Y)$ 的分布函数为 $F(x, y)$ ，若存在非负可积二元函数 $p(x, y)$ 满足
$$
F(x, y) = \int_{-\infin}^{x}\int_{-\infin}^{y}p(u, v)dudv
$$
则称 $(X, Y)$ 为二维连续型随机向量，称 $p(x,y)$ 为其联合概率密度函数

易得联合密度有性质

1. $p(x, y) \geqslant 0$
2. $\int_{-\infin}^{+\infin}\int_{-\infin}^{+\infin}p(x, y)dxdy = 1$

若一个二元函数满足上述性质，则可以保证 $F(x, y)$ 满足分布函数的性质，故 $p(x, y)$ 是某个二维连续型随机向量的联合密度

同样可以得到对于任意实数 $x_{1} \leqslant x_{2}, y_{1} \leqslant y_{2}$ 有
$$
P(x_{1} < X \leqslant x_{2}, y_{1} < Y \leqslant y_{2}) = \int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}p(u, v)dudv
$$
更一般的，设 $G$ 为平面任一区域，则
$$
P((X, Y) \in G) = \underset{G}{\iint}p(x, y)dxdy
$$

> 重积分的计算可以使用累次积分或是换元法

联合密度也可以看作是联合分布的导函数。若 $p(x, y)$ 在点 $(x_{0}, y_{0})$ 处连续，则
$$
\left. \frac{\partial^{2}F(x, y)}{\partial x \partial y} \right|_{(x_{0}, y_{0})} = p(x_{0}, y_{0})
$$
对于任意有限实数 $x$ ，令 $G = (-\infin , x] \times (-\infin, +\infin)$ ，则可以得到 $X$ 的边缘分布
$$
F_{X}(x) = P((X, Y) \in G) = \int_{-\infin}^{x}\int_{-\infin}^{+\infin}p(x, y)dxdy
$$
求导，可以得到 $X$ 的概率密度为
$$
p_{X}(x) = \int_{-\infin}^{+\infin}p(x, y)dy
$$
同理，$Y$ 的概率密度为
$$
p_{Y}(y) = \int_{-\infin}^{+\infin}p(x, y)dx
$$
这两个概率密度称为 $X, Y$ 的**边缘概率密度**

连续型随机向量的分量都是连续型随机变量，但连续型随机变量组成的向量不一定是连续型随机向量

平面上有两种常见的二维连续型分布：均匀分布，二元正态分布

均匀分布：设 $G$ 是 $\R^{2}$ 上的有限区域，其面积 $S > 0$ ，由密度函数
$$
p(x, y) = 
\begin{cases}
\frac{1}{S} & (x, y) \in G\\
0 & (x, y) \notin G
\end{cases}
$$
给出的分布称为 $G$ 上的均匀分布。若 $G$ 为矩形 $[a, b] \times [c, d]$ ，则联合密度为
$$
p(x, y) = 
\begin{cases}
\frac{1}{(b- a)(d-c)} & (x, y) \in G\\
0 & (x, y) \notin G
\end{cases}
$$
则可以得到 $X$ 的边缘分布
$$
F_{X}(x) = P(X \leqslant x) = \frac{x-a}{b-a}, x \in[a, b]
$$
其密度函数为
$$
p_{X}(x) = 
\begin{cases}
\frac{1}{b-a} & x \in [a, b] \\
0 & x \notin [a, b]
\end{cases}
$$
即 $X$ 服从区间 $[a, b]$ 上的均匀分布。同理 $Y$ 服从区间 $[c, d]$ 上的均匀分布

**二元正态分布**：若二维随机向量 $(X, Y)$ 的联合密度函数为
$$
p(x, y) = \frac{1}{2 \pi \sigma_{1}\sigma_{2}\sqrt{1-\rho^{2}}}\exp \left\{ -\frac{1}{2(1-\rho^{2})} \left[ \left(\frac{x - \mu_{1}}{\sigma_1} \right)^{2} - 2\rho\left(\frac{x - \mu_{1}}{\sigma_1} \right)\left(\frac{y - \mu_{2}}{\sigma_2} \right) + \left(\frac{y - \mu_{2}}{\sigma_2} \right)^{2}  \right] \right\}
$$
其中 $\mu_{1}, \mu_{2} \in \R, \sigma_{1}, \sigma_{2} > 0, |\rho| < 1$ 均为常数，则称 $(X, Y)$ 服从二元正态分布。记为
$$
(X, Y) \sim N(\mu_{1},\mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho)
$$
易得 $X$ 的概率密度为
$$
p_{X}(x) = \frac{1}{\sqrt{2 \pi} \sigma_{1}}e^{-\frac{(x - \mu_{1})^{2}}{2\sigma_{1}^{2}}}
$$
即 $X \sim N(\mu, \sigma_{1}^{2})$ ，同理可得 $Y \sim N(\mu, \sigma_{2}^{2})$

二维正态分布的边缘分布是正态分布，且其不依赖于参数 $\rho$ ，从另一角度也说明了根据 $X, Y$ 的边缘分布**一般不能确定联合分布**

## 相互独立的随机变量

设 $F(x, y)$ 是二维随机向量 $(X, Y)$ 的联合分布，$F_{X}(x), F_{Y}(y)$ 为其边缘分布，若对所有 $x, y$ 都有
$$
P(X \leqslant x, Y \leqslant y) = P(X \leqslant  x)P(Y \leqslant y)\\
F(x, y) = F_{X}(x)F_{Y}(y)
$$
则称随机变量 $X, Y$ 是相互独立的。

对于连续型随机向量 $(X, Y)$ 而言，设其联合密度为 $p(x, y)$ ，且 $X, Y$ 的边缘密度为 $p_{X}(x), p_{Y}(y)$ ，则 $X, Y$ 独立等价于

$$
p(x, y) = p_{X}(x)p_{Y}(y)
$$
在平面上**几乎处处成立**

> 几乎处处成立意为除去平面上面积为 0 的集合，处处成立

对于离散型随机向量 $(X, Y)$ 而言，$X, Y$ 相互独立等价于对于所有 $x_{i}, y_{j}$ 有
$$
P(X = x_{i}, Y = y_{j}) = P(X = x_{i})P(Y = y_{j})
$$
实际中根据分布律或密度函数判断独立性比使用分布函数要方便

事实上，对于连续型随机向量 $(X, Y)$ ，$X, Y$ 独立 $\iff$ 存在函数 $g_{1}(x), g_{2}(y)$ ，满足
$$
p(x, y) = g_{1}(x)g_{2}(y)
$$
对于二维正态分布来说，其分量独立 $\iff$ 参数 $\rho = 0$

## 随机向量函数的分布