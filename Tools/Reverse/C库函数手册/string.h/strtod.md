### 1.`strtod`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
double strtod(char *str, char **endptr);
```



### 1.2功能描述

 把参数 **str** 所指向的字符串转换为一个浮点数（类型为 double 型）。如果 **endptr** 不为空，则指向转换中最后一个字符后的字符的指针会存储在 endptr 引用的位置。 

### 1.3参数说明

**str** -- 待转换的字符串。

 **endptr** --  对类型为 char* 的对象的引用，其值由函数设置为 **str** 中数值后的下一个字符。 



### 1.4函数返回值

   该函数返回转换后的双精度浮点数，如果没有执行有效的转换，则返回零（0.0）。  

### 1.5程序实例



```c
#include <stdio.h>  
#include <string.h> 
int main(void)  
{  
   char input[80], *endptr; 
   char str[]="abcd" ; 
   double value;
   value = strtod(str, &endptr);  
   printf("The string is %s the number is %lf\n", str, value);  
   return 0;  
}  


```



输出结果：The string is abcd the number is 10422368.000000





### 1.6使用注意事项

无