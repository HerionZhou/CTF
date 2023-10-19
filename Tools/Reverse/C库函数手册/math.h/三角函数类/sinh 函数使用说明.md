## 1. 【$ sinh $】函数使用说明
定义于头文件 $'math.h'$

| 文档作者 | 作者 | 修改日期 | 备注|
|:--------:| -------------:|-------------:|-------------:|
| v0.1 | [Debroon](https://blog.csdn.net/qq_41739364) |1| |！

### 1.1 函数原型

```c
double sinh(double x);				/* 双曲正弦 */
```
&nbsp;
### 1.2. 功能描述
sinh( ) 函数的功能是求 x的双曲正弦。
&nbsp;
### 1.3. 使用示例
$ sinh $ 示例，

```c
#include <stdio.h> 
#include <math.h> 
int main () 
{ 
	double x, ret; x = 0.5; 
	ret = sinh(x); 
	printf("The hyperbolic sine of %lf is %lf degrees", x, ret); 
	return(0); 
}
```

运行结果：

```c
The hyperboloc sine of 0.500000 is 0.521095 degrees
```
&nbsp;
### 1.4. 参数说明

 - x：任意实数，为 double 型。

&nbsp;

### 1.5. 函数返回值
返回 x 的双曲正弦。
&nbsp;

### 1.6. 使用注意事项

 - sinh(任意实数)，参数范围不限。
 - 除了有 double sinh(double) 对应 double 型数据；
 - 还有 float sinhf(float) 对应 float 型数据；
 - 以及 long double sinhl(long double) 对应 long double 型数据。

