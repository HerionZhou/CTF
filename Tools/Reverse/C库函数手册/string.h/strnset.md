### 1.`strnset`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strnset(char *str, char ch, unsigned n);
```



### 1.2功能描述

   将字符串str中的前n个字符都设为指定字符ch。   

### 1.3参数说明

str--指向字符串

ch --设定字符

n--表示字符串前n个



### 1.4函数返回值

   返回指向更改后字符串的指针

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void) 
{  
   char *string = "abcdefghijklmnopqrstuvwxyz"; 
   char letter = 'x';  
   printf("string before strnset: %s\n", string); 
   strnset(string, letter, 13);  
   printf("string after  strnset: %s\n", string); 
   return 0;  
}  
```



输出结果：string before strnset: abcdefghijklmnopqrstuvwxyz

### 1.6使用注意事项

无