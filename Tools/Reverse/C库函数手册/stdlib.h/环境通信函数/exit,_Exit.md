# exit,Exit 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void exit(int status);

void _Exit(int status);
```



### **功能描述**

C 库函数 `exit()` 使程序正常终止。

C 标准定义了两个值 EXIT_SUCCESS 和 EXIT_FAILURE，可以作为 exit() 的参数，来分别指示是否为成功退出。





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
    printf("Test for exit\n");
    
    if(!exit(bye))
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
Test for exit
Called by exit
```

通过运行结果，我们可以看到，首先定义了 `bye()` 函数，使用 `exit()` 注册并判断返回值，通过 `exit()` 触发该注册函数。结果符合预期。





### **函数返回值**

- 函数运行成功，返回值为0。
- 函数运行失败，返回值非零。







### **使用注意事项**

- 多进程时，注意防止孤儿进程的产生。

