## 1. 【$pow$】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double pow(double x,double y);       	/* 计算以x为底数的y次幂  */
```
&nbsp;
### 1.2. 功能描述
C语言的 pow() 函数用来求幂。

&nbsp;
### 1.3. 使用示例
$' pow '$ 示例，使用 pow() 函数求 3 的 2 次方，代码如下：

```c
#include <stdio.h>
#include <math.h>
int main() {
    double x = 3, y = 2;  //为变量赋初值
    double result = pow(x, y);  //求x的y次方
    printf("%lf\n", result);
    return 0;
}
```

运行结果：

```c
9.000000
```
&nbsp;
### 1.4. 参数说明

 - x：双精度数的底数。
 - y：双精度数的指数。

&nbsp;
### 1.5. 函数返回值
 - 返回：x 的 y 次方。
&nbsp;
### 1.6. 使用注意事项
pow函数的返回值为double双精度型，如果输出的值为整型的话是不可以的，必须用浮点数。

```c
printf("%d", pow(10.0, 2.0))
// 结果是一个不确定的值，应用对应的 %lf 或 %g 输出
// %g 会对比小数的十进制形式和指数形式，以最短的方式来输出小数，让输出结果更加简练。所谓最短，就是输出结果占用最少的字符。

printf("%d", (int)pow(10.0, 2.0))
// 以整型输出，不过将一个小数赋值给整数类型，就得把小数部分丢掉，只能取整数部分，这会改变数字本来的值。
// 注意是直接丢掉小数部分，而不是按照四舍五入取近似值。

printf("%d\n",(int)round(pow(10.0, 2.0)))
// 这才是四舍五入的写法。
```

总结：底数、指数用什么类型无关紧要，重要的是pow的返回值要赋给一个double型变量，不然会造成精度“失真”。

 - 除了有 double pow(double, double) 对应 double 型数据；
 - 还有 float powf(float, float) 对应 float 型数据；
 - 以及 long double powl(long double, long double) 对应 long double 型数据。

