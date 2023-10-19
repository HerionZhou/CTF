### 1. `strncpy`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.12.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

char *strncpy(char *dest, char *src, int maxlen);



### 1.2功能描述

复制字符串src中的内容到字符串dest中，复制多少由maxlen的值决定。

### 1.3参数说明

dest指向目标字符串，src为指向源字符串，表示复制字符串的长度。



### 1.4函数返回值

*dest



### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void)  
{  

   char string[10];  
   char *str1 = "abcdefghi";  
   strncpy(string, str1, 3);  
   string[3] = '\0';  
   printf("%s\n", string);  
   return 0;  
}  
```



输出结果：abc







### 1.6使用注意事项

1)如果source的前n个字符不含NULL字符，则结果不会以NULL字符结束。如果n<source的长度，只是将source的前n个字符复制到destinin的前n个字符，不自动添加'\0'，也就是结果destinin不包括'\0'，需要再手动添加一个'\0'。如果source的长度小于n个字节，则以NULL填充destinin直到复制完n个字节。source和destinin所指内存区域不可以重叠且destinin必须有足够的空间来容纳source的字符长度+'\0'。

2）source串长度<=destin串长度,(这里的串长度包含串尾NULL字符)

​	如果n>source由于长度达到source NULL，正常复制，特别注意，如果source中有NULL，strncpy复制到NULL即使没到n也提前停止。如果n = source串长度，与strcpy一致。注意n的选择当n > destin串长度，destin栈空间溢出产生崩溃异常

3)source串长度>destin串长度

 	如果n =destin串长度，则destin串没有NULL字符，会导致输出会有[乱码](https://baike.baidu.com/item/乱码)。如果不考虑source串复制完整性，可以将destin 最后一字符置为'\0'。

综上，一般情况下，使用strncpy时，建议将n置为destin串长度（除非你将多个source串都复制到destin[数组](https://baike.baidu.com/item/数组)，并且从destin尾部反向操作)，复制完毕后，为保险起见，将destin串最后一字符置NULL，避免发生在第2)种情况下的输出乱码问题。