### 1. mktime  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.11.28 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <time.h>
time_t mktime(struct tm *timeptr)
```



#### 1.2. 功能描述

 重整化表示成 `struct tm` 的本地日历时间，并将其转化成从纪元开始经过时间的 `time_t` 对象格式。 





#### 1.3. 使用示例

判断输入日期是周几

```c
#include <stdio.h>      /* printf, scanf */
#include <time.h>       /* time_t, struct tm, time, mktime */
 
int main ()
{
    time_t rawtime;
    struct tm * timeinfo;
    int year, month ,day;
    const char * weekday[] = { "周日", "周一","周二", "周三","周四",                               "周五", "周六"};
 
    /* 用户输入日期 */
    printf ("年: "); fflush(stdout); scanf ("%d",&year);
    printf ("月: "); fflush(stdout); scanf ("%d",&month);
    printf ("日: "); fflush(stdout); scanf ("%d",&day);
 
    /* 获取当前时间信息，并修改用户输入的输入信息 */
    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    timeinfo->tm_year = year - 1900;
    timeinfo->tm_mon = month - 1;
    timeinfo->tm_mday = day;
 
    /* 调用 mktime: timeinfo->tm_wday  */
    mktime ( timeinfo );
 
    printf ("那一天是：%s\n", weekday[timeinfo->tm_wday]);
 
    return 0;
}
```

运行结果：

```
年: 2018
月: 7
日: 26
那一天是：周四
```







#### 1.4. 参数说明

 `timeptr`  这是指向表示日历时间的 `time_t` 值的指针，该日历时间被分解为以下各部分。下面是 `timeptr`  结构的细节： 

```c
struct tm {
   int tm_sec;         /* 秒，范围从 0 到 59 */
   int tm_min;         /* 分，范围从 0 到 59 */
   int tm_hour;        /* 小时，范围从 0 到 23 */
   int tm_mday;        /* 一月中的第几天，范围从 1 到 31 */
   int tm_mon;         /* 月份，范围从 0 到 11 */
   int tm_year;        /* 自 1900 起的年数 */
   int tm_wday;        /* 一周中的第几天，范围从 0 到 6 */
   int tm_yday;        /* 一年中的第几天，范围从 0 到 365 */
   int tm_isdst;       /* 夏令时 */    
};
```









#### 1.5. 函数返回值

成功返回时表示从纪元开始时间的 `time_t` 对象，若 `time` 不能表示成 `time_t` 对象则返回 `-1` 。







#### 1.6. 使用注意事项

 若 `struct tm` 对象是由 `POSIX strptime`或等价的函数取得的，则 `tm_isdst` 的值不确定，并需要在调用 `mktime` 前显式设置。 