# isascii 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 孙松     | 2019.12.02   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |

### **函数原型**

```c
#include<ctype.h>
extern int isascii(int c);
```

### **功能描述**

判断字符c是否为ascii码,也就是判断c的范围是否在0到127之间。

### **使用示例**

**判断字符是否是ASCII码字符**

```c
#include <stdio.h>
#include <ctype.h>
 
int main()
{
        for(int i = 125; i<130; i++)
        {
                if(isascii(i))
                        printf("%d is an ascii character : %c\n",i,i);
                else
                        printf("%d is not an ascii character\n",i);
        }
        return 0;

```

运行结果：

```c
125 is an ascii character : }
126 is an ascii character : ~
127 is an ascii character : 
128 is not an ascii character
129 is not an ascii character
```

通过运算结果我们可以看出，超过127就不是ASCII码了。



### **参数说明**

int c ------ 要分类的的字符



### **函数返回值**

 - 若字符为ASCII码时，则返回会非零值
 - 若字符不为ASCII码时，则返回零



### **使用注意事项**

- 哪些字符属于哪个类的详细信息取决于当前的语言环境