## 1. 【$ tan $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double tan(double x);       	/* 正切函数，求某个角的正切值 */
```
&nbsp;
### 1.2. 功能描述
tan() 函数的功能是求某个角的正切值。

在直角三角形 ABC 中（其中角 C 为 90°），角 A 的正切就是它的对边长度和临边长度的比值，如下图所示，tanA = a / b。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200109135501135.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNzM5MzY0,size_16,color_FFFFFF,t_70#pic_center)

安利文章：《[为什么会有弧度制](https://www.matongxue.com/madocs/5/)》
&nbsp;
### 1.3. 使用示例
$' tan '$ 示例，求 45° 角的正切值。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* tan */
#define PI 3.14159265
int main ()
{
    double param, result;
    param = 45.0;
    result = tan ( param * PI / 180.0 );
    // 由于 tan() 函数的参数是弧度，所以在给函数传递参数前，需要先将 45° 转换为弧度值。1°=π/180
    printf ("The tangent of %f degrees is %f.\n", param, result );
    return 0;
}
```

运行结果：

```c
The tangent of 45.000000 degrees is 1.000000.
```
&nbsp;
### 1.4. 参数说明

 - x：角的弧度值，为 double 类型。

&nbsp;

### 1.5. 函数返回值

 - x：弧度的正切值，为 double 类型。

&nbsp;

### 1.6. 使用注意事项

 - tan(弧度)，参数范围不限。
 - 除了有 double tan(double) 对应 double 型数据；
 - 还有 float tanf(float) 对应 float 型数据；
 - 以及 long double tanl(long double) 对应 long double 型数据。
