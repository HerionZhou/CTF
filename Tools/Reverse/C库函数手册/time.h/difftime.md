### 1. difftime  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.11.27 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <time.h>
double difftime (time_t time_end,time_t time_beg);
```



#### 1.2. 功能描述

以秒数计算两个作为  `time_t`  对象的日历时间的差  `(time_end - time_beg)` 。若  `time_beg` 的时间点则结果为负。





#### 1.3. 使用示例

计算从月初开始经过的秒数。

```c
#include <stdio.h>
#include <time.h>

int main(void)
{
    time_t now;
    time(&now);
 
    struct tm beg;
    beg = *localtime(&now);
 
    // 设 beg 为月初
    beg.tm_hour = 0;
    beg.tm_min = 0;
    beg.tm_sec = 0;
    beg.tm_mday = 1;
 
    double seconds = difftime(now, mktime(&beg));
 
    printf("%.f seconds have passed since the beginning of the                               month.\n",seconds);    

	return 0;
}
```

运行结果：

```
1937968 seconds have passed since the beginning of the month.
```







#### 1.4. 参数说明

`time_beg ` ,`time_end` ，指待比较的时间







#### 1.5. 函数返回值

- 两时间之差的秒数







#### 1.6. 使用注意事项

 在 POSIX 系统上 ，`time_t` 以秒计量，而 `difftime` 等价于算术减法，但 C 和 C++ 允许小数单位的 `time_t` 。