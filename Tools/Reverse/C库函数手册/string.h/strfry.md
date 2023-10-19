### 1. `strfry`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.01 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

①　char *strfry(char *str);



### 1.2功能描述

将一串字符串打乱成任意组合



### 1.3参数说明

str指向要打乱的字符串



### 1.4函数返回值

返回被打乱字符串的指针



### 1.5程序实例



```c
#include<stdio.h>
#include<string.h>
int main()
{
    char str[10]="abcdefghi";
    strfry(str);
    printf("%s\n",str);
    return 0;
}
```



输出结果：cbgihedfa (每次运行的结果都不同)







### 1.6使用注意事项

仅适用于GNU c 库



