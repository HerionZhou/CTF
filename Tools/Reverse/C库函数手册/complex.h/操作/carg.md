### 1. carg  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float  cargf( float complex z );
double carg( double complex z );
long double cargl( long double complex z );
```



#### 1.2. 功能描述

carg -计算复数的辐角（又称相位角），分支切割沿负实轴。




#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void) 
{
    double complex z1 = 1.0+0.0*I;
    printf("phase angle of %.1f%+.1fi is %f\n", creal(z1), cimag(z1), carg(z1));
 
    double complex z2 = 0.0+1.0*I;
    printf("phase angle of %.1f%+.1fi is %f\n", creal(z2), cimag(z2), carg(z2));
 
    double complex z3 = -1.0+0.0*I;
    printf("phase angle of %.1f%+.1fi is %f\n", creal(z3), cimag(z3), carg(z3));
 
    double complex z4 = conj(z3); // 或 CMPLX(-1, -0.0)
    printf("phase angle of %.1f%+.1fi (the other side of the cut) is %f\n",
             creal(z4), cimag(z4), carg(z4));
}
```

运行结果：

```
phase angle of 1.0+0.0i is 0.000000
phase angle of 0.0+1.0i is 1.570796
phase angle of -1.0+0.0i is 3.141593
phase angle of -1.0-0.0i (the other side of the cut) is -3.141593
```







#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
cabs -复数的模
carg -复数的辐角


#### 1.5. 函数返回值

若不出现错误，则返回 z 在 [−π; π] 区间中的相位角。 

如同函数实现为 atan2(cimag(z), creal(z)) 一般处理错误和特殊情况。




 





#### 1.6. 使用注意事项

对于任何复变量 z ， z == creal(z) + I*cimag(z) 。