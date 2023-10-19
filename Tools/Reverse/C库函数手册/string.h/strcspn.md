### 1.`strcspn`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
int strcspn(char *str1,char *str2)
```



### 1.2功能描述

​    strcspn()从参数s 字符串的开头计算连续的字符，而这些字符都完全不在参数reject 所指的字符串中。简单地说， 若strcspn()返回的数值为n，则代表字符串s 开头连续有n 个字符都不含字符串reject 内的字符。  

### 1.3参数说明

 str1为参照字符串，即str2中每个字符分别与str1中的每个字符比较。 

### 1.4函数返回值

​    返回字符串s 开头连续不含字符串reject 内的字符整数。  

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h> 
int main(void)  
 {  
    char *string1 = "1234567890";  
    char *string2 = "747DC8";  
    int length;  
    length = strcspn(string1, string2); 
    printf("Character where strings intersect is at position %d\n", length);  
    return 0;  
 }  
```



输出结果：Character where strings intersect is at position 3

### 1.6使用注意事项

无