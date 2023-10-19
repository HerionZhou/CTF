# free 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.12   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void free(void *ptr);
```



### **功能描述**

C 库函数 `free()` 用于释放一个已分配内存空间， `*ptr` 指向待释放的内存首地址。





### **使用示例**

分别使用不同的格式符去打印内存中的一个数据：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
        char *str_1, *str_2;

        str_1 = (char *)calloc(10, sizeof(char));
        strcpy(str_1, "Test for the function of malloc\n");
        printf("%s", str_1);

        str_2 = (char *)realloc(str_1, 50*sizeof(char));
        strcpy(str_2, "Test for the function of malloc\n");
        printf("%s", str_2);

        free(str_2);
        printf("free = %s\n",str_2);

        return 0;
}
```

运行结果：

```
Test for the function ofTest for the function of malloc
free = 
```

通过运行结果，我们可以看到，使用 `free` 释放空间后，打印出的字符串为空。





### **函数返回值**

- 无返回值







### **使用注意事项**

- `free` 函数是一个线程安全函数，在多线程环境中可以放心使用。
