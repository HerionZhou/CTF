## 1. 【$ sin $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double sin(double x);       	/* 正弦函数，求某个角的正弦值  */
```
&nbsp;
### 1.2. 功能描述
正弦函数，求某个角的正弦值。

在直角三角形 ABC 中（其中角 C 为 90°），角 A 的正弦就是它的对边长度和三角形斜边长度的比值，如下图所示，sinA = a / c。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200109124007109.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNzM5MzY0,size_16,color_FFFFFF,t_70#pic_center)

安利文章：《[为什么会有弧度制](https://www.matongxue.com/madocs/5/)》
&nbsp;
### 1.3. 使用示例
$sin$ 示例，求 30° 角的正弦值。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* sin */
#define PI 3.14159265
int main ()
{
    double param, result;
    param = 30.0;
    result = sin (param*PI/180);
    // 由于 sin() 函数的参数是弧度，所以在给函数传递参数前，需要先将 30° 转换为弧度值。1°=π/180
    printf ("The sine of %f degrees is %f.\n", param, result );
    return 0;
}
```

运行结果：

```c
The sine of 30.000000 degrees is 0.500000.
```
&nbsp;
### 1.4. 参数说明

 - x：角的弧度值，为 double 类型。

&nbsp;

### 1.5. 函数返回值

 - x： 弧度(制)的正弦值，为 double 类型。

&nbsp;

### 1.6. 使用注意事项

 - sin(弧度)，参数范围不限 。
 - 除了有 double sin(double) 对应 double 型数据；
 - 还有 float sinf(float) 对应 float 型数据；
 - 以及 long double sinl(long double) 对应 long double 型数据。

