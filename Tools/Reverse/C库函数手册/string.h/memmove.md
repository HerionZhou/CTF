### 1. `memmove`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
void *memmove( void* dest, const void* src, size_t count );
```



### 1.2功能描述

 memmove用于拷贝字节，如果目标区域和源区域有重叠的话，memmove能够保证源串在被覆盖之前将重叠区域的字节拷贝到目标区域中，但复制后源内容会被更改。但是当目标区域与源区域没有重叠则和memcpy函数功能相同。 

### 1.3参数说明

 dest -- 指向用于存储复制内容的目标数组，类型强制转换为 void* 指针。

src -- 指向要复制的数据源，类型强制转换为 void* 指针。

count -- 要被复制的字节数



### 1.4函数返回值

   该函数返回一个指向目标存储区  dest的指针



### 1.5程序实例



```c
#include <stdio.h> 
#include <string.h>
int main(void) 
{ 
	char *dest = "abcdefghijklmnopqrstuvwxyz0123456789"; 
	char *src = "******************************"; 
	printf("destination prior to memmove: %s\n", dest); 
	memmove(dest, src, 26); 
	printf("destination after memmove: %s\n", dest); 
	return 0; 
} 
```



输出结果：destination prior to memmove: abcdefghijklmnopqrstuvwxyz0123456789



### 1.6使用注意事项

无