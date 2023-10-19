### 1. clog  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   clogf( float complex z );
double complex  clog( double complex z );
```



#### 1.2. 功能描述

clog- 计算 z 的复自然（底 e ）对数，分支切割沿负实轴.



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = clog(I); // r = 1, θ = pi/2
    printf("2*log(i) = %.1f%+fi\n", creal(2*z), cimag(2*z));
 
    double complex z2 = clog(sqrt(2)/2 + sqrt(2)/2*I); // r = 1, θ = pi/4
    printf("4*log(sqrt(2)/2+sqrt(2)i/2) = %.1f%+fi\n", creal(4*z2), cimag(4*z2));
 
    double complex z3 = clog(-1); // r = 1, θ = pi
    printf("log(-1+0i) = %.1f%+fi\n", creal(z3), cimag(z3));
 
    double complex z4 = clog(conj(-1)); // 或 C11 中的 clog(CMPLX(-1, -0.0))
    printf("log(-1-0i) (the other side of the cut) = %.1f%+fi\n", creal(z4), cimag(z4));
}
```

运行结果：

```
2*log(i) = 0.0+3.141593i
4*log(sqrt(2)/2+sqrt(2)i/2) = 0.0+3.141593i
log(-1+0i) = 0.0+3.141593i
log(-1-0i) (the other side of the cut) = 0.0-3.141593i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值

若不发生错误，则返回 z 的复自然对数，在沿虚轴为区间 [−iπ, +iπ] ，沿实轴为数学上无界的条状范围中。


#### 1.6. 使用注意事项
拥有极坐标表示 (r,θ) 的复数 z 的自然对数等于 ln r + i(θ+2nπ) ，其主值为 ln r + iθ 。

若实现支持 IEEE 浮点算术，则

考虑虚部符号，函数连续到分支切割上
clog(conj(z)) == conj(clog(z))
若 z 为 -0+0i ，则结果为 -∞+πi 并引发 FE_DIVBYZERO
若 z 为 +0+0i ，则结果为 -∞+0i 并引发 FE_DIVBYZERO
若 z 为 x+∞i （对于任何有限 x ），则结果为 +∞+πi/2
若 z 为 x+NaNi （对于任何有限 x ），则结果为 NaN+NaNi 并可能引发 FE_INVALID
若 z 为 -∞+yi （对于任何有限正 y ），则结果为 +∞+πi
若 z 为 +∞+yi （对于任何有限正 y ），则结果为 +∞+0i
若 z 为 -∞+∞i ，则结果为 +∞+3πi/4
若 z 为 +∞+∞i ，则结果为 +∞+πi/4
若 z 为 ±∞+NaNi ，则结果为 +∞+NaNi
若 z 为 NaN+yi （对于任何有限 y ），则结果为 NaN+NaNi 并可能引发 FE_INVALID
若 z 为 NaN+∞i ，则结果为 +∞+NaNi
若 z 为 NaN+NaNi ，则结果为 NaN+NaNi