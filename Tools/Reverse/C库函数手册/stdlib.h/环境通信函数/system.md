# system 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

int system(const char *command);
```



### **功能描述**

C 库函数 `system()` 使用 `fork()` 创建子进程，在该子进程中使用 `execl()` 执行 `command` 指向的系统命令：

```c
execl("/bin/sh", "sh", "-c", command, (char *) 0);
```







### **使用示例**

```c
#include <stdlib.h>

int main(void)
{
    system("ls -l");

    return 0;
}
```

运行结果：

```
总用量 16
-rwxr-xr-x 1 yidougeng yidougeng 8640 12月 30 21:28 a.out
-rw-r--r-- 1 yidougeng yidougeng   76 12月 30 21:28 c.c
```

通过运行结果，我们可以看到，通过调用 `system()` 执行 `ls -l` 命令后，当前目录内的文件详细信息被列出至终端。





### **函数返回值**

- 子进程执行完后才会获得返回值。







### **使用注意事项**

- 线程安全。

