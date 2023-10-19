### 1.ctan  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    ctanf( float complex z );
double complex   ctan( double complex z );
```



#### 1.2. 功能描述

ctan- 计算 z 的复正切。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = ctan(1);  // 表现类似沿实轴的实正切
    printf("tan(1+0i) = %f%+fi ( tan(1)=%f)\n", creal(z), cimag(z), tan(1));
 
    double complex z2 = ctan(I); // 表现类似沿虚轴的 tanh
    printf("tan(0+1i) = %f%+fi (tanh(1)=%f)\n", creal(z2), cimag(z2), tanh(1));
}
```

运行结果：

```
tan(1+0i) = 1.557408+0.000000i ( tan(1)=1.557408)
tan(0+1i) = 0.000000+0.761594i (tanh(1)=0.761594)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
tan   -复数的正切



#### 1.5. 函数返回值

若无错误发生，则返回 z 的复正切。

错误和特殊情况如同运算实现为 -i * ctanh(i*z) 一般处理，其中 i 是虚数单位。

#### 1.6. 使用注意事项
正切是复平面上的解析函数，而无分支切割。它对于实部是周期的，周期为 πi ，而且沿实轴有一阶极点，位于坐标 (π(1/2 + n), 0) 。然而无常用浮点表示能准确表示 π/2 ，故而没有值使得极点错误出现。