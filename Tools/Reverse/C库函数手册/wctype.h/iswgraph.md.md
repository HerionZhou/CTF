# iswgraph 函数使用说明







| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 蔡宗福   | 2020.02.08   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### 函数原型

```c
#include <wctype.h>
int iswgraph (wint_t wc);
```





### **功能描述**

判断一个宽字符是否是一个图形字符（即除空格以外的任何打印字符）





### **参数说明**

参数 wc 表示宽字符





### **函数返回值**

- 如果 wc 是图形字符，返回一个非零值


- 如果不是的话，函数返回 0





### **使用示例**

定义一个宽字符，然后去判断这个宽字符是否是图形字符

```c
#include <stdio.h>
#include <wctype.h>

void is_wgragh (wint_t wc)
{
    if (iswgraph(wc))
        wprintf (L"%lc is a gragh\n", wc);
    else
        wprintf (L"%lc is not a gragh\n", wc);

}

int main (void)
{
	wint_t wi1 = L' ';
	wint_t wi2 = L'宅'; 
	wint_t wi3 = L'+'; 
	wint_t wi4 = L'/';
	
	is_wgragh (wi1);
	is_wgragh (wi2);
	is_wgragh (wi3);
	is_wgragh (wi4);
	
	return 0; 
}
```



运行结果：

```
  is not a gragh
 is a gragh
+ is a gragh
/ is a gragh
```

