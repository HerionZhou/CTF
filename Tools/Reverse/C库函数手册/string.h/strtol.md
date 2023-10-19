### 1.`strtol`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.20 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
long int strtol(char *str, char **endptr, int base);
```



### 1.2功能描述

 将参数nptr字符串根据参数base来转换成长整型数。 strtol() 会将参数 str 字符串根据参数 base 来转换成长整型数(long)。参数 base 范围从2 至36，或0。参数base 代表 str 采用的进制方式，如base 值为10 则采用10 进制，若base 值为16 则采用16 进制等。

 strtol() 会扫描参数 str 字符串，跳过前面的空白字符（例如空格，tab缩进等，可以通过 isspace()函数来检测），直到遇上数字或正负符号才开始做转换，再遇到非数字或字符串结束时('\0')结束转换，并将结果返回。   

### 1.3参数说明

str -- 要转换的字符串。

endstr --第一个不能转换的字符的指针。

base --字符串 str 所采用的进制，范围从2至36。



### 1.4函数返回值

​    返回转换后的长整型数；如果不能转换或者 str 为空字符串，那么返回 0(0L)；如果转换得到的值超出 long int  所能表示的范围，函数将返回 LONG_MAX 或 LONG_MIN（在 limits.h 头文件中定义），并将 errno 的值设置为  ERANGE。 

### 1.5程序实例



```c
#include <stdlib.h>  
#include <stdio.h>  
int main(void)  
{  
   char *string = "87654321", *endptr;  
   long lnumber;  
   /* strtol converts string to long integer  */  
   lnumber = strtol(string, &endptr, 10);  
   printf("string = %s  long = %ld\n", string, lnumber);  
   return 0;  
}  

```



输出结果：string = 87654321  long = 87654321



### 1.6使用注意事项

当 base 的值为 0 时，默认采用 10 进制转换，但如果遇到 '0x' / '0X' 前置字符则会使用 16 进制转换，遇到 '0' 前置字符则会使用 8 进制转换。

若endptr 不为NULL，则会将遇到的不符合条件而终止的字符指针由 endptr 传回；若 endptr 为 NULL，则表示该参数无效，或不使用该参数。
