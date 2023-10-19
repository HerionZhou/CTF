### 1. `strncmp`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.01 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

int strncmp(const char *str1, const char *str2, size_t n);



### 1.2功能描述

把 str1 和 str2 进行比较，最多比较前 **n** 个字节，若str1与str2的前n个字符相同，则返回0；若s1大于s2，则返回正数；若s1 小于s2，则返回负数

### 1.3参数说明

str1和str2都是指向字符串，n是无符号整数



### 1.4函数返回值

如果返回值 < 0，则表示 str1 小于 str2。

如果返回值 > 0，则表示 str2 小于 str1。

如果返回值 = 0，则表示 str1 等于 str2。



### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int  main(void)  
{  
	char *buf1 = "aaabbb", *buf2 = "bbbccc", *buf3 = "ccc";  
   int ptr;  
   ptr = strncmp(buf2,buf1,3);  
   if (ptr > 0)  
      printf("buffer 2 is greater than buffer 1\n");  
   else  
      printf("buffer 2 is less than buffer 1\n");  
   ptr = strncmp(buf2,buf3,3);  
   if (ptr > 0)  
      printf("buffer 2 is greater than buffer 3\n");  
   else  
      printf("buffer 2 is less than buffer 3\n");  
   return(0);  
}  


```



输出结果：buffer 2 is greater than buffer 1
buffer 2 is less than buffer 3







### 1.6使用注意事项

无

