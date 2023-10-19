### 1.`strchr`函数使用说明

定义于头文件<string.h>



| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 梁磊磊 | 2019.12.18 | 内容初填 |
|          |        |            |          |





### 1.1函数原型

char *strchr(char *str,char c);

char *strchr(char *str,int c);   	//这里的字符是以int类型给出的



### 1.2功能描述

strchr函数在字符串中搜索第一次出现字符**c**（一个无符号字符）的位置。





### 1.3参数说明

*str--要被检索的字符串。

c--在str中要搜素的字符





### 1.3函数返回值

返回一个指向该字符串中第一次出现的字符的指针，如果字符串中不包含该字符则返回NULL空指针。



### 1.4程序实例

```c
#include <string.h>
#include <stdio.h>
int main(void)
{
    char string[17];
    char *ptr,c='w';
    strcpy(string,"helloworld");
    ptr=strchr(string,c);
    if(ptr)
        printf("%s\n",ptr);
    else
        printf("the c not found\n");
    return 0;
}
```



运行结果：world





### 1.6使用注意事项

<无>