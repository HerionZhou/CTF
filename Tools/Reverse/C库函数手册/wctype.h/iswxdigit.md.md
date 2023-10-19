# iswxdigit 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.04.04   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswxdigit (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个十六进制数。





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是一个十六进制数，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符串，然后去判断这个宽字符是否是十六进制数，若是，就存储在是十六进制的数组中，若不是，就存储在不是十六进制的数组中。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	int countYes = 0, countNo = 0;
	wint_t wstr[] = L"1. Hello 宅学部落！";
	wint_t isAwxdigit[20];
	wint_t notAwxdigit[20];	
	setlocale (LC_ALL, "chs");

	while(wstr[i] != '\0')
	{
		if(iswxdigit (wstr[i]))
		{
			isAwxdigit[countYes++] = wstr[i++];
			continue;	
		}
		notAwxdigit[countNo++] = wstr[i++];
		
	}
	
 	isAwxdigit [countYes] = '\0';
	notAwxdigit [countNo] = '\0';	
	wprintf (L"all of these are not xdigit :\n%ls \n\n", notAwxdigit);
	wprintf (L"all of these are  xdigit :\n%ls \n", isAwxdigit);
	
	return 0; 
}
```



运行结果：

```
all of these are not xdigit :
. Hllo 宅学部落!

all of these are  xdigit :
1e
```

注：十六进制数有：0 1 2 3 3 4 5 67 8 9 A B C D E F




