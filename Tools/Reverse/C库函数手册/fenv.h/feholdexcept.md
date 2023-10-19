# feholdexcept函数使用说明

| 文档版本 |            作者             |  创建日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.22 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int feholdexcept(fenv_t *envp);//(C99起)
```

### 功能描述

- 首先，保存当前浮点环境到 `envp` 所指向的对象（类似 `fegetenv`)，然后清除所有浮点状态标志，再安装不停止模式：未来的浮点异常将不中断执行（不会陷落），直至以 `feupdateenv` 或 `fesetenv`还原浮点状态。

- 此函数可用于必须从调用方隐藏它可能引发的浮点异常的子程序的起始。若只是必须抑制某些异常而必须报告其他，则通常在清除不想要的异常后，通过调用 `feupdateenv` 结束不停止模式。

### 使用示例

```c
// filename : file_feholdexcept.c
#include <stdio.h>
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
 
double x2 (double x)   /* 乘二 */
{
    fenv_t curr_excepts;
 
    /* 保存并清除当前浮点异常。 */
    feholdexcept(&curr_excepts);
 
    /* 引发不准确和上溢异常。 */
    printf("In x2():  x = %f\n", x=x*2.0);
    show_fe_exceptions();
    feclearexcept(FE_INEXACT);   /* 从调用方隐藏不准确异常 */
 
    /* 将调用方的异常（ FE_INVALID ）并入剩下的 x2 的异常（ FE_OVERFLOW）。 */
    feupdateenv(&curr_excepts);
    return x;
}
 
int main(void)
{    
    feclearexcept(FE_ALL_EXCEPT);
    feraiseexcept(FE_INVALID);   /* 一些有非法参数的计算 */
    show_fe_exceptions();
    printf("x2(DBL_MAX) = %f\n", x2(DBL_MAX));
    show_fe_exceptions();
 
    return 0;
}
```

运行输出：

```
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_feholdexcept.c -o app -lm && ./app
// 输出结果
current exceptions raised:  FE_INVALID
In x2():  x = inf
current exceptions raised:  FE_INEXACT FE_OVERFLOW
x2(DBL_MAX) = inf
current exceptions raised:  FE_INVALID FE_OVERFLOW
```

### 参数说明

`envp` : 指向 fenv_t 类型对象的指针，将存储浮点环境于其中。

### 函数返回值

 成功时返回 0 ，否则返回非零。 



