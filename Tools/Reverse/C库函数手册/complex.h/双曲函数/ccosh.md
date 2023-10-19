### 1.ccosh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    ccoshf( float complex z );
double complex   ccosh( double complex z );
```



#### 1.2. 功能描述

ccosh- 计算 z 的复双曲余弦。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = ccosh(1);  // 表现如沿实轴的 cosh
    printf("cosh(1+0i) = %f%+fi (cosh(1)=%f)\n", creal(z), cimag(z), cosh(1));
 
    double complex z2 = ccosh(I); // 表现如沿虚轴的实余弦
    printf("cosh(0+1i) = %f%+fi ( cos(1)=%f)\n", creal(z2), cimag(z2), cos(1));
}
```

运行结果：

```
cosh(1+0i) = 1.543081+0.000000i (cosh(1)=1.543081)
cosh(0+1i) = 0.540302+0.000000i ( cos(1)=0.540302)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
sin   -复数的正弦
sinh  -复数的双曲正弦
cosh  -复数的双曲余弦


#### 1.5. 函数返回值

若不出现错误，则返回 z 的复双曲余弦。


#### 1.6. 使用注意事项
双曲余弦在复平面上是整函数，而无分支切割。它相对于虚部是周期的，周期为 2πi 。