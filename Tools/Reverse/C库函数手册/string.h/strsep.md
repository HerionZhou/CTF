### 1. `strsep`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.04 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strsep(char **stringp, const char *delim);
```



### 1.2功能描述

 分解字符串为一组字符串。从stringp指向的位置起向后扫描，遇到delim指向的字符串中的字符后，将此字符替换为NULL，返回stringp指向的地址。  

### 1.3参数说明

 stringp指向待分解的字符串，delim指向要替换的字符 。



### 1.4函数返回值

 返回指针stringp 



### 1.5程序实例



```c
#include<stdio.h>
#include<string.h>
int main(void)
{
	char str[] = "root:x::0:root:/root:/bin/bash:";
	char *buf;
	char *token;
	buf = str;
	while((token = strsep(&buf, ":")) != NULL){
		printf("%s\n", token);
		} 
	return 0;
}
```



输出结果：root
x

0
root
/root
/bin/bash





### 1.6使用注意事项

 strsep函数，这在 Windows Dev-C++ 是没有支持的，在写UNIX分析字符串常常需要利用到此函数。

