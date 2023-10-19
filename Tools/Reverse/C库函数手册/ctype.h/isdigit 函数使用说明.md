# isdigit 函数使用说明






| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.02   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int isdigit(int c);
```



### **功能描述**

该函数检查所传字符是否是十进制数字。





### **使用示例**

判断字符串中是否有十进制数字并打印出来。

```c
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<limits.h>

int main()
{
	int i =0 ;
	char *str = "2019year";
	int len = strlen(str);
	for(i = 0;i<len;i++)
	{
		if(isdigit(str[i]))
		{
			printf("is digit : %d\n",str[i]);
		}
	}
	return 0;
}
```

运行结果为：

```c
is digit : 50
is digit : 48
is digit : 49
is digit : 57
```

同过结果可以看出十进制数字包括：0 1 2 3 4 5 6 7  8 9。
### **参数说明**

int c ------ 要分类的的字符






### **函数返回值**

 - 若字符为十进制数字，则返回会非零
 - 若字符不为十进制数字，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境