### 1.`strxfrm`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.16 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
size_t strxfrm(char *dest, const char *src, size_t n);
```



### 1.2功能描述

 根据程序当前的区域选项中的 LC_COLLATE 来转换字符串 **src** 的前 **n** 个字符，并把它们放置在字符串 **dest** 中。 

### 1.3参数说明

dest-- 指向存储内容的目标数组的指针，如果参数 n 为 0，则它是一个空指针。

src -- 要被转换为当前区域设置的 C 字符串。

n-- 被复制到 str1 的最大字符数。

### 1.4函数返回值

​    该函数返回被转换字符串的长度，不包括空结束字符。 

### 1.5程序实例



```c
#include <stdio.h>
#include <string.h>
int main()
{
   char dest[20];
   char src[20]="hello world";
   int len;
   len = strxfrm(dest, src, 20);
   printf("字符串 %s 的长度是: %d", dest, len); 
   return(0);
}
```



输出结果：字符串 hello world 的长度是: 11



### 1.6使用注意事项

无