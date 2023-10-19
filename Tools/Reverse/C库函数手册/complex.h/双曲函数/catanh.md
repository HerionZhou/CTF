### 1.catanh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    catanhf( float complex z );
double complex   catanh( double complex z );
```



#### 1.2. 功能描述

ccosh- 计算 z 的复反双曲正切，其分支切割为沿实轴的 [−1; +1] 区间外部。


#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{
    double complex z = catanh(2);
    printf("catanh(+2+0i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = catanh(conj(2)); // 或 C11 中的 catanh(CMPLX(2, -0.0))
    printf("catanh(+2-0i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    // 对于任何 z ， atanh(z) = atan(iz)/i
    double complex z3 = catanh(1+2*I);
    printf("catanh(1+2i) = %f%+fi\n", creal(z3), cimag(z3));
    double complex z4 = catan((1+2*I)*I)/I;
    printf("catan(i * (1+2i))/i = %f%+fi\n", creal(z4), cimag(z4));
}
```

运行结果：

```
catanh(+2+0i) = 0.549306+1.570796i
catanh(+2-0i) (the other side of the cut) = 0.549306-1.570796i
catanh(1+2i) = 0.173287+1.178097i
catan(i * (1+2i))/i = 0.173287+1.178097i
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
catan -复数的反双曲正切


#### 1.5. 函数返回值
若不发生错误，则返回 z 的复反双曲正切，范围在数学上为沿着实轴无界的半条，沿着虚轴为区间 [−iπ/2; +iπ/2] 。


#### 1.6. 使用注意事项
尽管 C 标准命名此函数为“复弧双曲正切”，双曲函数的反函数却是面积函数。其参数是双曲扇形的面积，而非弧长。正确的名称是“复反双曲正切”，和较少见的“复面积双曲正切”。

反双曲正切是多值函数，并要求复平面上的分支切割。我们约定将分支切割置于实轴的划分线 (-∞,-1] 和 [+1,+∞) 。