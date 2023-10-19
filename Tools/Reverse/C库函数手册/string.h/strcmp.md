### 1. `strcmp`使用说明

定义于头文件`<string.h>`





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 梁磊磊 | 2019.12.19 | 内容初填 |
|          |        |            |          |





### 1.1原型声明

 int strcmp(const char *str1, const char *str2); 



### 1.2功能描述

比较字符串str1和字符串str2，两个[字符](https://baike.baidu.com/item/字符)串自左向右逐个字符相比（按ASCII值大小相比较），直到出现不同的字符或遇'\0'为止。

当str1<str2时，返回为负数；

 当str=str2时，返回值= 0；

 当str1>str2时，返回正数。

如：1."A"<"B"  2."A"<"AB"  3."Apple"<"Banana"  4."A"<"a"  5."compare"<"computer"



### 1.3参数说明

str1和str2是字符串类型的参数



### 1.4函数返回值

int 类型的整数



### 1.5程序实例

```c
#include <string.h>  
#include <stdio.h>   
int main(void)  
 {  
    char *buf1 = "abd", *buf2 = "bff", *buf3 = "adf";  
    int ptr;  
    ptr = strcmp(buf2, buf1);  
    if (ptr > 0)  
       printf("buffer 2 is greater than buffer 1,%d\n",ptr);  
    else  
       printf("buffer 2 is less than buffer 1,%d\n",ptr);  
    ptr = strcmp(buf2, buf3);  
    if (ptr > 0)  
       printf("buffer 2 is greater than buffer 3,%d\n",ptr);  
    else  
       printf("buffer 2 is less than buffer 3,%d\n", ptr);  
    return 0;  
 }  

```



运行结果：buffer 2 is greater than buffer 1,1
buffer 2 is greater than buffer 3,1





### 1.6使用注意事项

strcmp(const char *s1,const char * s2)这里面只能比较字符串，即可用于比较两个字符串常量，或比较数组和字符串常量，不能比较数字等其他形式的参数。