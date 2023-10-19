### 1. casin  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   casinf( float complex z );
double complex  casin( double complex z );
```



#### 1.2. 功能描述

casin - 计算 z 的复弧（反）正弦，分支切割在沿实轴的 [−1,+1] 区间外。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = casin(-2);
    printf("casin(-2+0i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = casin(conj(-2)); // 或 CMPLX(-2, -0.0)
    printf("casin(-2-0i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    // 对于任何 z ， asin(z) = acos(-z) - pi/2
    double pi = acos(-1);
    double complex z3 = csin(cacos(conj(-2))-pi/2);
    printf("csin(cacos(-2-0i)-pi/2) = %f%+fi\n", creal(z3), cimag(z3));
}
```

运行结果：

```
casin(-2+0i) = -1.570796+1.316958i
casin(-2-0i) (the other side of the cut) = -1.570796-1.316958i
csin(cacos(-2-0i)-pi/2) = 2.000000+0.000000i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
casin   -复反正弦



#### 1.5. 函数返回值
若不出现错误，则返回 z 的复弧正弦，在沿虚轴无界，沿实轴在区间 [−π/2; +π/2] 中的条状范围中。

如同运算以 -I * casinh(I*z) 实现一般处理错误和特殊情况。

#### 1.6. 使用注意事项
反正弦（或弧正弦）是多值函数，且在复平面上要求分支切割。约定将分支切割置于实轴上的线段 (-∞,-1) 和 (1,∞) 上。
