# islower 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.04   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int islower(int c);
```



### **功能描述**

检查给定字符是否按照当前 C 本地环境分类为小写字符。





### **使用示例**

判断一串字符串中是否有小写字母，如果有则返回true,如果没有则返回false。

```c
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

bool JudgingCharacters(char *str)
{
	int len = strlen(str);
	int i;
	for(i = 0;i<len;i++)
	{
		if(islower(str[i]))
		{
			return true;
		}
	}
	return false;
}

int main(int argc,char *argv[])
{
	char *test = "TEST DEmO!";
	bool flag = JudgingCharacters(test);
	if(flag = true)
	{
		printf("Lowercase letters in the string\n");
	}else{
		printf("No lowercase letters in the string\n");
	}
	return 0;
}
```

运行结果:

```c
Lowercase letters in the string
```

通过结果可以看出可以通过islower判断字符是否为小写字母。





### **参数说明**

int c ------ 要分类的的字符





### **函数返回值**

 - 若字符为小写字符，则返回会非零
 - 若字符不为小写字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境