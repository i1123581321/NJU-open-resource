[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# 参数估计

参数估计是统计推断的主要内容，一般在总体分布已知但参数未知的情况下，利用样本构造合理的统计量对参数进行估计，可分为点估计和区间估计

## 点估计

设总体的分布为 $F(x;\theta)$ ，其中 $\theta = (\theta_{1}, \theta_{2}, \dots , \theta_{k})$ 为参数，则根据样本 $X_{1}, X_{2}, \dots, X_{n}$ 构造一个**统计量** $\hat{\theta}(X_{1}, X_{2}, \dots ,X_{n})$ 作为参数 $\theta$ 的估计。称
$$
\hat{\theta}(X_{1}, X_{2}, \dots ,X_{n})
$$
为 $\theta$ 的**估计量**，如果将样本的值带入 $\hat{\theta}$ 则得到
$$
\hat{\theta}(x_{1}, x_{2}, \dots, x_{n})
$$
为 $\theta$ 的估计值。这样的估计方法称为点估计

点估计主要可分为矩估计和极大似然估计

### 矩估计

矩估计的基本思想就是：用样本矩作为总体矩的估计

如果参数 $\theta = (\theta_{1}, \theta_{2}, \dots, \theta_{n})$ 可以表示为总体矩的函数 $\theta_{i} = h_{i}(\mu_{1}, \mu_{2}, \dots , \mu_{k})$ ，则用样本矩 $A_{1}, A_{2}, \dots, A_{k}$ 代替总体矩，得到的估计量即为矩估计量，即
$$
\hat{\theta_{i}} =h_{i}(A_{1}, A_{2}, \dots, A_{k})
$$
矩估计的基本原理是，根据大数定律，样本矩按概率收敛到总体矩，若 $h$ 为已知连续函数，则有
$$
h(A_{1}, A_{2}, \dots, A_{k}) \overset{P}{\to} h(\mu_{1}, \mu_{2}, \dots, \mu_{k})
$$
矩估计十分简单，因为并没有用到总体分布的信息，但是也正因为没有充分利用总体分布的信息，精度不高

### 极大似然估计

极大似然估计的基本思想是，要为参数选一个合理的估计值，就要使参数在取该值时，样本发生的概率最大

对于离散型总体 $X$，样本 $X_{i}$ 取值 $x_{i}$ 的概率为 $p(X = x_{i};\theta)$ ，则所有样本取观测值的概率为
$$
L(x_{1}, x_{2}, \dots, x_{n}; \theta) = L(\theta) = \prod_{i=1}^{n}p(X = x_{i};\theta)
$$
上述函数称为极大似然函数，极大似然估计就是选取使上述概率达到最大的参数值 $\hat{\theta}$ 作为参数 $\theta$ 的估计，即
$$
\hat{\theta} = \arg \max L(\theta)
$$
对于连续型总体 $X$，若其密度函数为 $p(x;\theta)$ ，则样本的概率密度函数为 $\prod_{i=1}^{n}p(x_{i};\theta)$ ，样本取值在 $(x_{1}, x_{2}, \dots, x_{n})$ 邻域的概率可近似为 $\prod_{i=1}^{n}p(x_{i};\theta)dx_{i}$ ，则为方便起见，选取极大似然函数为
$$
L(x_{1}, x_{2}, \dots, x_{n};\theta) = L(\theta) = \prod_{i=1}^{n}p(x_{i};\theta)
$$
极大似然函数一般为连乘形式，而由于 $L(\theta) > 0$ ，且 $\ln L(\theta)$ 为 $L(\theta)$ 的单调函数，有相同的最大值点，故可以用 $\ln L(\theta)$ （称为对数似然函数） 

写出极大似然函数后求其偏导，令偏导数为 0，解方程（组）即可得到极大似然估计量/值

有时也会有解方程法失效的情况，此时需要结合极大似然估计的定义来分析，即选择能使极大似然函数取值尽可能大的参数值

**极大似然估计的不变性**：若 $\hat{\theta}$ 是 $\theta$ 的极大似然估计，$\phi(\theta)$ 有单值反函数，则 $\phi(\hat{\theta})$ 是 $\phi(\theta)$ 的极大似然估计

## 估计量的评价标准

### 无偏性

设 $\hat{\theta}(X_{1}, X_{2}, \dots, X_{n})$ 为参数 $\theta$ 的一个估计量，若对任意 $\theta \in \Theta$ 满足
$$
E[\hat{\theta}(X_{1}, X_{2}, \dots, X_{n})] = \theta
$$
则称 $\hat{\theta}$ 是 $\theta$ 的**无偏估计量**

样本原点矩是总体原点矩的无偏估计，即
$$
E[A_{k}] = E\left[\frac{1}{n} \sum_{i=1}^{n}X_{i}^{k} \right] = \frac{1}{n}\sum_{i=1}^{n}E[X_{i}^{k}] = \mu_{k}
$$
样本方差也是样本的无偏估计

### 均方误差准则

用 $E[(\hat{\theta} - \theta)^{2}]$ 来估计 $\hat{\theta}$ 与 $\theta$ 偏离的程度，记为
$$
M(\hat{\theta}, \theta) = E[(\hat{\theta} - \theta)^{2}]
$$
称其为**均方误差**

显然，均方误差越小越好

对于均方误差的计算，有
$$
M(\hat{\theta}, \theta) = D[\hat{\theta}] + (E[\hat{\theta}] - \theta)^{2}
$$
显然在 $\hat{\theta}$ 无偏时，均方误差就是 $\hat{\theta}$ 的方差

### 一致性

一致性的含义是当样本量越来越大时，估计量也应当越来越接近真实参数

设 $\hat{\theta}(X_{1}, X_{2}, \dots, X_{n})$ 为参数 $\theta$ 的一个估计量，若对任意 $\theta \in \Theta$ 满足
$$
\hat{\theta} \overset{P}{\to} \theta
$$
则称 $\hat{\theta}$ 是 $\theta$ 的**一致估计量**

## 区间估计

### 基本概念

除了构造一个点来估计未知参数以外，也可以构造一个区间 $(\hat{\theta_{1}}, \hat{\theta_{2}})$ 来估计参数 $\theta$ 的范围。

区间包含参数 $\theta$ 的概率称为区间的置信度

如果设 $\theta$ 是总体 $X$ 的未知参数，$X_{1}, X_{2}, \dots , X_{n}$ 是来自总体的样本，若对事先给定的常数 $\alpha(0 < \alpha < 1)$ 存在两个统计量
$$
\hat{\theta_{1}}(X_{1}, X_{2}, \dots, X_{n})\\
\hat{\theta_{2}}(X_{1}, X_{2}, \dots, X_{n})
$$
满足
$$
P(\hat{\theta_{1}} < \theta < \hat{\theta_{2}}) = 1 - \alpha
$$
则称区间 $(\hat{\theta_{1}}, \hat{\theta_{2}})$ 为 $\theta$ 的置信度为 $1 - \alpha$ 的**置信区间**

需要注意的是，置信度代表在取多个区间时，大约有 $100(1-\alpha)\%$ 的区间包含 $\theta$ ，而对于某个确定的区间来说 $\theta$ 只有在其中和不在其中两种可能

有时候仅关注未知参数的上限/下限，此时称为单侧置信区间

如果设 $\theta$ 是总体 $X$ 的未知参数，$X_{1}, X_{2}, \dots , X_{n}$ 是来自总体的样本，若对事先给定的常数 $\alpha(0 < \alpha < 1)$ 存在统计量 $\hat{\theta_{1}}$ 使得
$$
P(\hat{\theta_{1}} < \theta) = 1- \alpha
$$
则称 $(\hat{\theta_{1}}, \infin)$ 为 $\theta$ 的置信度为 $1 - \alpha$ 的单侧置信区间，上限同理

### 枢轴变量法

对于区间估计，有一种一般的方法

* 寻找一个样本函数 $U(X_{1}, X_{2}, \dots, X_{n})$ 包含待估计的参数 $\theta$ ，但是不含其他未知参数。并且 $U$ 的分布要已知。这个函数称为枢轴变量

* 由于 $U$ 的分布已知，故可以根据给定的置信度 $1 - \alpha$ ，找到两个常数 $a, b$ 满足
  $$
  P(a < U < b) = 1 - \alpha
  $$

* 变形不等式，解出 $\hat{\theta_{1}} < \theta < \hat{\theta_{2}}$ ，即为所求置信区间

## 正态总体的置信区间

### 正态总体均值的置信区间

给定置信度 $1 - \alpha$ ，设 $X_{1}, X_{2}, \dots ,X_{n}$ 为来自总体 $X \sim N(\mu, \sigma^{2})$ 的一组样本

若 $\sigma^{2}$ 已知，则可以取枢轴变量
$$
U = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)
$$
解不等式得到置信区间为
$$
\left(\overline{X} - u_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \overline{X} + u_{\alpha/2}\frac{\sigma}{\sqrt{n}} \right)
$$
若 $\sigma^{2}$ 未知，则取枢轴变量
$$
T = \frac{\overline{X} - \mu}{S / \sqrt{n}} \sim t(n-1)
$$
解不等式得到置信区间为
$$
\left(\overline{X} - t_{\alpha / 2}(n-1)\frac{S}{\sqrt{n}}, \overline{X} + t_{\alpha / 2}(n-1)\frac{S}{\sqrt{n}} \right)
$$

### 正态总体方差的置信区间

给定置信度 $1 - \alpha$ ，设 $X_{1}, X_{2}, \dots ,X_{n}$ 为来自总体 $X \sim N(\mu, \sigma^{2})$ 的一组样本

若 $\mu$ 未知，取枢轴变量
$$
\frac{(n-1)S^{2}}{\sigma^{2}} \sim \mathcal{X^{2}}(n-1)
$$
解不等式即可得到置信区间为
$$
\left(\frac{(n-1)S^{2}}{\mathcal{X}^{2}_{\alpha/2}(n-1)}, \frac{(n-1)S^{2}}{\mathcal{X}^{2}_{1- \alpha/2}(n-1)} \right)
$$

### 两个正态总体均值差的置信区间

给定置信度 $1 - \alpha$ ，设 $X_{1}, X_{2}, \dots ,X_{n_{1}}$ 为来自总体 $X \sim N(\mu_{1}, \sigma^{2}_{1})$ 的一组样本，$Y_{1}, Y_{2}, \dots, Y_{n_{2}}$ 是来自总体 $Y \sim N(\mu_{2}, \sigma^{2}_{2})$ 的一组样本，且两样本相互独立

若 $\sigma^{2}_{1}, \sigma^{2}_{2}$ 已知，则取枢轴变量
$$
U = \frac{\overline{X} - \overline{Y} - (\mu_{1} - \mu_{2})}{\sqrt{\dfrac{\sigma^{2}_{1}}{n_{1}} + \dfrac{\sigma^{2}_{2}}{n_{2}}}} \sim N(0, 1)
$$
解不等式得到置信区间为
$$
\left(\overline{X} - \overline{Y} - u_{\alpha/2}\sqrt{\dfrac{\sigma^{2}_{1}}{n_{1}} + \dfrac{\sigma^{2}_{2}}{n_{2}}},\overline{X} - \overline{Y} + u_{\alpha/2}\sqrt{\dfrac{\sigma^{2}_{1}}{n_{1}} + \dfrac{\sigma^{2}_{2}}{n_{2}}} \right)
$$
可以类比单个正态总体的情况，基本原理为
$$
\overline{X} - \overline{Y} \sim N\left(\mu_{1} - \mu_{2}, \frac{\sigma^{2}_{1}}{n_{1}} + \frac{\sigma^{2}_{2}}{n_{2}} \right)
$$
若 $\sigma^{2}_{1} = \sigma^{2}_{2} = \sigma^{2}$ 但 $\sigma^{2}$ 未知，则取枢轴变量
$$
T = \sqrt{\frac{n_{1}n_{2}(n_{1} + n_{2} - 2)}{n_{1} + n_{2}}}\frac{(\overline{X} - \overline{Y}) - (\mu_{1} - \mu_{2})}{\sqrt{(n_{1} - 1)S^{2}_{1} + (n_{2} - 1)S^{2}_{2}}} \sim t(n_{1} + n_{2} - 2)
$$
为了方便表示，设
$$
S_{w} = \sqrt{\frac{(n_{1} - 1)S^{2}_{1} + (n_{2} - 1)S^{2}_{2}}{n_{1} + n_{2} - 2}}
$$
则置信区间为
$$
\left(\overline{X} - \overline{Y} - t_{\alpha/2}(n_{1} + n_{2} - 2)S_{w}\sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}}, \overline{X} - \overline{Y} + t_{\alpha/2}(n_{1} + n_{2} - 2)S_{w}\sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)
$$
同样可以类比单个正态总体的情况

### 两个正态总体方差比的置信区间

给定置信度 $1 - \alpha$ ，设 $X_{1}, X_{2}, \dots ,X_{n_{1}}$ 为来自总体 $X \sim N(\mu_{1}, \sigma^{2}_{1})$ 的一组样本，$Y_{1}, Y_{2}, \dots, Y_{n_{2}}$ 是来自总体 $Y \sim N(\mu_{2}, \sigma^{2}_{2})$ 的一组样本，且两样本相互独立

若 $\mu_{1}, \mu_{2}$ 未知，则取枢轴变量
$$
F = \frac{S^{2}_{1}\sigma^{2}_{2}}{S^{2}_{2}\sigma^{2}_{1}} \sim F(n_{1 } - 1, n_{2} - 1)
$$
则置信区间为
$$
\left(\frac{S^{2}_{1}}{S^{2}_{2}}\frac{1}{F_{\alpha/2}(n_{1} - 1, n_{2} - 1)}, \frac{S^{2}_{1}}{S^{2}_{2}}\frac{1}{F_{1 - \alpha/2}(n_{1} - 1, n_{2} - 1)}\right)
$$

## 非正态总体的区间估计

总体分布非正态时，通常采用大样本法，求得枢轴变量的近似分布

设 $X_{1}, X_{2}, \dots, X_{n}$ 为来自均值为 $\mu$ ，方差为 $\sigma^{2}$ 的总体的一组样本，给定置信度 $1 - \alpha$ ，求均值 $\mu$ 的置信区间，则根据中心极限定理，有
$$
\frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \approx N(0, 1)
$$
由于 $\sigma^{2}$ 未知，使用样本标准差 $S$ 代替，枢轴变量为
$$
U = \frac{\overline{X} - \mu}{S /\sqrt{n}} \approx N(0, 1)
$$
解不等式，置信区间为
$$
\left(\overline{X} - u_{\alpha/2}\frac{S}{\sqrt{n}},\overline{X} + u_{\alpha/2}\frac{S}{\sqrt{n}} \right)
$$