### 1.`memcpy`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.16 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
 void *memcpy(void *str1, const void *str2, size_t n)
```



### 1.2功能描述

 从存储区 **str2** 复制 **n** 个字符到存储区 **str1** 

### 1.3参数说明

str1 -- 指向用于存储复制内容的目标数组，类型强制转换为 void* 指针。

str2-- 指向要复制的数据源，类型强制转换为 void* 指针。

n-- 要被复制的字节数。



### 1.4函数返回值

​    返回一个指向目标存储区 str1 的指针。 

### 1.5程序实例



```c
#include<stdio.h>
#include<string.h>
int main(void) 
{ 
	char src[] = "--------------------------"; 
	char dest[] = "abcdefghijlkmnopqrstuvwxyz0123456709"; 
	char *ptr; 
	printf("destination before memcpy: %s\n", dest); 
	ptr = memcpy(dest, src, strlen(src)); 
	if (ptr) 
		printf("destination after memcpy: %s\n", dest); 
	else 
		printf("memcpy failed\n"); 
	return 0; 
} 
```



输出结果：destination before memcpy: abcdefghijlkmnopqrstuvwxyz0123456709
					destination after memcpy: --------------------------0123456709



### 1.6使用注意事项

无