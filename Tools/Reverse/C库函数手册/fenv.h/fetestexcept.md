# fetestexcept函数使用说明

| 文档版本 |            作者             |  修改日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.2   | [恒成立](1332417183@qq.com) | 2019.12.18 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int fetestexcept(int excepts);//(C99起)
```

### 功能描述

确定指定的浮点异常状态标志的当前设置。

### 使用示例

```c
// filename: file_fetestexcept.c
#include <stdio.h>
#include <math.h>
#include <fenv.h>
#include <float.h>
 
#pragma STDC FENV_ACCESS ON
 
void show_fe_exceptions(void)
{
    printf("current exceptions raised: ");
    if(fetestexcept(FE_DIVBYZERO))     printf(" FE_DIVBYZERO");
    if(fetestexcept(FE_INEXACT))       printf(" FE_INEXACT");
    if(fetestexcept(FE_INVALID))       printf(" FE_INVALID");
    if(fetestexcept(FE_OVERFLOW))      printf(" FE_OVERFLOW");
    if(fetestexcept(FE_UNDERFLOW))     printf(" FE_UNDERFLOW");
    if(fetestexcept(FE_ALL_EXCEPT)==0) printf(" none");
    printf("\n");
}
 
int main(void)
{
    /* 显示默认浮点标志集合。 */
    show_fe_exceptions();
 
    /* 进行一些引发浮点异常的计算。 */
    printf("1.0/0.0     = %f\n", 1.0/0.0);        /* FE_DIVBYZERO            */
    printf("1.0/10.0    = %f\n", 1.0/10.0);       /* FE_INEXACT              */
    printf("sqrt(-1)    = %f\n", sqrt(-1));       /* FE_INVALID              */
    printf("DBL_MAX*2.0 = %f\n", DBL_MAX*2.0);    /* FE_INEXACT FE_OVERFLOW  */
    printf("nextafter(DBL_MIN/pow(2.0,52),0.0) = %.1f\n",
           nextafter(DBL_MIN/pow(2.0,52),0.0));   /* FE_INEXACT FE_UNDERFLOW */
    show_fe_exceptions();
 
    return 0;
}
```

运行结果：

```shell
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_fetestexcept.c -o app -lm && ./app
// 输出结果
current exceptions raised:  none
1.0/0.0     = inf
1.0/10.0    = 0.100000
sqrt(-1)    = -nan
DBL_MAX*2.0 = inf
nextafter(DBL_MIN/pow(2.0,52),0.0) = 0.0
current exceptions raised:  FE_DIVBYZERO FE_INEXACT FE_INVALID FE_OVERFLOW FE_UNDERFLOW
```

### 参数说明

*`excepts`* : 列出待测试异常标志的位掩码 

### 函数返回值

如果成功，返回一个包含位或运算的浮点异常宏的当前对应的异常状态标志的位掩码设置。

 设置返回 0，如果没有引发的异常。 