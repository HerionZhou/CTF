# iscntrl 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2019.12.02   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int iscntrl(int c);
```



### **功能描述**

 - 检查是否为控制字符。即编码为0x00 - 0x1F及0x7F。
 - "控制字符"是指那些具有某种特殊功能、不会显示在屏幕上、不会占用字符位置的特殊字符。
 - 控制字符和可打印字符是相对的，可打印字符是指那些会显示在屏幕上、会占用字符位置的"普通"字符。






### **使用示例**

使用isalcntrl()判断字符串是否有控制字符，遇到控制字符停止输出。

```c
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

int main(int argc,char* argv[])
{
	char *str = "iscntrl test demo\n isntrl test demo2\n";
	int i = 0;
	int len = strlen(str);
	for(i = 0; i < len;i++)
	{
		if(!iscntrl(str[i]))
		{
			putchar(str[i]);
		}else
		{
			printf("\nmeet the control character\n");
			break;
		}
	}
	return 0;
}
```

运行结果为：

```c
iscntrl test demo
meet the control character
```

通过运算结果我们可以看出一旦遇到控制字符就停止输出字符。因为换行符\n是控制字符，它的ASCII码为0x0a。





### **参数说明**

int c ------ 要分类的的字符。它可以是一个有效的字符（被转换为int型），也可以是EOF，即无效字符。






### **函数返回值**

 - 若字符为控制字符，则返回会非零
 - 若字符不为控制字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境

