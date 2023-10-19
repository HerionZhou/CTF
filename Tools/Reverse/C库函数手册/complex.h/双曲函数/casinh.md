### 1.casinh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    casinhf( float complex z );
double complex   casinh( double complex z );
```



#### 1.2. 功能描述

ccosh- 计算 z 的复反双曲正弦，分支切割在沿虚轴的 [−i; +i] 区间外。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{
    double complex z = casinh(0+2*I);
    printf("casinh(+0+2i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = casinh(-conj(2*I)); // 或 C11 中的 casinh(CMPLX(-0.0, 2))
    printf("casinh(-0+2i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    // 对于任何 z ， asinh(z) = asin(iz)/i
    double complex z3 = casinh(1+2*I);
    printf("casinh(1+2i) = %f%+fi\n", creal(z3), cimag(z3));
    double complex z4 = casin((1+2*I)*I)/I;
    printf("casin(i * (1+2i))/i = %f%+fi\n", creal(z4), cimag(z4));
}
```

运行结果：

```
casinh(+0+2i) = 1.316958+1.570796i
casinh(-0+2i) (the other side of the cut) = -1.316958+1.570796i
casinh(1+2i) = 1.469352+1.063440i
casin(i * (1+2i))/i =  1.469352+1.063440i
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


#### 1.5. 函数返回值

若不出现错误，则返回 z 的复反双曲正弦，在沿实轴数学上无界，沿虚轴在区间 [−iπ/2; +iπ/2] 中的条状范围中。


#### 1.6. 使用注意事项
尽管 C 标准命名此函数为“复弧双曲正弦”函数，双曲函数的反函数仍是面积函数。其参数是双曲扇形的面积，而非弧长。正确的名称是“复反双曲正弦”或较不常用的“复面积双曲正弦”。

反双曲正弦是多值函数，而在复平面上要求分支切割。约定将分支置于虚轴的线段 (-i∞,-i) 和 (i,i∞) 上。