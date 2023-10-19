### 1.`strtok`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.16 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strtok(char *s, const char *delim);
```



### 1.2功能描述

 strtok() 分解字符串为一组字符串。参数s指向欲分割的字符串，参数delim则为分割字符串中包含的所有字符。当strtok()在参数s的字符串中发现参数delim中包含的分割字符时,则会将该字符改为\0 字符。在第一次调用时，strtok()必需给予参数s字符串，往后的调用则将参数s设置成NULL。每次调用成功则返回指向被分割出片段的指针. 

### 1.3参数说明

**str** -- 要被分解成一组小字符串的字符串。

**delim** -- 包含分隔符的 C 字符串。



### 1.4函数返回值

   该函数返回被分解的第一个子字符串，如果没有可检索的字符串，则返回一个空指针。 

### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int main(void)  
{  
   char input[16] = "abc,d";  
   char *p;  
   /* strtok places a NULL terminator  
   in front of the token, if found */  
   p = strtok(input, ",");  
   if (p)   printf("%s\n", p);  
   /* A second call to strtok using a NULL  
   as the first parameter returns a pointer  
   to the character following the token  */  
   p = strtok(NULL, ",");  
   if (p)   printf("%s\n", p);  
   return 0;  
}  


```



输出结果：abc
					d





### 1.6使用注意事项

无
