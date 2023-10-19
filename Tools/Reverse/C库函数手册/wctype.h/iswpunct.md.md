# iswpunct 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.03.31   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswpunct  (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个标点符号，标点符号是指本地语言环境下，不被 `iswspace`  函数和 `iswalnum` 函数认定为真的可打印宽字符。





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是标点符号，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符串，然后去判断这个宽字符在本地语言环境下是否标点字符，若是，就存储在是标点字符的数组中，若不是，就存储在不是标点字符的数组中。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	int countYes = 0, countNo = 0;
	wint_t wstr[] = L"1. Hello 宅学部落！";
	wint_t isApunct[20];
	wint_t notApunct[20];	
	setlocale (LC_ALL, "chs");

	while(wstr[i] != '\0')
	{
		if(iswpunct (wstr[i]))
		{
			isApunct[countYes++] = wstr[i++];
			continue;	
		}
		notApunct[countNo++] = wstr[i++];
		
	}
	
 	isApunct [countYes] = '\0';
	notApunct [countNo] = '\0';	
	wprintf (L"all of these are not punctuation :\n%ls \n\n", notApunct);
	wprintf (L"all of these are  punctuation :\n%ls \n", isApunct);
	
	return 0; 
}
```



运行结果：

```
all of these are not punctuation :
1 Hello 宅学部落

all of these are  punctuation :
.！
```

这个函数使用的时候，运行结果跟本地操作系统、中英文，或其他语言环境相关。



### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用



