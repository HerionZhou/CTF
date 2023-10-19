### 1. `strdup`（字符拼接函数）函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.12.29 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

char *strdup(char *str); 



### 1.2功能描述

将串拷贝到新建的位置处

strdup()会先用maolloc()配置与参数s 字符串相同的空间大小，然后将参数s 字符串的内容复制到该内存地址，然后把该地址返回。该地址最后可以利用free()来释放。 

### 1.3参数说明

str指向目标字符串。



### 1.4函数返回值

返回一个指针,指向为复制字符串分配的空间;如果分配空间失败,则返回NULL值。

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h>  
int main(void)  
 {  
    char *dup_str, *string = "abcde";  
    dup_str = strdup(string);  
    printf("%s\n", dup_str);  
    free(dup_str);  
    return 0;  

 }  


```



输出结果：abcde







### 1.6使用注意事项

无

