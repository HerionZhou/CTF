# fegetenv函数使用说明

| 文档帮助 |            作者             |  创建日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.21 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int fegetenv(fenv_t *envp);//(C99起)
```

### 功能描述

-  试图存储浮点环境的状态于 `envp` 所指向的对象。

-  试图从 `envp` 所指向的对象建立浮点环境状态。对象的值必须是以先前调用 `feholdexcept` 或 `fegetenv` 获得 值或是浮点宏常量。若 `envp` 中设置了任何浮点状态标志，则环境中标志变为被设置（然后可用 `fetestexcept`  测试），但不引发对应的浮点异常（执行持续而不中断）。

### **使用示例**

```c
// filename : file_fegetenv.c
#include <stdio.h>
#include <math.h>
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
    printf("\n");
}
 
void show_fe_rounding_method(void)
{
    printf("current rounding method:    ");
    switch (fegetround()) {
           case FE_TONEAREST:  printf ("FE_TONEAREST");  break;
           case FE_DOWNWARD:   printf ("FE_DOWNWARD");   break;
           case FE_UPWARD:     printf ("FE_UPWARD");     break;
           case FE_TOWARDZERO: printf ("FE_TOWARDZERO"); break;
           default:            printf ("unknown");
    };
    printf("\n");
}
 
void show_fe_environment(void)
{
    show_fe_exceptions();
    show_fe_rounding_method();
}    
 
int main(void)
{
    fenv_t curr_env;
    int rtn;
 
    /* 显示默认环境。 */
    show_fe_environment();
    printf("\n");
 
    /* 在默认环境下做一些计算。 */
    printf("+11.5 -> %+4.1f\n", rint(+11.5)); /* 两整数的中央值 */
    printf("+12.5 -> %+4.1f\n", rint(+12.5)); /* 两整数的中央值 */
    show_fe_environment();
    printf("\n");
 
    /* 保存当前环境。 */
    rtn = fegetenv(&curr_env);
 
    /* 以新舍入方法进行一些计算。 */
    feclearexcept(FE_ALL_EXCEPT);
    fesetround(FE_DOWNWARD);
    printf("1.0/0.0 = %f\n", 1.0/0.0);
    printf("+11.5 -> %+4.1f\n", rint(+11.5));
    printf("+12.5 -> %+4.1f\n", rint(+12.5));
    show_fe_environment();
    printf("\n");
 
    /* 恢复先前环境。 */
    rtn = fesetenv(&curr_env);
    show_fe_environment();
 
    return 0;
}
```

输出结果:

```shell
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_fegetenv.c -o app -lm && ./app
// 输出结果
current exceptions raised:  none
current rounding method:    FE_TONEAREST

+11.5 -> +12.0
+12.5 -> +12.0
current exceptions raised:  FE_INEXACT
current rounding method:    FE_TONEAREST

1.0/0.0 = inf
+11.5 -> +11.0
+12.5 -> +12.0
current exceptions raised:  FE_DIVBYZERO FE_INEXACT
current rounding method:    FE_DOWNWARD

current exceptions raised:  FE_INEXACT
current rounding method:    FE_TONEAREST
```



### **参数说明**

`envp` : 指向 fenv_t 类型对象的指针，该对象保有浮点环境的状态。

### 函数返回值

成功时返回 0 ，否则返回非零。







