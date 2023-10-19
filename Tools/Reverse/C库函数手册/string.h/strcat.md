### 1. `strcat`（字符拼接函数）函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.12.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

char *strcat(char *dest,char *src);



### 1.2功能描述

strcat函数把字符串stc中的内容追加到字符串dest的末尾，并且返回字符串dest（指向结果的字符串的指针）。



### 1.3参数说明

dest指向目标字符串，src为指向源字符串。



### 1.4函数返回值

*dest



### 1.5程序实例



```c
#include<string.h>　
#include<stdio.h>
int main()　
{　
	char dest[10];
	strcpy(dest,"abc");
	strcat(dest,"def");
	printf("%s\n",dest);
    return 0;
}
```



输出结果：abcdef







### 1.6使用注意事项

假设从dest开始的内存区足够大，能够放下这两个字符串：终止dest的null字符（和内存后面的其他字符）被src中的字符串和新的终止null字符覆盖，直到遇到src中的null字符。如果dest指向的内存没有大到足以容纳字符串dest和字符串src，那么调用strcat(dest,src)的结果是不可预测的。



