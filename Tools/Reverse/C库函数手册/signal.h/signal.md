### signal 函数使用说明



| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 李磊 | 2019.01.05 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |







#### 函数原型说明

```c
#include <signal.h>
typedef void (*sighandler_t)(int);
sighandler_t signal(int signum, sighandler_t handler);
```



#### 功能描述

signal() 的行为方式在不同的UNIX版本中，以及不同版本的Linux中都有所不同。避免使用这些：用 sigaction(2) 代替。signal() 将信号signum设置为handler，可以是SIG_IGN、SIG_DFL，或者是程序员定义的函数（一个"signal handler"）。如果将信号signum传递给进程，会发生以下情况之一：

​		(1) 如果signum设置为SIG_IGN，这个信号将会被忽略

​		(2) 如果signum设置为SIG_DFL，将会发生与信号默认相关联的操作（查看 signal(7)）

​		(3) 如果signum设置为自定义的函数，那么首先将其重新设置为SIG_DFL，或者重新设置为阻塞信号，然后handler调用参数signum。如果handler导致信号被阻塞，则从handler返回时解除阻塞。



#### 使用示例

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

static void catch_function(int signal) {
    printf("Interactive attention signal caught.\n");
}

int main(void) {
    if (signal(SIGINT, catch_function) == SIG_ERR) {
        fprintf(stderr, "An error occurred while setting a signal handler.\n");
        return EXIT_FAILURE;
    }
    printf("The interactive attention signal.\n");
    if (raise(SIGINT) != 0) {
       fprintf(stderr, "Error the signal.\n");
        return EXIT_FAILURE;
    }
   printf("Exiting.\n");
    return 0;
}
```

运行结果：

```
The interactive attention signal.
Interactive attention signal caught.
Exiting.
```

通过运行结果，我们可以看到， 一个信号的处理函数在信号到达时，被目标函数调用。 

