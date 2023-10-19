### 1. `strspn`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.07 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
int strspn(const char *str1, const char *str2);
```



### 1.2功能描述

  检索字符串 **str1** 中第一个不在字符串 **str2** 中出现的字符下标。 

### 1.3参数说明

  **str1** 指向要被检索的 C 字符串。 str2指向该字符串包含了要在str1中进行匹配的字符列表

### 1.4函数返回值

 返回整数，返回str1中第一个不在字符串str2中出现的字符下标 



### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>   
int main(void)  
{  
   char *string1 = "1234567890";  
   char *string2 = "123DC8";  
   int length;  
   length = strspn(string1, string2);  
   printf("Character where strings differ is at position %d\n", length);  
   return 0;  
}  
```



输出结果：Character where strings differ is at position 3





### 1.6使用注意事项

无