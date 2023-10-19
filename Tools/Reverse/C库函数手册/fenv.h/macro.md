# fenv.h中的所有MACRO定义

| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 恒成立   | 2019.12.09   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |

### **MACRO原型**

```c
#define FE_DIVBYZERO  /*implementation defined power of 2*/     (C99 起)
#define FE_INEXACT    /*implementation defined power of 2*/     (C99 起)
#define FE_INVALID    /*implementation defined power of 2*/     (C99 起)
#define FE_OVERFLOW   /*implementation defined power of 2*/     (C99 起)
#define FE_UNDERFLOW  /*implementation defined power of 2*/     (C99 起)
#define FE_ALL_EXCEPT FE_DIVBYZERO | FE_INEXACT | \
					  FE_INVALID   | FE_OVERFLOW| \				(C99 起)
					  FE_UNDERFLOW
```

```c
所有这些宏常量(除FE_ALL_EXCEPT)展成值为2的相异次幂整数常量表达式，唯一地鉴别所有受支持浮点异常。每个宏仅若受支持才得到定义。
宏常量FE_ALL_EXCEPT展开成所有其他FE_*的逐位或，且始终有定义，若实现不支持浮点异常，则为零。
```

### **MACRO解释**

|     常量      |                     定义                     |
| :-----------: | :------------------------------------------: |
| FE_DIVBYZERO  |         出现于之前浮点运算的极点错误         |
|  FE_INEXACT   | 不准确结果：必须舍入以存储之前浮点运算的结果 |
|  FE_INVALID   |        出现于之前浮点运算的定义域错误        |
|  FE_OVERFLOW  |       之前浮点运算的结果过大而无法表示       |
| FE_UNDERFLOW  |   之前浮点运算的结果为有精度损失的非正规值   |
| FE_ALL_EXCEPT |          所有受支持浮点异常的逐位或          |

### **参考案例**

```c
/**
 *  Filename : fe_macro.c
 *      Date : 2019/12/09
 */
#include <stdio.h>
#include <math.h>
#include <float.h>
#include <fenv.h>
 
#pragma STDC FENV_ACCESS ON
void show_fe_exceptions(void)
{
    printf("exceptions raised:");
    if(fetestexcept(FE_DIVBYZERO)) printf(" FE_DIVBYZERO");
    if(fetestexcept(FE_INEXACT))   printf(" FE_INEXACT");
    if(fetestexcept(FE_INVALID))   printf(" FE_INVALID");
    if(fetestexcept(FE_OVERFLOW))  printf(" FE_OVERFLOW");
    if(fetestexcept(FE_UNDERFLOW)) printf(" FE_UNDERFLOW");
    feclearexcept(FE_ALL_EXCEPT);
    printf("\n");
}
 
int main(void)
{
    printf("MATH_ERREXCEPT is %s\n",
           math_errhandling & MATH_ERREXCEPT ? "set" : "not set");
 
    printf("0.0/0.0 = %f\n", 0.0/0.0);
    show_fe_exceptions();
 
    printf("1.0/0.0 = %f\n", 1.0/0.0);
    show_fe_exceptions();
 
    printf("1.0/10.0 = %f\n", 1.0/10.0);
    show_fe_exceptions();
 
    printf("sqrt(-1) = %f\n", sqrt(-1));
    show_fe_exceptions();
 
    printf("DBL_MAX*2.0 = %f\n", DBL_MAX*2.0);
    show_fe_exceptions();
 
    printf("nextafter(DBL_MIN/pow(2.0,52),0.0) = %.1f\n",
                      nextafter(DBL_MIN/pow(2.0,52),0.0));
    show_fe_exceptions();
}
```

```shell
gcc fe_macro.c -o app -lm && ./app
```

输出结果：

```c
// 编译环境 gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
MATH_ERREXCEPT is set
0.0/0.0 = -nan
exceptions raised: FE_INVALID
1.0/0.0 = inf
exceptions raised: FE_DIVBYZERO
1.0/10.0 = 0.100000
exceptions raised:
sqrt(-1) = -nan
exceptions raised: FE_INVALID
DBL_MAX*2.0 = inf
exceptions raised: FE_INEXACT FE_OVERFLOW
nextafter(DBL_MIN/pow(2.0,52),0.0) = 0.0
exceptions raised: FE_INEXACT FE_UNDERFLOW
```

