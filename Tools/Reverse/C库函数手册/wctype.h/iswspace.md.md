# iswspace 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.02.08   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswspace (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个空白字符





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是空白字符，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

在中文环境下，定义一个宽字符串，然后去遍历判断这个宽字符串是否存在空白字符，若当前字符是空白字符，就替换为换行输出，若不是，就直接输出当前宽字符。

说明： `hello`  后面的空白字符为中文环境下的空格，而 `宅学部落!` 之间为英文环境下的空格。

```c
#include <stdio.h>
#include <wctype.h>
#include <locale.h>


int main (void)
{
	int i = 0;
	wint_t wstr[] = L"hello　宅 学 部 落 ！";
	setlocale (LC_ALL, "chs");
	wprintf(L"%ls\r\n", wstr);

    while(wstr[i] != '\0')
    {
    	if(iswspace (wstr[i]))
		{
			wprintf (L"\n");
			i++	;
		}
		wprintf (L"%lc",wstr[i++]);		
    } 
    wprintf (L"\n");
	
	return 0; 
}
```



运行结果：

```
hello　宅 学 部 落 ！
hello
宅
学
部
落
！
```

第一行可以看出中文的空格，会比英文的空格占据的空间大一些。且这个函数使用的时候，运行结果跟本地操作系统、中英文，或其他语言环境相关，当前中文环境下的空格也认为空白字符。



### **使用注意事项**

- 在Linux和Windows环境下运行上面的程序结果和打印可能不一样
- 在Linux下，如Ubuntu，需要设置本地化环境，如：setlocale (LC_ALL, "en_US.utf8");
- 关于setlocale的使用，可参考locale.h目录中的文档
- 关于wprintf的使用，可参考wchar.h头文件中关于wprintf函数的使用