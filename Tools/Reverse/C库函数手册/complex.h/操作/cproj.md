### 1. cproj  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
float  cprojf( float complex z );
double cproj( double complex z );
```



#### 1.2. 功能描述

cproj - 计算复数在黎曼球面上的投影.



#### 1.3. 使用示例

```c

运行此代码


#include <stdio.h>
#include <complex.h>
#include <math.h>
 
int main(void)
{
    double complex z1 = cproj(1 + 2*I);
    printf("cproj(1+2i) = %.1f%+.1fi\n", creal(z1),cimag(z1));
 
    double complex z2 = cproj(INFINITY+2.0*I);
    printf("cproj(Inf+2i) = %.1f%+.1fi\n", creal(z2),cimag(z2));
 
    double complex z3 = cproj(INFINITY-2.0*I);
    printf("cproj(Inf-2i) = %.1f%+.1fi\n", creal(z3),cimag(z3));
}

```

运行结果：

```
cproj(1+2i) = 1.0+2.0i
cproj(Inf+2i) = inf+0.0i
cproj(Inf-2i) = inf-0.0i
```







#### 1.4. 参数说明
z  -  复参数
creal -复数的实部
cimag -复数的虚部



#### 1.5. 函数返回值
z 在黎曼球面上的投影。 

此函数为所有可行输入完整指定，并且不受制于任何描述于 math_errhandling 的错误。 



#### 1.6. 使用注意事项
cproj 函数通过将所有无穷大映射到一（给出或采用虚部零的符号），帮助用户模拟黎曼球面，而且它应该在任何操作，特别是比较之前使用，比较可能对任何其他无穷大给出虚假结果。