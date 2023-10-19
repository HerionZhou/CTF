### 1.  va_start   函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.12.03 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <stdarg.h>
void va_start( va_list ap, parmN );
```



#### 1.2. 功能描述

`va_start` 宏使函数能访问后随具名参数 `parmN` 的可变参数。



#### 1.3. 使用示例

```c
#include <stdio.h>
#include <stdarg.h>
 
int add_nums(int count, ...) 
//这个函数声明中省略号表示的就是任意个数的参数，可变参数函数就是输入的参数的个数是可变的。
{
    int result = 0;
    va_list args;
    va_start(args, count);
    for (int i = 0; i < count; ++i) 
    {
        result += va_arg(args, int);
    }
    va_end(args);
    return result;
}
 
int main(void) 
{
    printf("%d\n", add_nums(4, 25, 25, 50, 50));
}
```

运行结果：

```
150
```







#### 1.4. 参数说明

| 参数  | 说明                     |
| ----- | ------------------------ |
| ap    | `va_list` 类型实例。     |
| parmN | 首个可变参数前的参数名。 |







#### 1.5. 函数返回值

（无）







#### 1.6. 使用注意事项

1）参数 `parmN` 是函数定义（在.......之前的那个）的可变参数表中最右边参数的标识符。如果采用 `register` 存储类别，一个函数或者数组类型，或者合应用默认的参数提升产生的类型不兼容的类型来声明参数 `parmN`，那么这种行为未定义。

2）宏 `va_start` 对 `ap` 进行初始化，以便后面 `va_arg` 和 `va_end` 对它的使用。





