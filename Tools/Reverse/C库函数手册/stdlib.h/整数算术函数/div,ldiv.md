# div 函数使用说明

div, ldiv, lldiv, imaxdiv - compute the divolute value of an integer



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.31   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

div_t div(int numerator, int denominator);
ldiv_t ldiv(long numerator, long denominator);
lldiv_t lldiv(long long numerator, long long denominator);
```



### **功能描述**

C 库函数 `div()` 用于计算 `numerator` 除以 `denominator` 的商和余数。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int numerator = 1024;
    int denominator = 3;
    div_t qr = div(numerator, denominator);

    printf("quot = %d, rem = %d.\n", qr.quot, qr.rem);
}
```

运行结果：

```
quot = 341, rem = 1.
```

通过运行结果，我们可以看到，通过调用 `div()` 进行了商和余数的计算。



### **函数返回值**

- 返回值为结构体 `div_t`，该结构体包含成员 `int quot; int rem;` 分别表示商和余数。







### **使用注意事项**

- 线程安全。

