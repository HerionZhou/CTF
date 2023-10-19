### 1.`strrev`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strrev(char *str);
```



### 1.2功能描述

   把字符串s的所有字符的顺序颠倒过来（不包括空字符NULL）。 

### 1.3参数说明

str--指向待颠倒的字符串

### 1.4函数返回值

   返回指向颠倒顺序后的字符串指针。 

### 1.5程序实例



```c
#include <string.h>  
#include <stdio.h>  
int main(void)  
{  
   char forward[] = "string";  
   printf("Before strrev(): %s\n", forward);  
   strrev(forward);  
   printf("After strrev():  %s\n", forward);  
   return 0;  
}  
```



输出结果：Before strrev(): string
After strrev():  gnirts

### 1.6使用注意事项

无
