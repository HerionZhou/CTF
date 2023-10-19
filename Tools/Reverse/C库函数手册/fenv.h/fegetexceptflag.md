# fegetexceptflag函数使用说明

| 文档版本 |          **作者**           |  修改日期  | **备注** |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.15 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int fegetexceptflag(fexcept_t *flagp, int excepts);
```

### 功能描述

该函数存储异常标志`exception flags`状态，它由参数`excepts`表示，在不透明对象`*flagp`中；其试图获得列于位掩码参数 `excepts` 的浮点异常标志的完整内容，它是**浮点异常宏**的逐位或。 

### 使用示例

```c
// file name : file_fegetexceptflag.c
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
    printf("\n");
}
 
int main(void)
{
    fexcept_t excepts;
 
    /* 设置“当前”异常标志集合。 */
    feraiseexcept(FE_INVALID);
    show_fe_exceptions();
 
    /* 保存当前异常标志。 */
    fegetexceptflag(&excepts,FE_ALL_EXCEPT);
 
    /* 临时引发二个其他异常。 */
    feclearexcept(FE_ALL_EXCEPT);
    feraiseexcept(FE_OVERFLOW | FE_INEXACT);
    show_fe_exceptions();
 
    /* 恢复先前的异常标志。 */
    fesetexceptflag(&excepts,FE_ALL_EXCEPT);
    show_fe_exceptions();
 
    return 0;
}
```

运行结果：

```
// 编译环境
Linux Ubuntu 5.0.0-37-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1) 
// 编译指令
gcc file_fegetexceptflag.c -o app -lm && ./app
```

### 参数说明

| flagp       | 指向将要存储或读取标志位置的 fexcept_t 对象的指针 |
| ----------- | ------------------------------------------------- |
| **excepts** | **列出要获取/设置的异常的位掩码**                 |

### 函数返回值

 成功时返回 0 ，否则返回非零。 

