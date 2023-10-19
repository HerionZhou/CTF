## 1. 【$ acos $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double acos(double x);      	/* 反余弦函数，求反余弦值  */
```
&nbsp;
### 1.2. 功能描述
acos() 函数的功能是求反余弦值。

反余弦函数 acos() 和余弦函数 cos() 的功能恰好相反：cos() 是已知一个角的弧度值 x，求该角的余弦值 y；而 acos() 是已知一个角的余弦值 y，求该角的弧度值 x。
&nbsp;
### 1.3. 使用示例
$ acos $ 示例，求 0.5 的反余弦值。

```c
#include <stdio.h>      /* printf */
#include <math.h>       /* acos */
#define PI 3.14159265
int main ()
{
    double param, result;
    param = 0.5;
    result = acos (param) * 180.0 / PI;  // 将弧度转换为度
    printf ("The arc cosine of %f is %f degrees.\n", param, result);
    return 0;
}
```

运行结果：

```c
The arc cosine of 0.500000 is 60.000000 degrees.
```
&nbsp;
### 1.4. 参数说明
余弦值。x 的取值必须位于区间 [-1, 1] 中，如果 x 的值超出此区间，将会产生域错误（domain error）。

具体记录在 [asin 函数](https://gitee.com/zhaixuebuluo/glibc_man_cn/blob/master/math.h/%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0%E7%B1%BB/asin%20%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)。
&nbsp;

### 1.5. 函数返回值
正常情况下（x 的取值位于区间[-1, 1]），函数返回余弦值为 x 的角的弧度数。

如果 x 的取值超出范围，那么 acos() 将发生域错误，此时返回值为 NaN。

&nbsp;

### 1.6. 使用注意事项

 - acos(余弦值)，范围在：[-1, 1] 。
 - 除了有 double acos(double) 对应 double 型数据；
 - 还有 float acosf(float) 对应 float 型数据；
 - 以及 long double acosl(long double) 对应 long double 型数据。

