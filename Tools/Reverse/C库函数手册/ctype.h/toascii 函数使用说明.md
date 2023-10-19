# toascii 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松   | 2020.03.24   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |





### **函数原型**

```c
#include<ctype.h>
int toascii(int c)
```



### **功能描述**

toascii()会将参数c转换成7位的unsigned char值，第八位则会被清除，此字符即会被转成ASCII码字符。



### **使用示例**

```c

#include <ctype.h>
#include <stdio.h>
 
int main()
{
        int a = 217;
        char b;
        printf("a  value = %d(%c)\n",a,a);
        b = toascii(a);
        printf("a  value = %d(%c)\n",b,b);
 
 
}
```



运行结果：

```c
a  value = 217()
a  value = 89(Y)
```

从运行结果可以看出217之前并不是ascii字符，使用toascii后，称为ascii字符。



### **参数说明**

int c ------ 要分类的的字符





### **函数返回值**

 - 返回的值是转换后的字符的值






### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境