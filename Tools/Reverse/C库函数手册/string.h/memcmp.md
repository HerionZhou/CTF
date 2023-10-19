### 1. `memcmp`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.17 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
 int memcmp(const void *str1, const void *str2, size_t n);
```



### 1.2功能描述

  其功能是把存储区 str1 和存储区 str2 的前 n 个字节进行比较。该函数是按[字节](https://baike.baidu.com/item/字节/1096318)比较的。 

### 1.3参数说明

str1，str2是指向内存块的指针。

n--要被比较的字节数。

### 1.4函数返回值

如果返回值 < 0，则表示 str1 小于 str2。

如果返回值 > 0，则表示 str2 小于 str1。

如果返回值 = 0，则表示 str1 等于 str2。

### 1.5程序实例



```c
#include<string.h>
#include<stdio.h>
int main()
{
	char *s1 = "Hello,Programmers!";
	char *s2 = "Hello,Programmers!";
	int r;
	r = memcmp(s1,s2,strlen(s1));
	if(!r)
	    printf("s1 and s2 are identical\n");/*s1等于s2*/
	else if(r<0)
	    printf("s1 is less than s2\n");/*s1小于s2*/
	else
	    printf("s1 is greater than s2\n");/*s1大于s2*/
	return 0;
}
```



输出结果：s1 and s2 are identical

### 1.6使用注意事项

无