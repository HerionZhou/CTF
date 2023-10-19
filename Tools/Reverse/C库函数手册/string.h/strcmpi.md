### 1.`strcmpi`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
int strcmpi(char *str1, char *str2);
```



### 1.2功能描述

  比较字符串str1和str2，但不区分字母的大小写。 

### 1.3参数说明

str1,str2--指向待比较的字符串



### 1.4函数返回值

  当s1<s2时，返回值<0

当s1=s2时，返回值=0

当s1>s2时，返回值>0

### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int main(void)  
{  
   char *buf1 = "BBB", *buf2 = "bbb";  
   int ptr;  
   ptr = strcmpi(buf2, buf1);  
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