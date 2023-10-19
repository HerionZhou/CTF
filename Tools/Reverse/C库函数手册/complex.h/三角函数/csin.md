### 1. csin  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   csinf( float complex z );
double complex  csin( double complex z );
```



#### 1.2. 功能描述

csin - 计算 z 的复正弦。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = csin(1);  // 表现如同沿着实轴的实数正弦
    printf("sin(1+0i) = %f%+fi ( sin(1)=%f)\n", creal(z), cimag(z), sin(1));
 
    double complex z2 = csin(I); // 表现如同沿着虚轴的sinh
    printf("sin(0+1i) = %f%+fi (sinh(1)=%f)\n", creal(z2), cimag(z2), sinh(1));
}
```

运行结果：

```
sin(1+0i) = 0.841471+0.000000i ( sin(1)=0.841471)
sin(0+1i) = 0.000000+1.175201i (sinh(1)=1.175201)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
sin   -复正弦



#### 1.5. 函数返回值
若无错误发生，则为 z 的复正弦。

错误和特殊情况的处理如同运算以 -I * csinh(I*z) 实现。

#### 1.6. 使用注意事项
正弦在复平面上是整函数，而且没有分支切割。