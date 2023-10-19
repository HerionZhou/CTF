### 1. clock  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.11.28 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <time.h>
clock_t clock(void);
```



#### 1.2. 功能描述

 函数返回从“开启这个程序进程”到“程序中调用 `clock()` 函数”时之间的CPU时钟计时单元`clock tick` 数，其中 `clock_t` 是用来保存时间的数据类型。值除以 `CLOCKS_PER_SEC`  可转换为秒。 





#### 1.3. 使用示例

测试程序执行时间

```c
#include <stdio.h>
#include <time.h>

int cpp11() {
    int a;
    int b;
    int c;
    int d = 10000;
    for (a = 0; a < d; a++) {
        for (b = 0; b < d; b++) {
            c = a * b;
        }
    }
    return c;
}

int main(int argc, char const *argv[])
{
    const int N = 1e2;
    int i = 0;
    clock_t start, end;
    start = clock();
    for (; i < N; i++) {
        cpp11();
    }
    end = clock();
    printf("程序运行时间为: %f s\n", ((double)(end - start)) / CLOCKS_PER_SEC / N);
    return 0;
}
```

运行结果：

```
程序运行时间：0.222540 s
```







#### 1.4. 参数说明

 `CLOCKS_PER_SEC` 在 `time.h` 中有如下定义: 

```c
#define CLOCKS_PER_SEC    ((clock_t)(1000))
```





#### 1.5. 函数返回值

 程序迄今为止所用的处理器时间。若该信息不可用，或若其值无法表示，则为 `(clock_t)(-1)` 。 







#### 1.6. 使用注意事项

只有两次对 `clock` 不同调用的返回值的差是有意义的，因为 `1clock` 时期的起始不必与程序起始一致。 `clock` 时间或许会快于或慢于挂钟时间，这取决于操作系统给予程序的执行资源。例如，若 CPU 为其他进程所共享， `clock` 时间可能慢于挂钟。另一方面，若当前进程为多线程，而有更多资源可用， `clock` 时间可能会快于挂钟。 