### 1. cpow  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.10 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float complex   cpowf( float complex x, float complex y );
double complex  cpow( double complex x, double complex y );
```



#### 1.2. 功能描述

cexp - 计算复幂函数 ，首参数的分支切割沿负实轴。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{    
    double complex z = cpow(1.0+2.0*I, 2);
    printf("(1+2i)^2 = %.1f%+.1fi\n", creal(z), cimag(z));
 
    double complex z2 = cpow(-1, 0.5);
    printf("(-1+0i)^0.5 = %.1f%+.1fi\n", creal(z2), cimag(z2));
 
    double complex z3 = cpow(conj(-1), 0.5); // 切割的另一侧
    printf("(-1-0i)^0.5 = %.1f%+.1fi\n", creal(z3), cimag(z3));
 
    double complex z4 = cpow(I, I); // i^i = exp(-pi/2)
    printf("i^i = %f%+fi\n", creal(z4), cimag(z4));
}
```

运行结果：

```
(1+2i)^2 = -3.0+4.0i
(-1+0i)^0.5 = 0.0+1.0i
(-1-0i)^0.5 = 0.0-1.0i
i^i = 0.207880+0.000000i
```


#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值
若不出现错误，则返回复幂Xy。

错误和特殊情况按照如同以 cexp(y*clog(x)) 实现运算一般处理，除了允许实现更细致地处理特殊情况。


#### 1.6. 使用注意事项
< 无 >