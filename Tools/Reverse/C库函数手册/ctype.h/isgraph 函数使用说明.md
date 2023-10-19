# isgraph 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.04   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int isgraph(int c);
```



### **功能描述**

检查空格以外的任何可打印字符。即检查给定的字符是否拥有图形表示，即它是数字（0123456789）、大写字母（ABCDEFGHIJKLMNOPQRSTUVWXYZ）、小写字母（ abcdefghijklmnopqrstuvwxyz ）或标点字符，或任何指定于当前 C 本地环境的图形字符之一。





### **使用示例**

打印字符串，并判断字符是否为可打印字符。

```c
#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(int argc,char *argv)
{
	char *str = "s1 @;";
	int len = strlen(str);
	int i;
	for( i = 0;i<len;i++)
	{
		if(isgraph(str[i]))
		{
			printf("str[%d] is printable character:%c\n",i,str[i]);
		}else{
			printf("str[%d] is not printable character:%c\n",i,str[i]);
		}
	}
	return 0;
}
```

运行结果：

```c
str[0] is printable character:s
str[1] is printable character:1
str[2] is printable character:  
str[3] is printable character:@
str[4] is printable character:;
```

通过运算结果我们可以得出空格不是可打印字符。





### **参数说明**

int c ------ 要检测的的字符





### **函数返回值**

 - 若字符为图形字符，则返回会非零
 - 若字符不为图形字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境