### 1.ccos  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    ccosf( float complex z );
double complex   ccos( double complex z );
```



#### 1.2. 功能描述

ccos- 计算 z 的复余弦。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = ccos(1);  // 表现如同沿着实轴的实余弦
    printf("cos(1+0i) = %f%+fi ( cos(1)=%f)\n", creal(z), cimag(z), cos(1));
 
    double complex z2 = ccos(I); // 表现如同沿着虚轴的实 cosh
    printf("cos(0+1i) = %f%+fi (cosh(1)=%f)\n", creal(z2), cimag(z2), cosh(1));
}
```

运行结果：

```
cos(1+0i) = 0.540302-0.000000i ( cos(1)=0.540302)
cos(0+1i) = 1.543081-0.000000i (cosh(1)=1.543081)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
cos   -复数的余弦



#### 1.5. 函数返回值

若无错误发生，则返回 z 的复余弦。

错误和特殊情况如同操作以 ccosh(I*z) 实现一般。

#### 1.6. 使用注意事项
余弦在复平面上是整函数，而且无分支切割。