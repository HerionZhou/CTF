# iswalpha 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 王利涛   | 2020.01.03   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include <wctype.h>
int iswalpha(wint_t wc);


```



### **功能描述**

判断一个宽字符是否是字母。



### **参数说明**

参数wc表示宽字符



### **函数返回值**

- 如果 wc 是字符集中的字母，返回一个非零值
- 如果不是的话，函数返回0



### **使用示例**

定义一个宽字符串，然后去判断这个字符串中有多少个字母：

```c
#include <stdio.h>
#include <wctype.h>
#include <wchar.h>
#include <locale.h>

int main (void)
{
    int i = 0;
    int count = 0;
    wchar_t wstr[] = L"hello宅学部落";
    setlocale (LC_ALL, "chs");
    while (wstr[i])
    {
        if (iswalpha(wstr[i]))
        {
            wprintf (L"%lc ", wstr[i++]);
            count++;
        }
    }
    wprintf (L"\nTotal %d alphabet\n", count);
    return 0;
}
```

运行结果：

```
h e l l o 宅 学 部 落 
Total 9 alphabet
```

这个函数使用的时候，运行结果跟本地操作系统、中英文环境相关，如果本地是英文环境，遇到中文字符时，可能不认为是个字母，我们可以使用 setlocale 设定本地化环境，识别中文汉字。

宽字符一般是双字节存储的，打印宽字符一般使用wprintf函数，占位符使用 “ls”，在定义宽字符时，要在字符或字符串的前面加一个L，表示宽字符、双字节存储。



### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用
