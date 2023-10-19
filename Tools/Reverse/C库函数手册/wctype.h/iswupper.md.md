# iswupper 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.04.04   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswupper (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个大写字母或者是本地语言环境下指定的一些字符，一般地，这些字符不被 `iswcntrl`  函数， `iswdigit` 函数，`iswpunct` 函数，`iswspace` 认定为真的宽字符。





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是大写字符，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符串，然后去判断这个宽字符在本地语言环境下是否大写字符，若是，就存储在是大写字符的数组中，若不是，就存储在不是大写字符的数组中。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	int countYes = 0, countNo = 0;
	wint_t wstr[] = L"1. Hello 宅学部落！ΩΔ";
	wint_t isAupper[20];
	wint_t notAupper[20];	
	setlocale (LC_ALL, "chs");

	while(wstr[i] != '\0')
	{
		if(iswupper (wstr[i]))
		{
			isAupper[countYes++] = wstr[i++];
			continue;	
		}
		notAupper[countNo++] = wstr[i++];
		
	}
	
 	isAupper [countYes] = '\0';
	notAupper [countNo] = '\0';	
	wprintf (L"all of these are not upper :\n%ls \n\n", notAupper);
	wprintf (L"all of these are  upper :\n%ls \n", isAupper);
	
	return 0; 
}
```



运行结果：

```
all of these are not upper :
1. ello 宅学部落！

all of these are  upper :
HΩΔ
```

这个函数使用的时候，运行结果跟本地操作系统、中英文，或其他语言环境相关。在运行结果中我们可以看到，在当前的中文环境下，不仅有我们通常的认为的大写字母，还有 `ΩΔ` 也认为是大写。



### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用



