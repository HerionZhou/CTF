### 1. `longjmp` 函数使用说明

定义于头文件 `<setjmp.h>`



| 文档版本 |   作者   |  修改日期  |     备注     |
| ------------- | ---------- | -------------- | ------------- |
| V0.1         |  [饕餮人](admin@taotieren.com)  | 2019.12.1 | 内容初填 |
|                  |              |                    |                  |
|                  |              |                    |                  |





#### 1.1. 函数原型

```c
void longjmp( jmp_buf env, int status );
_Noreturn void longjmp( jmp_buf env, int status );
```



#### 1.2. 功能描述

载入先前调用 `setjmp` 保存的执行环境 `env` 。此函数不返回。转移控制流到设置 `env `的宏 `setjmp` 的调用方。该 `setjmp` 会返回作为 `status` 传递的值。
若调用 `setjmp` 的函数已退出（通过返回或通过另一到栈上更高处的 `longjmp` ），则行为未定义。换言之，只有调用栈间的长跳转是允许的。

跨线程跳转（若调用 `setjmp` 的函数被另一线程执行）亦是未定义行为。
若在调用 `setjmp` 时， `VLA` 或其他可变修改类型变量在作用域中，并且控制流离开了该作用域，则 `longjmp` 到该 `setjmp` 将引发未定义行为，即使控制流仍然留在该函数内。
在上溯栈的途中， `longjmp` 不会解分配任何 `VLA` ，若其的生存期以此方式终结，则会出现内存泄漏：

```c
void g(int n)
{
    int a[n]; // a 仍为已分配
    h(n); // 不返回
}
void h(int n)
{
    int b[n]; // b 仍为已分配
    longjmp(buf, 2); // 可能因为 h 的 b 和 g 的 a 导致内存泄漏
}
```




#### 1.3. 使用示例

 `longjmp` 示例，使用 `printf()` 打印输出数据。

```c
#include <stdio.h>
#include <setjmp.h>
#include <stdnoreturn.h>
 
jmp_buf jump_buffer;
 
noreturn void a(int count) 
{
    printf("a(%d) called\n", count);
    longjmp(jump_buffer, count+1); // 将在 setjmp 外返回 count+1
}
 
int main(void)
{
    volatile int count = 0; // 必须为 setjmp 声明 volatile 对象
    if (setjmp(jump_buffer) != 9)
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

- `env` 	- 	引用 `setjmp` 所保存的程序执行状态的变量
- `status `	- 	要从 `setjmp` 返回的值。若它等于 `​0`​ ，则以 `1` 替代使用







#### 1.5. 函数返回值

（无） 







#### 1.6. 使用注意事项

`longjmp` 是有意用以处理未期待的错误条件的，该条件下函数无法有意义地返回。这与其他编程语言中的异常处理相似。 
