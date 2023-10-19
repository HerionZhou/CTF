## 1. 【$ atan2 $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double atan2(double y，double x);       	/* 反正切函数，atan() 的增强版，能确定象限  */
```
&nbsp;
### 1.2. 功能描述
atan2() 函数的功能是求 y/x 的反正切值。atan2() 是 atan() 的增强版，能够确定角度所在的象限。

反正切函数 atan2() 和正切函数 tan() 的功能恰好相反：tan() 是已知一个角的弧度值，求该角的正切值；而 atan2() 是已知一个角的正切值（也就是 y/x），求该角的弧度值。

&nbsp;
### 1.3. 使用示例
$ atan2 $ 示例，

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* atan2 */
#define PI 3.14159265
int main ()
{
    double x, y, result;
    x = -10.0;
    y = 10.0;
    result = atan2 (y,x) * 180 / PI;
    printf ("The arc tangent for (x=%f, y=%f) is %f degrees\n", x, y, result );
    return 0;
}
```

运行结果：

```c
The arc tangent for (x=-10.000000, y=10.000000) is 135.000000 degrees
```
&nbsp;
### 1.4. 参数说明
 - y：表示位于 Y 轴上的值，为 double 型。
 - x：表示位于 X 轴上的值，为 double 型。

注意，x 和 y 同时为 0 时将导致域错误（domain error），因为此时的角度是不存在的，或者说是没有意义的。

&nbsp;

### 1.5. 函数返回值
返回 y/x 的反正切值，以弧度表示，取值范围为(-π,π]。如上图所示，tan(θ) = y/x，θ = atan2(y, x)。

当 (x, y) 在象限中时：

 - 当 (x, y) 在第一象限，0 < θ < π/2 
 - 当 (x, y) 在第二象限，π/2 < θ ≤ π
 - 当 (x, y) 在第三象限，-π < θ < -π/2
 - 当 (x, y) 在第四象限，-π/2 < θ < 0

当 (x, y) 在象限的边界（也就是坐标轴）上时：

 - 当 y 是 0，且 x 为非负值，θ = 0
 - 当 y 是 0，且 x 是负值，θ = π
 - 当 y 是正值，且 x 是 0，θ = π/2
 - 当 y 是负值，且 x 是 0，θ = -π/2

由此可知，一般情况下用 atan() 即可，当对所求出角度的象限有特殊要求时，应使用 atan2()。
&nbsp;

### 1.6. 使用注意事项

 - atan2 (y,x)，x 和 y 同时为 0。
 - 除了有 double atan2(double, double) 对应 double 型数据；
 - 还有 float atan2f(float, float) 对应 float 型数据；
 - 以及 long double atan2l(long double, long double) 对应 long double 型数据。

