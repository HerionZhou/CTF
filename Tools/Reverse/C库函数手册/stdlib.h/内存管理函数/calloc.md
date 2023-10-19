# calloc 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.12   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void *calloc(size_t nmemb, size_t size);
```



### **功能描述**

C 库函数 `calloc()` 用于给一个对象分配内存空间，该空间的类型大小由 `size` 指定，数量由 `nmemb` 指定。`void *` 该返回值指针只想分配好的内存首地址，并且会对分配好的内存进行初始化（清零）。





### **使用示例**

分别使用不同的格式符去打印内存中的一个数据：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
        char *str;

        str = (char *)calloc(50, sizeof(char));
        strcpy(str, "Test for the function of calloc\n");
        printf("%s", str);

        return 0;
}
```

运行结果：

```
Test for the function of calloc
```

通过运行结果，我们可以看到，首先定义了一个空字符指针，然后使用 `calloc` 函数为其分配空间，放回分配后该空间的首地址，使用 `strcpy` 函数将字符床复制至该指针指向处，随后打印出来。





### **函数返回值**

- 函数运行成功，返回值为分配后的内存空间首地址，并且对分配空间进行初始化。
- 函数运行失败，返回值空指针。







### **使用注意事项**

- `calloc` 函数是一个线程安全函数，在多线程环境中可以放心使用。
