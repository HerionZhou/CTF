### 1. catan  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   catanf( float complex z );
double complex  catan( double complex z );
```



#### 1.2. 功能描述

catan - 计算 z 的复弧（反）正切，分支切割在沿虚轴的 [−i,+i] 区间外。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <float.h>
#include <complex.h>
 
int main(void)
{
    double complex z = catan(2*I);
    printf("catan(+0+2i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = catan(-conj(2*I)); // 或 CMPLX(-0.0, 2)
    printf("catan(-0+2i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    double complex z3 = 2*catan(2*I*DBL_MAX); // 或 CMPLX(0, INFINITY)
    printf("2*catan(+0+i*Inf) = %f%+fi\n", creal(z3), cimag(z3));
}
```

运行结果：

```
catan(+0+2i) = 1.570796+0.549306i
catan(-0+2i) (the other side of the cut) = -1.570796+0.549306i
2*catan(+0+i*Inf) = 3.141593+0.000000i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
catan -复反正弦



#### 1.5. 函数返回值
若不发生错误，则返回 z 的复弧（反）正切，在沿虚轴无界，沿实轴在区间 [−π/2; +π/2] 内的条状范围中。

按照如同以 -I * catanh(I*z) 实现运算一般处理错误和特殊情况。

#### 1.6. 使用注意事项
反正切（或弧正切）是多值函数而要求复平面上的分支切割。约定分支切割置于虚轴的线段 (-∞i,-i) 和 (+i,+∞i) 上。