# isxdigit 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松     | 2019.12.10   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int isxdigit(int c);
```



### **功能描述**

用来检测一个字符是否是十六进制数字。
十六进制数字包括：0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F





### **使用示例**

找出字符串中的十六进制数字。
```c
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>



int main(int argc, const char *argv[])
{
    char *str="aB1%^$#EfG!@#";
    int i=0;
    while(str[i])
    {
        char c = str[i];
        if(isxdigit(c))
        {
            putchar(c);
        }
        i++;
    }
	return 0;
}
```

运行结果：

```c
aB1Ef
```

通过运算结果，我可以使用isxdigit函数来找出十六进制字符。



### **参数说明**

int c ------ 要检测的字符





### **函数返回值**

 - 若字符为十六进制数字字符，则返回会非零
 - 若字符不为十六进制数字字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境