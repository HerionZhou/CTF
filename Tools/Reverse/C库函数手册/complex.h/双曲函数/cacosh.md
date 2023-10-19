### 1.cacosh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    cacoshf( float complex z );
double complex   cacosh( double complex z );
```



#### 1.2. 功能描述

ccosh- 计算复数值 z 的复反双曲余弦，分支切割在沿实轴小于 1 的值上。


#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{
    double complex z = cacosh(0.5);
    printf("cacosh(+0.5+0i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = conj(0.5); // 或 C11 中的 cacosh(CMPLX(0.5, -0.0))
    printf("cacosh(+0.5-0i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    // 在上半平面， acosh(z) = i*acos(z) 
    double complex z3 = casinh(1+I);
    printf("casinh(1+1i) = %f%+fi\n", creal(z3), cimag(z3));
    double complex z4 = I*casin(1+I);
    printf("I*asin(1+1i) = %f%+fi\n", creal(z4), cimag(z4));
}
```

运行结果：

```
cacosh(+0.5+0i) = 0.000000-1.047198i
cacosh(+0.5-0i) (the other side of the cut) = 0.500000-0.000000i
casinh(1+1i) = 1.061275+0.666239i
I*asin(1+1i) = -1.061275+0.666239i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
sin   -复数的正弦
sinh  -复数的双曲正弦
cosh  -复数的双曲余弦
tanh  -复数的双曲正切
casin -复数的反双曲正弦
cacos -复数的反双曲余弦


#### 1.5. 函数返回值
z 的复反双曲余弦，沿实轴在区间 [0; ∞) 中，而沿虚轴在区间 [−iπ; +iπ] 中。


#### 1.6. 使用注意事项
尽管 C 标准命名此函数为“复弧双曲余弦”，双曲函数的反函数是面积函数。其参数为双曲扇形的面积，而非弧长。正确名称是“复反双曲余弦”，和更少见的“复面积双曲余弦”。

反双曲余弦是多值函数，在复平面上要求分支切割。约定将分支切割置于实轴的线段 (-∞,+1) 上。

复反双曲余弦主值的数学定义是 acosh z = ln(z + √z+1 √z-1) 。