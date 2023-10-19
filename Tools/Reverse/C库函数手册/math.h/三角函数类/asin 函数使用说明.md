## 1. 【$ asin $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double asin(double x);       	/* asin() 函数的功能是求反正弦值。  */
```
&nbsp;
### 1.2. 功能描述
反正弦函数 asin() 和正弦函数 sin() 的功能正好相反：sin() 是已知一个角的弧度值 x，求该角的正弦值 y；而 asin() 是已知一个角的正弦值 y，求该角的弧度值 x。

&nbsp;
### 1.3. 使用示例
$' asin '$ 示例，求 0.5 的反正弦值。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* asin */
#define PI 3.14159265
int main ()
{
    double param, result;
    param = 0.5;
    result = asin (param) * 180.0 / PI; //将弧度转换为度
    printf ("The arc sine of %f is %f degrees\n", param, result);
    return 0;
}
```

运行结果：

```c
The arc sine of 0.500000 is 30.000000 degrees
```
&nbsp;
### 1.4. 参数说明

 - 正弦值x，x 的取值必须位于区间 [-1, 1] 中，如果 x 的值超出此区间，将会产生**域错误**（domain error）。

在 <math.h> 头文件中，某些函数仅针对一定范围内的数值有意义，我们称这个范围为**域**（domain）。例如，sqrt() 函数仅能对非负数求平方根，所以此函数的域就为非负数。

如果我们给这类函数传递一个在域范围之外的参数，函数就会产生错误，我们称这种错误为**域错误**（domain error）。

当发生域错误时，这些函数就会将返回值设置为 **NaN**，表示返回值无效。想进一步了解域错误。

**NaN**（Not a Number）表示一个无效的数字，或者该数字未经初始化。NaN 是针对浮点数而言的，不适用于整数。

C99 标准新增加了 6 个头文件，其中的 <fenv.h> 专门用来处理浮点数错误，域错误也可以借助其中的 fetestexcept() 函数和 FE_INVALID 宏检测出来。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* asin */
#include <fenv.h>  /* FE_INVALID */
#define PI 3.14159265
int main()
{
    double result = asin(2) * 180.0 / PI;
    printf("result is :%f\n", result);
    if (fetestexcept(FE_INVALID)) {
        printf("FE_INVALID is set\n");
    }
    return 0;
}
```
GCC下运行结果：
```c
result is :nan		// 不同的编译器对 NaN 的输出不同
FE_INVALID is set
```

&nbsp;

### 1.5. 函数返回值
正常情况下（x 的取值位于区间[-1, 1]），函数返回正弦值为 x 的角的弧度数。

如果 x 的取值超出范围，那么 asin() 将发生域错误，此时返回值为 NaN。
&nbsp;

### 1.6. 使用注意事项

 - asin(正弦值)，参数范围：[-1, 1]。
 - 除了有 double asin(double) 对应 double 类型数据；
 - 还有 float asinf(float) 对应 float 类型数据；
 - 以及 long double asinl(long double) 对应 long double 类型数据。

