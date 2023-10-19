### 1. `strpbrk`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.04 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
extern char *strpbrk(const char *str1, const char *str2);
```



### 1.2功能描述

 比较字符串str1和str2中是否有相同的字符，如果有，则返回该字符在str1中的位置的指针。 

### 1.3参数说明

 str1指向待比较的字符串，str2指向被搜索的字符串 。



### 1.4函数返回值

 返回指针，搜索到的字符在str1中的索引位置的指针。 



### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void)  
{  
   char *str1 = "abcdefghijklmnopqrstuvwxyz";  
   char *str2 = "onm";  
   char *ptr;  
   ptr = strpbrk(str1, str2);  
   if (ptr)  
      printf("strpbrk return is : %s\n", ptr);  
   else  
      printf("strpbrk didn't find character in set\n");  
   return 0;  
}  


```



输出结果：strpbrk return is : mnopqrstuvwxyz





### 1.6使用注意事项

无

