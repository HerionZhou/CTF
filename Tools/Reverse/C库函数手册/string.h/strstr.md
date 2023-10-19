### 1. `strstr`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.16 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strstr(const char *str1, const char *str2);
```



### 1.2功能描述

查找在字符串str1中第一次出现str2的位置，可以验证str2是不是str1的字串。

### 1.3参数说明

 str1指向查找的字符串，str2表示要查找的字符串。



### 1.4函数返回值

  若str2是str1的子串，则返回str2在str1的首次出现的地址；如果str2不是str1的子串，则返回NULL。  



### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void)  
{  
   char *str1 = "Borland International", *str2 = "nation", *ptr;   
   ptr = strstr(str1, str2);  
   printf("The substring is: %s\n", ptr);  
   return 0;  
}
```



输出结果：national





### 1.6使用注意事项

无