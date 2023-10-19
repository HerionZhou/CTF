### 1. `memchr`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
void *memchr(const void *str, int c, size_t n);
```



### 1.2功能描述

   在参数 **str** 所指向的字符串的前 **n** 个字节中搜索第一次出现字符 **c**（一个无符号字符）的位置。 

### 1.3参数说明

 str--指向要执行搜索的内存块。

c--以int的形式传递的值，但是函数在每次字节搜索时是使用该值的无符号形式。

### 1.4函数返回值

​    返回一个指向匹配字节的指针，如果在给定的内存区域未出现字符，则返回 NULL。 



### 1.5程序实例



```c
#include <stdio.h> 
#include <string.h>
int main(void) 
{ 
	char str[17]; 
	char *ptr; 
	strcpy(str, "This is a string"); 
	ptr = memchr(str, 'r', strlen(str)); 
	if (ptr) 
		printf("The character 'r' is at position: %d\n", ptr - str); 
	else 
		printf("The character was not found\n"); 
	return 0; 
} 
```



输出结果：The character 'r' is at position: 12

### 1.6使用注意事项

无