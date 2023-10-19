# iswdigit 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 王利涛   | 2020.01.03   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <wctype.h>
int iswdigit(wint_t wc);
```



### **功能描述**

判断一个宽字符是否是数字。



### **参数说明**

参数wc表示宽字符



### **函数返回值**

- 如果 wc 是字符集中的数字，返回一个非零值
- 如果不是的话，函数返回0



### **使用示例**

定义一个宽字符串，然后去判断这个字符串中有多少个字母：

```c
#include <stdio.h>
#include <wctype.h>
#include <wchar.h>
#include <locale.h>

void is_digit (wchar_t wc)
{
    if (iswdigit (wc))
        wprintf (L"%lc is a digit\n", wc);
    else
        wprintf (L"%lc is not a digit\n", wc);

}

int main (void)
{
    wchar_t wc1 = L'2';
    wchar_t wc2 = L'a';
     
    is_digit (wc1);
    is_digit (wc2);

    return 0;
}
```

运行结果：

```
2 is a digit
a is not a digit
```

这个函数使用的时候，运行结果跟本地操作系统、中英文环境相关，如果本地是英文环境，遇到全角数字字符时，可能不认为是个字母，我们可以使用 setlocale 设定本地化环境，识别全角数字字符。

宽字符一般是双字节存储的，打印宽字符一般使用wprintf函数，占位符使用 “ls”，在定义宽字符时，要在字符或字符串的前面加一个L，表示宽字符、双字节存储。
