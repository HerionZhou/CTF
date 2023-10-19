# ispunct 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松     | 2019.12.10   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include<ctype.h>
int ispunct(int c);
```



### **功能描述**

检查给定的字符是否为当前 C 本地环境分类为标点字符。





### **使用示例**

统计文字中标点符号的个数。
```c
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>



int main(int argc, const char *argv[])
{
	char *str="This is test.author:song.";
    int number=0;
	int i=0;
    while(str[i])
    {
        if(ispunct(str[i]))
        {
            number++;
        }
        i++;     
    }
    printf("The number of punctuation marks in this text is %d\n",number);
	return 0;
}
```

运行结果：

```c
The number of punctuation marks in this text is 3
```

通过运算结果，可以使用ispunct函数来统计标点字符个数。



### **参数说明**

int c ------要检测的字符。它可以是一个有效的字符（被转换为int类型）,也可以是EOF（表示无效字符）。





### **函数返回值**

 - 若字符是标点字符，则返回非零
 - 若字符不为标点字符，则返回零






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境