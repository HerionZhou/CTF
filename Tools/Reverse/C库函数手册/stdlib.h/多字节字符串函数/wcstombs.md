# wcstombs函数使用说明

> wcstombs - convert a wide-character string to a multibyte string
>



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2020.03.24   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <stdlib.h>

size_t wcstombs(char *dest, const wchar_t *src, size_t n);
```



### **功能描述**

C 库函数 `wcstombs()` 将指针 `const wchar_t *src` 指向的宽字符字符串转化为指针 `char *dest` 多字节字符串，转化字节个数由 `size_t n` 限定。





### **使用示例**

```c
暂无
```





### **函数返回值**

- 修改的数组元素的个数。







### **使用注意事项**

- 线程安全。

