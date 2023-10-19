### 1. cexp  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   cexpf( float complex z );
double complex  cexp( double complex z );
```



#### 1.2. 功能描述

cexp - 计算复数的底 e 指数。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double PI = acos(-1);
    double complex z = cexp(I * PI); // 欧拉公式
    printf("exp(i*pi) = %.1f%+.1fi\n", creal(z), cimag(z));
 
}
```

运行结果：

```
exp(i*pi) = -1.0+0.0i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值

若不出现错误，则返回 e 的 z 次幂， ez。


#### 1.6. 使用注意事项

复指数函数 ez对于自变量 z = x+iy 的值等于 excis(y) ，或 ex(cos(y) + i sin(y)) 。指数函数在复平面上是整函数且无分支切割。
若实现支持IEEE浮点算术，则

cexp(conj(z)) == conj(cexp(z))
若 z 为 ±0+0i ，则结果是1+0i；
若 z 为 x+∞i （对于任何有限 x），则结果是 NaN+NaNi并引发 FE_INVALID ；
若 z 为 x+NaNi （对于任何有限 x），则结果是 NaN+NaNi 并可能引发 FE_INVALID ；
若 z 为 +∞+0i ，则结果是+∞+0i；
若 z 为 -∞+yi （对任何有限 y），则结果是 +0cis(y) ；
若 z 为 +∞+yi （对于任何有限非零 y），则结果是 +∞cis(y) ；
若 z 为 -∞+∞i ，则结果是 ±0±0i （符号未指定）
若 z 为 +∞+∞i ，则结果是 ±∞+NaNi 并引发 FE_INVALID （实部符号未指定）；
若 z 为 -∞+NaNi ，则结果是 ±0±0i （符号未指定）；
若 z 为 +∞+NaNi ，则结果是 ±∞+NaNi （实部符号未指定）；
若 z 为 NaN+0i ，则结果是 NaN+0i ；
若 z 为 NaN+yi （对于任意非零 y ），则结果是 NaN+NaNi 并可能引发 FE_INVALID ；
若 z 为 NaN+NaNi ，则结果是 NaN+NaNi ；
其中 cis(y) 为 cos(y) + i sin(y) 。