### assert 函数使用说明



| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 李磊 | 2019.12.14 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |







#### 函数原型说明

```c
#include <assert.h>
void assert(scalar expression);
```



#### 功能描述

assert(expression) 是一个宏，可以帮助程序员查找它们代码中的一些bug，或者通过一个crash来产生输出异常处理事件。如果 asser(expression) 括号内的expression是false（比如，比较起来后等于zero），assert() 将会打打印错误信息到标准错误输出中，同时通过调用 abort(3) 使得终止这个程序。这个错误信息包含了文件名称和assert() 调用的函数，以及源代码的行数，和参数的内容。



#### 使用示例

```c
#include <stdio.h>
#include <assert.h>

int main(void)
{
    int a = 10;
    assert(5 == a);
    
    return 0;
}
```

运行结果：

```
a.out: main.c:7: main: Assertion `5 == a' failed.
Aborted (core dumped)
```

通过运行结果，我们可以看到，表达式 (5 == a) 是不成立的，所以assert() 会输出错误信息，同时调用 abort(3) 函数来终止程序运行。