# iswprint 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.03.31   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswprint (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个可打印的宽字符。





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是可打印的宽字符，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符串，然后去判断这个字符串中的宽字符，在本地语言环境下是否是可打印宽字符，若是，就存储在是可打印宽字符的数组中，若不是，就存储在不是可打印宽字符的数组中。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	int countYes = 0, countNo = 0;
	wint_t wstr[] = L"1. Hello 宅学部落！\n\n\n";
	wint_t isAprint[20];
	wint_t notAprint[20];	
	setlocale (LC_ALL, "chs");

	while(wstr[i] != '\0')
	{
		if(iswprint (wstr[i]))
		{
			isAprint[countYes++] = wstr[i++];
			continue;	
		}
		notAprint[countNo++] = wstr[i++];
		
	}
	
 	isAprint [countYes] = '\0';
	notAprint [countNo] = '\0';	
	wprintf (L"%d not printing character :\n\n ", countNo);
	wprintf (L"all of these are  printing character :\n%ls \n", isAprint);
	
	return 0; 
}
```



运行结果：

```
3 of these are not printing character

 all of these are  printing character :
1. Hello 宅学部落！
```

这个函数使用的时候，运行结果跟本地操作系统、中英文，或其他语言环境相关。运行结果中 `countNo` 中的值，扣除一个存储 `\0` ，刚好是三个换行符 ，它们属于控制字符，所以不可打印。控制字符和通信专用字符都属于不可打印字符。





### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用



