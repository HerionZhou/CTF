# feclearexcept函数使用说明

| **文档版本** | **作者**                    | **修改日期** | **备注**       |
| ------------ | --------------------------- | ------------ | -------------- |
| V0.2         | [恒成立](1332417183@qq.com) | 2019.12.09   | 修改了部分内容 |
|              |                             |              |                |
|              |                             |              |                |

### **函数原型**

```c
#include <fenv.h>

int feclearexcept(int excepts); //(C99起)
```

### **功能描述**

 试图清除列于位掩码参数 `excepts` 的浮点异常，异常为**浮点异常宏**的逐位或。 

### **使用示例**

```c
// 文件名:file_feclearexcept.c
#include <fenv.h>
#include <stdio.h>
#include <math.h>
#include <float.h>
 
/*
 * 可能的hypot实现，它会活用许多高级浮点特性。
 */
double hypot_demo(double a, double b) {
  const int range_problem = FE_OVERFLOW | FE_UNDERFLOW;
  feclearexcept(range_problem);
  // 尝试快速算法
  double result = sqrt(a * a + b * b);
  if (!fetestexcept(range_problem))  // 未上溢或下溢
    return result;                   // 返回结果
  // 做更多复杂计算以避免上溢或下溢
  int a_exponent,b_exponent;
  frexp(a, &a_exponent);
  frexp(b, &b_exponent);
 
  if (a_exponent - b_exponent > DBL_MAX_EXP)
    return fabs(a) + fabs(b);        // 我们可以忽略小值
  // 令fabs(a)的规模接近1
  double a_scaled = scalbn(a, -a_exponent);
  double b_scaled = scalbn(b, -a_exponent);
  // 现在上溢和下溢是不可能的
  result = sqrt(a_scaled * a_scaled + b_scaled * b_scaled);
  // 撤销规模化
  return scalbn(result, a_exponent);
}
 
int main(void)
{
  // 通常情况选择较快的路线
  printf("hypot(%f, %f) = %f\n", 3.0, 4.0, hypot_demo(3.0, 4.0));
  // 极限情形会选择较慢但更准确的路线
  printf("hypot(%e, %e) = %e\n", DBL_MAX / 2.0, 
                                DBL_MAX / 2.0, 
                                hypot_demo(DBL_MAX / 2.0, DBL_MAX / 2.0));
 
  return 0;
}
```

运行结果：

```shell
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_feclearexcept.c -o app -lm && ./app
// 输出结果
hypot(3.000000, 4.000000) = 5.000000
hypot(8.988466e+307, 8.988466e+307) = 1.271161e+308
```

### **参数说明**

`excepts` -  列出要清理的异常标志的位掩码 

### **函数返回值**

 若成功清除所有指示的异常则或若 `excepts` 为零则为 0 。错误时返回非零值。 



