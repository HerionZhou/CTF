### 1. `strlen`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.01 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

size_t  strlen(const char *str);



### 1.2功能描述

计算字符串的长度，到'\0'为止，但不包括'\0'

### 1.3参数说明

str指向字符串。



### 1.4函数返回值

size_t（无符号整数）



### 1.5程序实例



```c
#include <stdio.h>
#include <string.h>
int main ()
{
   char str[20]="happy new year";
	int len;
   len = strlen(str);
   printf("%s 的长度是 %d \n", str, len);  
   return(0);
}

```



输出结果：happy new year 的长度是 14







### 1.6使用注意事项

无



