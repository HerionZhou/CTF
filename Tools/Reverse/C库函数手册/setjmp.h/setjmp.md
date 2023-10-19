### 1. `setjmp` 函数使用说明

定义于头文件 `<setjmp.h>`



| 文档版本 |                         作者                         |  修改日期  |     备注     |
| ------------- | --------------------------------------------- | -------------- | ------------- |
| V0.1         | [饕餮人](admin@taotieren.com) | 2019.12.1 | 内容初填 |
|                  |                                                          |                    |                  |
|                  |                                                          |                    |                  |





#### 1.1. 函数原型

```c
#define setjmp(env)   /* 指定-定义 */
```



#### 1.2. 功能描述

将当前执行环境保存到 ` jmp_buf` 类型对象 `env` 。此对象可在之后被 `longjmp` 函数用来恢复当前执行环境。即当调用 `longjmp` 函数时，执行将从传递给 `longjmp` 的 `jmp_buf` 对象所构建的特定调用点继续。该情况下 `setjmp` 返回传递给 `longjmp` 的值。






#### 1.3. 使用示例

 `setjmp` 示例，使用 `printf()` 打印输出数据。

```c
#include <stdio.h>
#include <setjmp.h>
#include <stdnoreturn.h>
 
jmp_buf jump_buffer;
 
noreturn void a(int count) 
{
    printf("a(%d) called\n", count);
    longjmp(jump_buffer, count+1); // 将从 setjmp 外 count+1
}
 
int main(void)
{
    volatile int count = 0; // setjmp 作用域内要修改的局部变量必须为 volatile
    if (setjmp(jump_buffer) != 9) // 在一个 if 内与常数比较
        a(count++);
}
```

运行结果：

```c
a(0) called
a(1) called
a(2) called
a(3) called
a(4) called
a(5) called
a(6) called
a(7) called
a(8) called
```






#### 1.4. 参数说明

`env` 	- 	要保存程序执行状态的对象。







#### 1.5. 函数返回值

- 若原初代码调用该宏，则返回 `​0`​ ，并保存执行环境到 `env` 。
- 若进行了非局部跳转则可返回非零值。返回值与传递给 `longjmp `者相同。 







#### 1.6. 使用注意事项

`setjmp` 的调用必须只出现在下列语境之一中：

- 选择或迭代语句（ `if` 、 `switch` 、 `for` 、 `while` 、 `do-while` ）的完整控制表达式

```c
switch(setjmp(env)) { ..
```

- 比较或相等运算符的一个运算数，另一运算数为整数常量表达式，产生的表达式为选择或迭代语句的完整控制表达式

```c
if(setjmp(env) > 10) { ...
```

- 一元 `!` 运算符的运算数，其结果为选择或迭代语句的完整控制表达式

```c
while(!setjmp(env)) { ...
```

- 表达式语句的完整表达式（可以将其转型到 `void` ）。

```c
setjmp(env);
```

若 `setjmp` 出现于其他语境中，则行为未定义。

在返回到 `setjmp` 的作用域之后，所有可访问对象、浮点状态标志，以及抽象机的其他组分拥有 `longjmp` 执行时的值，除了 `setjmp` 作用域内的非 `volatile` 局部变量，若在调用 `setjmp` 后更改它们，则其值不确定。
