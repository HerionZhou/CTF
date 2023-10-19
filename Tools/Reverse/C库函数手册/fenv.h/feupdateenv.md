# feupdateenv函数使用说明

| 文档信息 |            作者             |  创建日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.23 | 创建文本 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int feupdateenv(const fenv_t *envp);//(C99起)
```

### 功能描述

- 首先，回忆当前引发的浮点异常，然后从 `envp` 所指向的对象恢复浮点环境（类似 `fesetenv` ），再引发保存的浮点异常。

- 此函数可用于结束先前调用 `feholdexcept` 建立的不停止模式。

### **使用示例**

```c
// filename : file_feupdateenv.c
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
 
    /* 保存并清理当前浮点环境。 */
    feholdexcept(&curr_excepts);
 
    /* 引发不准确和溢出异常。 */
    printf("In x2():  x = %f\n", x=x*2.0);
    show_fe_exceptions();
    feclearexcept(FE_INEXACT);   /* 从调用方隐藏不准确异常 */
 
    /* 将调用方的异常（FE_INVALID）并入        */
    /* 剩下的x2的异常（FE_OVERFLOW）。 */
    feupdateenv(&curr_excepts);
    return x;
}
 
int main(void)
{    
    feclearexcept(FE_ALL_EXCEPT);
    feraiseexcept(FE_INVALID);   /* 一些带有非法参数的计算 */
    show_fe_exceptions();
    printf("x2(DBL_MAX) = %f\n", x2(DBL_MAX));
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
gcc file_feupdateenv.c -o app -lm && ./app
// 输出结果
current exceptions raised:  FE_INVALID
In x2():  x = inf
current exceptions raised:  FE_INEXACT FE_OVERFLOW
x2(DBL_MAX) = inf
current exceptions raised:  FE_INVALID FE_OVERFLOW
```

### 参数说明

`envp` : 指向 fenv_t 类型对象的指针，对象为之前到 feholdexcept 或 fegetenv 的调用所设，或等于 FE_DFL_ENV。

### 函数返回值

 成功时为 0 ，否则为非零。 



