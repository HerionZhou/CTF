### 1. `strcpy`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.12.12 | 内容初填 |
|          |        |            |          |









### 1.1 原型声明

```c
char *strcpy(char *dest,const char *src);
```





### 1.2 功能描述

把从src指向的且含有NULL结束符的字符串复制到以dest指向的的地址空间，覆盖dest中原先的内容。



### 1.3参数说明

在调用strcpy函数中，strcpy函数无法检查src指向的字符串的大小是否真的适合dest指向的地址空间。假设dest指向的字符串长度为n，如果src指向的字符串不超过n-1，那么复制操作可以完成。但是src指向更长的字符串，结果无法预料。（ 因为strcpy函数会一直复制到第一个空字符为止，所以它会越过dest指向的数组边界继续复制。）



### 1.4 程序实例

```c
#include <strdio.h>
#include <string.h>

int main (void)
{
	char string[10];
	char *str1 = "abcdefghi";
	strcpy (string, str1);
	printf ("%s\n", string);
	return 0;
}
```



输出结果：abcdefghi





#### 1.5函数返回值

*dest

#### 1.6使用注意事项

<无>
