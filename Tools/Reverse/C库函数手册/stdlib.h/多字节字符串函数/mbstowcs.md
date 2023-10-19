# mbstowcs函数使用说明

> mbstowcs - convert a multibyte string to a wide-character string
>



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2020.03.24   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <stdlib.h>

size_t mbstowcs(wchar_t *dest, const char *src, size_t n);
```



### **功能描述**

C 库函数 `mbstowcs()` 将指针 `const char *src` 指向的多字节字符串转化为指针 `wchar_t *dest` 指向的宽字节字符串，转化字节个数由 `size_t n` 限定。





### **使用示例**

```c
暂无
```





### **函数返回值**

- 修改的数组元素的个数。







### **使用注意事项**

- 线程安全。

