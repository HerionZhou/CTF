# getenv 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

char *getenv(const char *name);
```



### **功能描述**

C 库函数 `getenv()` 在宿主环境提供的环境表中搜索 `name` 所指向的环境字符串，并返回指向该字符串的指针。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>

int main ()
{
   printf("PATH : %s\n", getenv("PATH"));

   return(0);
}
```

运行结果：

```
PATH : /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin
```

通过运行结果，我们可以看到，通过调用 `getenv()` 搜索 `PATH` 并打印，可以在环境变量中找到该指定的环境变量值。





### **函数返回值**

- 返回指向该字符串的指针。







### **使用注意事项**

- 线程安全。

