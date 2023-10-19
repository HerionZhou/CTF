### 1.ctanh  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.23 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    ctanhf( float complex z );
double complex   ctanh( double complex z );
```



#### 1.2. 功能描述

ccosh- 计算 z 的复双曲正切。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = ctanh(1);  // 表现类似沿实轴的 tanh
    printf("tanh(1+0i) = %f%+fi (tanh(1)=%f)\n", creal(z), cimag(z), tanh(1));
 
    double complex z2 = ctanh(I); // 表现类似沿虚轴的正切
    printf("tanh(0+1i) = %f%+fi ( tan(1)=%f)\n", creal(z2), cimag(z2), tan(1));
}
```

运行结果：

```
tanh(1+0i) = 0.761594+0.000000i (tanh(1)=0.761594)
tanh(0+1i) = 0.000000+1.557408i ( tan(1)=1.557408)
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
sin   -复数的正弦
sinh  -复数的双曲正弦
cosh  -复数的双曲余弦
tanh  -复数的双曲正切


#### 1.5. 函数返回值

若不出现错误，则返回 z 的复双曲正切。


#### 1.6. 使用注意事项
双曲正切是复平面上的解析函数且无分支切割。它对于虚部是周期的，周期为 πi ，而且沿虚轴有一阶极点，位于坐标 (0, π(1/2 + n)) 。然而无常用浮点表示能准确表示 π/2 ，故没有参数值能导致极点错误。