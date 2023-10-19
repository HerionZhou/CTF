# feraiseexcept函数使用说明

| 文档版本 |            作者             |  修改日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.16 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int feraiseexcept(int excepts);//(C99起)
```

### 功能描述

feraiseexcept()函数引起所支持的异常，该异常由异常中的位表示。

 尝试引发所有列于 `excepts` 浮点异常宏的逐位或的浮点异常。若异常之一为 `FE_OVERFLOW`或 `FE_UNDERFLOW `，则此函数可以额外引发 `FE_INEXACT` 。异常的引发顺序未指定，除了 `FE_OVERFLOW`和 `FE_UNDERFLOW`一定先于 `FE_INEXACT` 引发。 

### 使用示例

```c
// file_feraiseexcept.c
#include <stdio.h>
#include <fenv.h>
 
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
    feclearexcept(FE_ALL_EXCEPT);
    printf("\n");
}
 
double some_computation(void)
{
    /* 计算达到引发上溢的状态。 */
    int r = feraiseexcept(FE_OVERFLOW | FE_INEXACT);
    printf("feraiseexcept() %s\n", (r?"fails":"succeeds"));
    return 0.0;
}
 
int main(void)
{
    some_computation();
    show_fe_exceptions();
 
    return 0;
}
```

运行结果：

```
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_feraiseexcept.c -o app -lm && ./app
// 输出结果
feraiseexcept() succeeds
current exceptions raised:  FE_INEXACT FE_OVERFLOW
```

### 参数说明

`excepts` :列出所有要引发的异常标志的位掩码

### 函数返回值

 若引发了所有列出的异常，则返回 0 ，否则返回非零值。 







