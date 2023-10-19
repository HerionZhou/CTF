### 1. `strrchr`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.04 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strrchr(const char *str, int c);
```



### 1.2功能描述

 查找一个字符c在另一个字符串str中末次出现的位置（也就是从str的右侧开始查找字符c首次出现的位置），并返回这个位置的地址,使用这个地址返回从最后一个字符c到str末尾的字符串。 如果未能找到指定字符，那么函数将返回NULL。

### 1.3参数说明

 str指向查找的字符串，c表示要查找的字符。



### 1.4函数返回值

 返回指针，指向查找字符到str结束的指针。 



### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int main(void)  
{  
   char string[20];  
   char *ptr;
   int c = 'r';  
   strcpy(string, "This is a string");  
   ptr = strrchr(string, c);  
   if (ptr)  
      printf("%s\n",ptr);  
   else  
      printf("The character was not found\n");  
   return 0;  
}  

```



输出结果：ring





### 1.6使用注意事项

因为函数原型里c是int类型，所以如果要查找字符，需要加单引号引起来表示整数

