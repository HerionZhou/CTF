### 1. creal  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 李鹏威 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <complex.h>
double creal( double complex z );
```



#### 1.2. 功能描述

creal -返回z的实部
此函数对所有可能输入指明，而且不受制于任何描述于math_errhandling 的错误。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <complex.h>
 
int main(void)
{    
    double complex z = 1.0 + 2.0*I;
    printf("%f%+fi\n", creal(z), cimag(z));
}
```

运行结果：

```
1.000000+2.000000i
```







#### 1.4. 参数说明
z  -  复参数  。







#### 1.5. 函数返回值

z的实部 

此函数对所有可能输入指明，而且不受制于任何描述于 math_errhandling 的错误。


 





#### 1.6. 使用注意事项

对于任何复变量 z ， z == creal(z) + I*cimag(z) 。