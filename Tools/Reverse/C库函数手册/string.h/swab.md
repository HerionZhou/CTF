### 1.`swab`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.20 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
void swab (char *from, char *to, int nbytes);
```



### 1.2功能描述

 交换相邻的奇偶字节， 如果 nbytes 字节数为偶数，所有的奇偶字节都会互相交换，如果 nbytes 是奇数，前 nbytes-1 个字节会进行奇偶交换。 

### 1.3参数说明

from -- 要交换的字符串。

to --指向接收目标数据的缓存

nbytes--字节数

### 1.4函数返回值

​    没有返回值

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
char source[15] = "rFna koBlrna d";  
char target[15];  
int main(void)  
{  
   swab(source, target, strlen(source));  
   printf("This is target: %s\n", target);  
   return 0;  
}  
```



输出结果：This is target: Frank Borland



### 1.6使用注意事项

无