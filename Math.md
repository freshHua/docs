<center style=“color:red”>数学公式</center>
===============================================

###分组
通过大括号{}将操作数与符号分割开，消除二义性。
$$ x^{10} $$
###特殊符号
符号 |命令
----|----
$\infty$ |\infty
$\to$|\to
$\uparrow$|\uparrow
$\downarrow$|\downarrow
$\dots$|\dots

###括号
原始符号并不会随着公式大小缩放，可以使用\left(...\right)来自适应地调整括号大小
$$
f\left(
   \left[ 
     \frac{
       1+\left\{x,y\right\}
     }{
       \left(
          \frac{x}{y}+\frac{y}{x}
       \right)
       \left(u+1\right)
     }+a
   \right]^{\frac{3}{2}}
\right)
$$


###关系比较运算
符号 |描述
----|----
$\gt$ |\gt
$\lt$ |\lt
$\ge$ |\ge
$\le$ |\le
$\ne$ |\ne

###绝对值
\lvertx\rvert
$$
\lvert{x-3}\rvert
$$
###运算符号
运算符 |表示
----|----
+|+
-|-
$\times$|\times
$\div$|\div
$\cdot$|\cdot

###逻辑与集合论
符号 |描述
----|----
$\in$ |\in
$\notin$ |\notin
$\because$|\because
$\therefore$|\therefore

###上下标
上标：^
下标：_
举例：C_n^2呈现为 $ C_n^2 $

###矢量
\vec{x}
$$\vec{x}$$
\overrightarrow{AB}
$$\overrightarrow{AB}$$
###分式
\frac{x}{y}
$$\frac{x}{y}$$
###根式
\sqrt[x]{y}
$$\sqrt[x]{y}$$
###求和
\sum
$$\sum_{i=0}^n{a_i}$$
###极限
\lim
$$\lim_{x\to 0}$$
###积分
\int
$$\int_0^\infty{f(x)dx}$$
###条件表达式
x = \begin{cases}
   a &\text{if } b  \\\
   c &\text{if } d
\end{cases}
$$ f(n) =
\begin{cases}
n/2,  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}
$$
$$\begin{cases}
a_1x+b_1y+c_1z=d_1 \\ 
a_2x+b_2y+c_2z=d_2 \\ 
a_3x+b_3y+c_3z=d_3
\end{cases}
$$
###等式对齐
\begin{align}…\end{align},每一行用\\结束

$$
\begin{align}
f(x)&=\left(x^3\right)+\left(x^3+x^2+x^1\right)+\left(x^3+x^2\right) \\
f'(x)&=\left(3x^2+2x+1\right)+\left(3x^2+2x\right) \\
\end{align}
$$

###参考
https://khan.github.io/KaTeX/function-support.html
###加法原理
$$
N = m_1+m_2+\dots+m_n 
$$
###乘法原理
$$
N = m_1\times m_2\times \dots \times m_n 
$$
###排列
$$
P_n^m=n\cdot (n-1) \dots (n-m+1)    \text{ (1$\le$m$\le$n) }
$$
$n!$阶乘
$$
P_n=P_n^n=n\cdot (n-1) \dots 2 \cdot 1 = n!
$$
$$
P_n^m=\frac{n!}{(n-m)!}
$$
###组合
$$
C_n^m=\frac{n\cdot (n-1) \dots (n-m+1)}{m\cdot (m-1) \dots 2 \cdot 1} = \frac{P_n^m}{m!}
$$
$$
C_n^m=C_n^{n-m}
$$
###练习###
求方程式
$$
\frac{x-1}{1-\frac{x-1}{x}} = -\frac{1}{4}
$$
解:
$$
\begin{align}
\frac{x-1}{1-\frac{x-1}{x}} &= \frac{x-1}{\frac{x-x+1}{x}} \\
&= \frac{x-1}{\frac{1}{x}} \\
&= x(x-1) \\
&= -\frac{1}{4} \\
\end{align}
$$
$$
x^2-x+\frac{1}{4}=0 \\
(x-\frac{1}{2})^2=0 \\
x = \frac{1}{2}
$$
搞笑电影，证明
$$
1=2
$$
$$
\begin{align}
x^2-x^2 &= x(x-x)\\
&= (x-x)(x+x) \\
\implies \\
x(x-x) &= (x-x)(x+x) \\
x &= (x+x) \\
x &= 2x \\
1 &= 2
\end{align}
$$

$$
\{1,2,3,\cdots,9\}组成７个各位不相同的７位数
$$
###动态规划(DP)
分阶段求解决求解决策略问题的数学方法．
数学建模
1.最优子结构，解问题分解成若干个子问题;
2.边界值
3.数学公式
如
$$ f(n) =
\begin{cases}
1 & \text{if $n$ $\lt$  2 } \\
f(n-1) + f(n-2) & \text{if $n$ $\ge$  2}
\end{cases}
$$
金矿问题，N为工人数，W为金矿数，P(w)挖对应${1,2,\dots,W}$金矿需要的人数，G(w)挖对应${1,2,\dots,W}$每坐金矿的产量，F(N,W)Ｎ个工人为挖Ｗ个金矿

$$ 
F(N,W) = \max(F(N,W-1),F(N-P(W)) + G(W)) 
$$
$$
F(N,0) = 0
$$
$$
F(0,W) = 0
$$
$$
F(N,1) = G(1) \text{ n $\ge$ P(1)}
$$
$$
F(N,W) = F(N,W-1) \text{P(W) $\ge$ N}
$$
###余数
如果a和d是两个自然数，d非零，可以证明存在两个唯一的整数 q 和 r，满足 
$　a = qd + r $　且0 ≤ r < d