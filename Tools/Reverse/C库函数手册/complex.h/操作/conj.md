### 1. cong  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float  conjf( float complex z );
double conj( double complex z );
```



#### 1.2. 功能描述

conj - 通过反转虚部的符号计算复数的共轭复数.



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{
    double complex z = 1.0 + 2.0*I;
    double complex z2 = conj(z);
    printf("The conjugate of %.1f%+.1fi is %.1f%+.1fi\n",
            creal(z), cimag(z), creal(z2), cimag(z2));
 
    printf("Their product is %.1f%+.1fi\n", creal(z*z2), cimag(z*z2));
}
```

运行结果：

```
The conjugate of 1.0+2.0i is 1.0-2.0i
Their product is 5.0+0.0i
```







#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值

z 的共轭复数


#### 1.6. 使用注意事项

在不实现 I 为 _Imaginary_I 的 C99 实现上，可用 conj 获得拥有负零虚部的复数。 C11 中，宏 CMPLX 用于此目的。