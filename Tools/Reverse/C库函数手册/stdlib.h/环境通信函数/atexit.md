# atexit 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

int atexit(void (*function)(void));
```



### **功能描述**

C 库函数 `atexit()` 用于注册 `function` 指向的函数，当程序调用 `exit()` 时，已注册的函数将按逆注册顺序被调用。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void bye(void)
{
    printf("Called by exit\n");
}

int main(void)
{
    printf("Test for atexit\n");
    
    if(!atexit(bye))
    {
        exit(EXIT_SUCCESS);
    }
    else
    {
        printf("exit failed\n");
        exit(EXIT_FAILURE);
    }
}
```

运行结果：

```
Test for atexit
Called by exit
```

通过运行结果，我们可以看到，首先定义了 `bye()` 函数，使用 `atexit()` 注册并判断返回值，通过 `exit()` 触发该注册函数。结果符合预期。





### **函数返回值**

- 函数运行成功，返回值为0。
- 函数运行失败，返回值非零。







### **使用注意事项**

- `atexit` 函数是一个线程安全函数，在多线程环境中可以放心使用。
