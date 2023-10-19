### 1.cacos  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex    cacosf( float complex z );
double complex   cacos( double complex z );
```



#### 1.2. 功能描述

cacos- 计算 z 的复弧（反）余弦，分支切割在沿实轴的区间 [−1,+1] 外。

#### 1.3. 使用示例

```c
#include <stdio.h>
#include <math.h>
#include <complex.h>
 
int main(void)
{
    double complex z = cacos(-2);
    printf("cacos(-2+0i) = %f%+fi\n", creal(z), cimag(z));
 
    double complex z2 = cacos(conj(-2)); // 或 CMPLX(-2, -0.0)
    printf("cacos(-2-0i) (the other side of the cut) = %f%+fi\n", creal(z2), cimag(z2));
 
    // 对于任何 z ， acos(z) = pi - acos(-z)
    double pi = acos(-1);
    double complex z3 = ccos(pi-z2);
    printf("ccos(pi - cacos(-2-0i) = %f%+fi\n", creal(z3), cimag(z3));
}
```

运行结果：

```
cacos(-2+0i) = 3.141593-1.316958i
cacos(-2-0i) (the other side of the cut) = 3.141593+1.316958i
ccos(pi - cacos(-2-0i) = 2.000000+0.000000i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部
cacos -复数的反余弦



#### 1.5. 函数返回值

若不出现错误，则返回 z 的复弧（反）余弦，于沿实轴的范围 [0 ; ∞) 且于沿虚轴的范围 [−iπ ; iπ] 中。

#### 1.6. 使用注意事项
反余弦（或弧余弦）是多值函数，要求复平面上的分支切割。约定将分支切割置于实轴的线段 (-∞,-1) 和 (1,∞) 上。