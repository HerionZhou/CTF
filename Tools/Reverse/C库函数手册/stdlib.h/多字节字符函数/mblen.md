# mblen函数使用说明

> mblen - determine number of bytes in next multibyte character
>



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2020.03.24   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <stdlib.h>

int mblen(const char *s, size_t n);
```



### **功能描述**

C 库函数 `mblen()` 用于获得字符串 `*s` 中第一个字符（即该指针指向的字符）所包含的字节数，该多字节字符类型由`LC_CTYPE`决定，其判断最大值由参数 `size_t n` 决定。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
        char *s = "Test";
        int no = 0;

        no = mblen(s, MB_CUR_MAX);

        printf("%d\n", no);

        return 0;
}
```

运行结果：

```
1
```

- 通过运行结果，我们可以看到，通过调用 `mblen()` 判断该字符串中指针指向的单字符所占用的字节数大小。
- 在 Linux 环境下，使用命令 `locale` 可查看当前环境的 `LC_CTYPE` 值，一般为 `LC_CTYPE="C.UTF-8"` ,在 UTF-8 编码模式下，一个英文字符占用一个字节的存储空间，与上述结果相符。



### **函数返回值**

- 指针 `*s` 指向的单个字符所占存储空间的字节数。







### **使用注意事项**

- 线程安全。

