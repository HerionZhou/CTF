# iswlower 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.03.24   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswlower (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是小写（在当前的语言环境中）





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是小写，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符串，然后去遍历判断这个宽字符串中的小写（字母），如果是，就打印该宽字符并计数，如果不是，就输出一个空格，遇到 `\0` 就结束循环，最终输出宽字符串中总的小写（字母）的个数。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	int count = 0;
	wint_t wstr[] = L"zhái xué";
	setlocale (LC_ALL, "chs");
	while(wstr[i] != '\0')
	{
		if(iswlower (wstr[i]))
		{
			wprintf (L"%lc", wstr[i++]);
			count++;
			continue;	
		}
		wprintf (L" ");
		i++;
		
	}
	wprintf (L"\r\nTotal %d lower\r\n", count);
	
	return 0; 
}
```



运行结果：

```
zhái xué
Total 7 lower
```

这个函数使用的时候，运行结果跟本地操作系统、中英文，或其他语言环境相关，如果本地是中文环境，拼音也是被认定为小写的。当然在英文环境下，就是 26 个小写字母认定为小写。



### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用



