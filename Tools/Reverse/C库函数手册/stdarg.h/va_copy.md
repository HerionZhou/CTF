### 1. localtime  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.12.04 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <stdarg.h>
void va_copy( va_list dest, va_list src );
```



#### 1.2. 功能描述

将 `src` 复制到 `dest`。





#### 1.3. 使用示例

```c
#include <stdio.h>
#include <stdarg.h>
#include <math.h>
 
double sample_stddev(int count, ...) 
{
    /* 以 args1 计算平均数。*/
    double sum = 0;
    va_list args1;
    va_start(args1, count);
    va_list args2;
    va_copy(args2, args1);   /* 复制 va_list 对象 */
    for (int i = 0; i < count; ++i) {
        double num = va_arg(args1, double);
        sum += num;
    }
    va_end(args1);
    double mean = sum / count;
 
    /* 以args2和平均数计算标准差。*/
    double sum_sq_diff = 0;
    for (int i = 0; i < count; ++i) {
        double num = va_arg(args2, double);
        sum_sq_diff += (num-mean) * (num-mean);
    }
    va_end(args2);
    return sqrt(sum_sq_diff / count);
}
 
int main(void) 
{
    printf("%f\n", sample_stddev(4, 25.0, 27.3, 26.9, 25.7));
}
```

运行结果：

```
0.920258
```







#### 1.4. 参数说明

|  参数   |    含义        |
| ------  | --------------------------------------- |
| dest | 一个要初始化的 `va_list` 类型的实例。 |
| src | 将用于初始化 `dest` 的源 `va_list`。 |







#### 1.5. 函数返回值

无







#### 1.6. 使用注意事项

在函数返回，或 `dest` 的任何再初始化（通过调用 `va_start` 或 `va_copy`）前，应该对 `dest` 调用 `va_end`。







