# realloc 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.12   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void *realloc(void *ptr, size_t size);
```



### **功能描述**

C 库函数 `realloc()` 用于给一个已分配内存空间继续分配内存空间（扩容），该扩充空间的类型大小由 `size` 指定， `*ptr` 指向待扩充的内存首地址。`void *` 该返回值指针指向扩充后的内存首地址。





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

        return 0;
}

```

运行结果：

```
Test for the function ofTest for the function of malloc
```

通过运行结果，我们可以看到，首先定义了一个空字符指针，然后使用 `calloc` 函数为其分配较少的内存空间，放回分配后该空间的首地址，使用 `strcpy` 函数将字符床复制至该指针指向处，随后打印出来，可看到打印字符不全。再使用 `realloc` 对其重新分配，发现字符得以完全显示。





### **函数返回值**

- 函数运行成功，返回值为重新分配后的内存空间首地址。
- 函数运行失败，返回值空指针。







### **使用注意事项**

- `realloc` 函数是一个线程安全函数，在多线程环境中可以放心使用。
