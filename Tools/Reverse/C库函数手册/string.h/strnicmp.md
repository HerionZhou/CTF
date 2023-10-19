### 1. `strnicmp`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
int strnicmp(char *str1, char *str2, unsigned maxlen);
```



### 1.2功能描述

​     比较字符串str1和str2的前n个字符串字典序的大小，但是不区分字母大小写。 

### 1.3参数说明

​	str1, str2 --需要比较的两个字符串。

​	n--要比较的字符的数目。

### 1.4函数返回值

​	当str1<str2时，返回值是-1 ;

​	当str1=str2时，返回值是0; 

​	当str1>str2时，返回值是1。  

### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int main(void) 
{  
   char *buf1 = "BBBccc", *buf2 = "bbbccc";  
   int ptr;  
   ptr = strnicmp(buf2, buf1, 3);  
   if (ptr > 0)  
      printf("buffer 2 is greater than buffer 1\n"); 
   if (ptr < 0)  
      printf("buffer 2 is less than buffer 1\n");  
   if (ptr == 0)  
      printf("buffer 2 equals buffer 1\n");  
   return 0;  
}  
```



输出结果：buffer 2 equals buffer 1

### 1.6使用注意事项

无
