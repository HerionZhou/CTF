### 1.csinh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    csinhf( float complex z );
double complex   csinh( double complex z );
```



#### 1.2. 功能描述

csinh- 计算 z 的复双曲正弦。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = csinh(1);  // 表现类似沿实轴的 sinh
    printf("sinh(1+0i) = %f%+fi (sinh(1)=%f)\n", creal(z), cimag(z), sinh(1));
 
    double complex z2 = csinh(I); // 表现类似沿虚轴的正弦
    printf("sinh(0+1i) = %f%+fi ( sin(1)=%f)\n", creal(z2), cimag(z2), sin(1));
}
```

运行结果：

```
sinh(1+0i) = 1.175201+0.000000i (sinh(1)=1.175201)
sinh(0+1i) = 0.000000+0.841471i ( sin(1)=0.841471)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
sin   -复数的正弦
sinh  -复数的双曲正弦



#### 1.5. 函数返回值

若不出现错误，则返回 z 的复双曲正弦。


#### 1.6. 使用注意事项
双曲正弦在复平面上是整函数而无分支切割。它相对于虚部是周期的，周期为 2πi 。
