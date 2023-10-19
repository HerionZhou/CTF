### 1. `stpcpy`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.12.18 | 内容初填 |
|          |        |            |          |





### 

### 1.1函数原型

char *stpcpy(char *dest, char *src);



### 1.2功能描述

把src所指由NULL结束的字符串复制到dest所指的[数组](https://baike.baidu.com/item/数组)中。

### 1.3参数说明

dest指向目标字符串，src为指向源字符串。



### 1.4函数返回值

*dest



### 1.5程序实例



```c
#include<stdio.h>
#include<string.h>
int main()
{
	char *s="helloworld";
	char d[20];
	stpcpy(d,s);
	printf("%s",d);
	return 0;
}
```



输出结果：helloworld







### 1.6使用注意事项

src和dest所指内存区域不可以重叠且dest必须有足够的空间来容纳src的字符串。

