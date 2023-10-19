# isalnum 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.02   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int isalnum(int c);
```



### **功能描述**

检查给定的字符是否为当前C本地环境所分类的字母数字字符。它等效于（isalpha(c)或者(isdigit(c))）





### **使用示例**

判断当前字符变量c是否为字母或数字
```c
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>



int main(int argc, const char *argv[])
{
	int c1 = 'a';
	printf("c1 is %c and c1 are alphanumeric characters %s\n",c1,isalnum(c1)?"yes":"no");
	int c2 = '1';
	printf("c2 is %c and c2 are alphanumeric characters %s\n",c2,isalnum(c2)?"yes":"no");
	int c3 = '#';
	printf("c3 is %c and c3 are alphanumeric characters %s\n",c3,isalnum(c3)?"yes":"no");
	return 0;
}
```

运行结果：

```c
c1 is a and c1 are alphanumeric characters yes
c2 is 1 and c2 are alphanumeric characters yes
c3 is # and c3 are alphanumeric characters no
```

通过运算结果，我们可以看出当c为数字0-9或者字母a-z及A-Z时，返回非零值，否则返回零。





### **参数说明**

int c ------ 要分类的的字符





### **函数返回值**

 - 若字符为字母数字字符，则返回会非零
 - 若字符不为字母数字字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境