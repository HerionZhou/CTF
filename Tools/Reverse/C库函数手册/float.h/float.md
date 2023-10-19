# float.h文档说明

| 文档版本 |            作者             |  创建日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.29 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 功能描述

 C 标准库的 `float.h`头文件包含了一组与浮点值相关的依赖于平台的常量。这些常量是由 `ANSI` `C` 提出的，这让程序更具有可移植性。在讲解这些常量之前，最好先弄清楚浮点数是由下面四个元素组成的： 

| 组件 | 组件描述                                                     |
| :--- | :----------------------------------------------------------- |
| S    | 符号 ( +/- )                                                 |
| b    | 指数表示的基数，2 表示二进制，10 表示十进制，16 表示十六进制，等等... |
| e    | 指数，一个介于最小值 **emin** 和最大值 **emax** 之间的整数。 |
| p    | 精度，基数 b 的有效位数                                      |

基于以上 4 个组成部分，一个浮点数的值如下：

**floating-point = ( S ) p x be**

或

**floating-point = (+/-) precision x baseexponent**

## 库宏

下面的值是特定实现的，且是通过 #define 指令来定义的，这些值都不得低于下边所给出的值。请注意，所有的实例 FLT 是指类型 float，DBL 是指类型 double，LDBL 是指类型 long double。

| 宏                                                      | 描述                                                         |
| :------------------------------------------------------ | :----------------------------------------------------------- |
| FLT_ROUNDS                                              | 定义浮点加法的舍入模式，它可以是下列任何一个值：-1 - 无法确定0 - 趋向于零1 - 去最近的值2 - 趋向于正无穷3 - 趋向于负无穷 |
| FLT_RADIX 2                                             | 这个宏定义了指数表示的基数。基数 2 表示二进制，基数 10 表示十进制，基数 16 表示十六进制。 |
| FLT_MANT_DIGDBL_MANT_DIGLDBL_MANT_DIG                   | 这些宏定义了 FLT_RADIX 基数中的位数。                        |
| FLT_DIG 6DBL_DIG 10LDBL_DIG 10                          | 这些宏定义了舍入后不会改变表示的十进制数字的最大值（基数 10）。 |
| FLT_MIN_EXPDBL_MIN_EXPLDBL_MIN_EXP                      | 这些宏定义了基数为 FLT_RADIX 时的指数的最小负整数值。        |
| FLT_MIN_10_EXP -37DBL_MIN_10_EXP -37LDBL_MIN_10_EXP -37 | 这些宏定义了基数为 10 时的指数的最小负整数值。               |
| FLT_MAX_EXPDBL_MAX_EXPLDBL_MAX_EXP                      | 这些宏定义了基数为 FLT_RADIX 时的指数的最大整数值。          |
| FLT_MAX_10_EXP +37DBL_MAX_10_EXP +37LDBL_MAX_10_EXP +37 | 这些宏定义了基数为 10 时的指数的最大整数值。                 |
| FLT_MAX 1E+37DBL_MAX 1E+37LDBL_MAX 1E+37                | 这些宏定义最大的有限浮点值。                                 |
| FLT_EPSILON 1E-5DBL_EPSILON 1E-9LDBL_EPSILON 1E-9       | 这些宏定义了可表示的最小有效数字。                           |
| FLT_MIN 1E-37DBL_MIN 1E-37LDBL_MIN 1E-37                | 这些宏定义了最小的浮点值。                                   |

### 使用示例

下面的实例演示了 float.h 文件中定义的一些常量的使用。

```c
// filename : file_float.c
#include <stdio.h>
#include <float.h>

int main()
{
   printf("The maximum value of float = %.10e\n", FLT_MAX);
   printf("The minimum value of float = %.10e\n", FLT_MIN);

   printf("The number of digits in the number = %.10e\n", FLT_MANT_DIG);
}
```

输出结果 : 

```
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_float.c -o app -lm && ./app
// 输出结果
The maximum value of float = 3.4028234664e+38
The minimum value of float = 1.1754943508e-38
The number of digits in the number = 7.2996655210e-312
```



