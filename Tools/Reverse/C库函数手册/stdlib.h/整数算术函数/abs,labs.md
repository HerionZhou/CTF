# abs 函数使用说明

abs, labs, llabs, imaxabs - compute the absolute value of an integer



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.31   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

int abs(int j);
long int labs(long int j);
long long int llabs(long long int j);
```



### **功能描述**

C 库函数 `abs()` 用于对整数取绝对值。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int j = -1024;

    printf("j = %d, abs(j) = %d.\n", j, abs(j));
}
```

运行结果：

```
j = -1024, abs(j) = 1024.
```

通过运行结果，我们可以看到，通过调用 `abs()` 进行绝对值运算并输出。



### **函数返回值**

- 返回绝对值。







### **使用注意事项**

- 线程安全。

