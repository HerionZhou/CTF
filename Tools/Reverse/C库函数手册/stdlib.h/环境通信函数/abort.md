# abort 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void abort(void);
```



### **功能描述**

C 库函数 `abort()` 使当前进程异常关闭。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world\n");
    abort();
    printf("Hello world\n");
    return 0;
}
```

运行结果：

```
Hello world
已放弃
```

通过运行结果，我们可以看到，代码中两个 `Hello world` 间插入了一个 `abort()` 使得程序运行至该出时异常退出，导致第二个 `Hello world` 没有打印出来，并且终端回显提示。





### **函数返回值**

- 无返回值。







### **使用注意事项**

- `abort` 函数是一个线程安全函数，在多线程环境中可以放心使用。
