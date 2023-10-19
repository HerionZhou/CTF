# errno.h文档说明

| 文档版本 |            作者             |  修改日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.25 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <errno.h>

#ifndef errno 
extern int errno; 
#endif 
```

### 功能描述

- errno 是一个预处理器宏（见后述），展开成线程局域的 (C11 起) int 类型可修改左值。一些标准库函数通过写入正整数到 errno 指定错误。通常，会将 errno 的值设置为错误码之一。错误码作为以字母 E 后随大写字母或数字开始的宏常量，列于 <errno.h> 。

- errno 的值在程序启动时为 0 ，而且无论是否出现错误，都允许库函数将正整数写入 errno ，不过库函数决不会将 0 存储于 errno 。

- 库函数 perror 和 strerror 能用于获得对应当前 errno 值的错误条件的文本描述。

- 注解： C11 前， C 标准有矛盾的要求，称 errno 是宏但亦称“不指明 errno 是宏还是声明带外部链接的标识符”。 C11 修正了此错误，要求必须定义它为宏。

### 使用示例

```c
// filename : file_errno.c
#include <stdio.h>
#include <math.h>
#include <errno.h>
 
void show_errno(void)
{
    const char *err_info = "unknown error";
    switch (errno) {
    case EDOM:
        err_info = "domain error";
        break;
    case EILSEQ:
        err_info = "illegal sequence";
        break;
    case ERANGE:
        err_info = "pole or range error";
        break;
    case 0:
        err_info = "no error";
    }
    fputs(err_info, stdout);
    puts(" occurred");
}
 
int main(void)
{
    fputs("MATH_ERRNO is ", stdout);
    puts(math_errhandling & MATH_ERRNO ? "set" : "not set");
 
    errno = 0;
    1.0/0.0;
    show_errno();
 
    errno = 0;
    acos(+1.1);
    show_errno();
 
    errno = 0;
    log(0.0);
    show_errno();
 
    errno = 0;
    sin(0.0);
    show_errno();
}
```

输出结果：

```
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_errno.c -o app -lm && ./app
// 输出结果
MATH_ERRNO is set
no error occurred
domain error occurred
pole or range error occurred
no error occurred
```

