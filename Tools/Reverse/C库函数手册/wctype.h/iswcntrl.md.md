# iswcntrl 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 王利涛   | 2020.01.03   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <wctype.h>
int iswcntrl (wint_t wc);
```



### **功能描述**

判断一个宽字符是否是控制字符



### **参数说明**

参数wc表示宽字符



### **函数返回值**

- 如果 wc 是控制字符，返回一个非零值
- 如果不是的话，函数返回0



### **使用示例**

判断一个宽字符是否是控制字符：

```c
#include <stdio.h>
#include <wctype.h>
#include <wchar.h>
#include <locale.h>

void is_cntrl (wchar_t wc)
{
    if (iswcntrl (wc))
        wprintf (L"%lc is a wcntrl\n", wc);
    else
        wprintf (L"%lc is not a wcntrl\n", wc);
}

int main (void)
{
    wchar_t wc1 = L'\n'; 
    wchar_t wc2 = L'a';
     
    is_cntrl (wc1);
    is_cntrl (wc2);

    return 0;
}
```

运行结果：

```
 is a wcntrl
a is not a wcntrl
```

