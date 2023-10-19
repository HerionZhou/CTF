# iswalnum 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 王利涛   | 2020.01.03   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <wctype.h>
int iswalnum (wint_t wc);
```



### **功能描述**

判断一个宽字符是否是数字、字母（大写字母或小写字母）或基于当前本地语言环境的数字、字母（如阿拉伯字母等）。



### **参数说明**

参数wc表示宽字符



### **函数返回值**

- 如果 wc 是数字或字母，返回一个非零值
- 如果不是的话，函数返回0



### **使用示例**

定义一个宽字符串，然后去判断这个字符串中有多少个字母：

```c
#include <stdio.h>
#include <wctype.h>
#include <wchar.h>
#include <locale.h>

void is_alnum (wchar_t wc)
{
    if (iswalnum (wc))
        wprintf (L"%lc is a alnum\n", wc);
    else
        wprintf (L"%lc is not a alnum\n", wc);

}

int main (void)
{
    wchar_t wc1 = L'2';
    wchar_t wc2 = L'a';
    wchar_t wc3 = L'宅';
     
    is_alnum (wc1);
    is_alnum (wc2);
    is_alnum (wc3);  

    return 0;
}
```

运行结果：

```
2 is a alnum
a is a alnum
? is not a alnum
```

在Ubuntu 16.04 英文环境下测试，中文不是一个字母。如果有兴趣，你可以使用setlocale函数将本地环境设置为中文环境，看看运行结果是不是一样。
