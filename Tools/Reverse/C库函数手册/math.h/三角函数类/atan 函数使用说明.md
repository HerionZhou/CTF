## 1. 【$ atan $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double atan(double x);       	/* 反正切函数，求反正切值  */
```
&nbsp;
### 1.2. 功能描述
atan() 函数的功能是求反正切值。

反正切函数 atan() 和正切函数 tan() 的功能正好相反。

tan() 是已知一个角的弧度值 x，求该角的正切值 y；而 atan() 是已知一个角的正切值 y，求该角的弧度值 x。
&nbsp;
### 1.3. 使用示例
$ atan $ 示例，求 1 的反正切值。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* atan */
#define PI 3.14159265
int main ()
{
    double param, result;
    param = 1.0;
    result = atan (param) * 180 / PI;  //将弧度转换为度
    printf ("The arc tangent of %f is %f degrees.\n", param, result );
    return 0;
}
```

运行结果：

```c
The arc tangent of 1.000000 is 45.000000 degrees.
```
&nbsp;
### 1.4. 参数说明

 - x：正切值。

&nbsp;

### 1.5. 函数返回值
正切值为 x 的角的度数，以弧度表示，取值区间为 (-π/2, π/2)。

注意：atan() 并不能确定角度所在的象限，例如求得的度数是 45°，并不能说明是第一象限的角度，还有可能是第三象限的角度。

如果想进一步确定角度所在的象限，请使用 atan2()。
&nbsp;

### 1.6. 使用注意事项

 - atan(正切值)，参数范围不限。
 - 除了有 double atan(double) 对应 double 型的数据；
 - 还有 float atanf(float) 对应 float 型的数据；
 - 以及 long double atanl(long double) 对应 long double 型的数据。

