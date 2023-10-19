# isalpha 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.02   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int isalpha(int c);
```



### **功能描述**

检查字母字符；在标准C语言环境下，它等效于（（isupper(c)）||（islower(c)））。在特殊语言环境中，可能还有其他字符，其isalpha()是真实字母，既不是大写字母也不是小写字母。





### **使用示例**

判断当前字符是否为字母

```c
#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(int argc,char* argv[])
{
	char *str = "isalphaTest!";
	int len = strlen(str);
	int i;
	for(i=0;i<len;i++)
	{
		if(isalpha(str[i]))
		{
			printf("character %c is alphabetic\n",str[i]);
		}else
		{
			printf("character %c is not alphabetic\n",str[i]);
		}
	}
	return 0;
}
```

运行结果：

```c
character i is alphabetic
character s is alphabetic
character a is alphabetic
character l is alphabetic
character p is alphabetic
character h is alphabetic
character a is alphabetic
character ! is not alphabetic
```

通过运算结果，我们可以看出当字符为字母时，返回值为非零，当字符不是字母时，返回值为零。





### **参数说明**

int c ------ 要分类的的字符






### **函数返回值**

 - 若字符为字母字符，则返回会非零
 - 若字符不为字母字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境