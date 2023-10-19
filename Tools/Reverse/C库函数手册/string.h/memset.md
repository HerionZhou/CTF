### 1. `memset`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
void *memset(void *str, int c, size_t n);
```



### 1.2功能描述

​    复制字符 **c**（一个无符号字符）到参数 **str** 所指向的字符串的前 **n** 个字符。 

### 1.3参数说明

 str--指向要执行搜索的内存块。

c--以int的形式传递的值，但是函数在每次字节搜索时是使用该值的无符号形式， 这个函数通常为新申请的内存做初始化工作。 

### 1.4函数返回值

​     返回一个指向存储区 str 的指针。 

### 1.5程序实例



```c
#include <stdio.h>
#include <string.h>
int main(void) 
{ 
	char buffer[] = "Hello world\n"; 
	printf("Buffer before memset: %s\n", buffer);
	memset(buffer, '-', strlen(buffer) - 1); 
	printf("Buffer after memset: %s\n", buffer); 
	return 0; 
} 
```



输出结果：Buffer before memset: Hello world

Buffer after memset: -----------

### 1.6使用注意事项

无