### 1. csqrt  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   csqrtf( float complex z );
double complex  csqrt( double complex z );
```



#### 1.2. 功能描述

csqrt- 计算 z 的复平方根，分支切割沿负实轴。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{
    double complex z1 = csqrt(-4);
    printf("Square root of -4 is %.1f%+.1fi\n", creal(z1), cimag(z1));
 
    double complex z2 = csqrt(conj(-4)); // 或 C11 中的 CMPLX(-4, -0.0)
    printf("Square root of -4-0i, the other side of the cut, is "
           "%.1f%+.1fi\n", creal(z2), cimag(z2));
}
```

运行结果：

```
Square root of -4 is 0.0+2.0i
Square root of -4-0i, the other side of the cut, is 0.0-2.0i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值

若不出现错误，则返回 z 的平方根，在包含虚轴的右半平面中（沿实轴为 [0; +∞) ，而沿虚轴为 (−∞; +∞) ）。

#### 1.6. 使用注意事项
报告的错误与 math_errhandling 一致。

若实现支持 IEEE 浮点算术，则

考虑虚部符号，函数连续到分支切割上。
csqrt(conj(z)) == conj(csqrt(z))
若 z 为 ±0+0i ，则结果为 +0+0i
若 z 为 x+∞i ，则结果为 +∞+∞i ，即使 x 为 NaN
若 z 为 x+NaNi ，则结果为 NaN+NaNi （除非 x 为 ±∞ ）并可能引发 FE_INVALID
若 z 为 -∞+yi ，则对于有限正 y 结果为 +0+∞i
若 z 为 +∞+yi ，则对于有限正 y 结果为 +∞+0i)
若 z 为 -∞+NaNi ，则结果为 NaN±∞i （虚部符号未指定）
若 z 为 +∞+NaNi ，则结果为 +∞+NaNi
若 z 为 NaN+yi ，则结果为 NaN+NaNi 并可能引发 FE_INVALID
若 z 为 NaN+NaNi ，则结果为 NaN+NaNi