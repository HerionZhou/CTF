### 1.`strupr`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.20 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strupr(char *str);
```



### 1.2功能描述

  将字符串str出现的小写字符转换为大写形式。 

### 1.3参数说明

str -- 要转换的字符串。



### 1.4函数返回值

   返回转换后的大写字符串。 

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void)  
{  
   char string[] = "abcdefghijklmnopqrstuvwxyz", *ptr;  
   /* converts string to upper case characters */  
   ptr = strupr(string); 
   printf("%s\n", ptr);  
   return 0;  
}  

```



输出结果：ABCDEFGHIJKLMNOPQRSTUVWXYZ

### 1.6使用注意事项

无