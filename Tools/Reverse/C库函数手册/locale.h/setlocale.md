### 1. setlocale  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.12.09 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <locale.h>
char* setlocale( int category, const char* locale);
```



#### 1.2. 功能描述

函数既可以用来对当前程序进行地域设置（本地设置、区域设置），也可以用来获取当前程序的地域设置信息。





#### 1.3. 使用示例

```c
#include <stdio.h>
#include <locale.h>
#include <time.h>
#include <wchar.h>
 
int main(void)
{
    // C 本地环境将为启用 UTF-8 的英文；
    // 小数点将为德文
    // 日期和时间格式将为日文
    setlocale(LC_ALL, "en_US.UTF-8");
    setlocale(LC_NUMERIC, "de_DE");
    setlocale(LC_TIME, "ja_JP");
 
    wchar_t str[100];
    time_t t = time(NULL);
    wcsftime(str, 100, L"%A %c", localtime(&t));
    wprintf(L"Number: %.2f\nDate: %Ls\n", 3.14, str);
}
```

运行结果：

```
Number: 3,14
Date: 木曜日 2019年12月09日 09時59分56秒 //输出的是当前本地时间
```







#### 1.4. 参数说明

| 参数     | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| category | 本地环境类识别符，`LC_xxx` 宏之一，可为0。                   |
| locale   | 用来设置地域设置的名称（字符串），也就是设置为哪种地域，对于不同的平台和不同的编译器，地域设置的名称可能会不同，C语言标准没有干预太多。 |







#### 1.5. 函数返回值

- 如果函数执行成功，那么返回一个指向字符串的指针，该字符串包含了当前地域设置的名称。也就是说，`setlacole()` 当前地域设置的名称返回。

- 如果函数执行失败（如 `locale` 指定的名称不存在，就会导致地域设置失败），那么返回空指针NULL。







#### 1.6. 使用注意事项

- 程序启动过程中，运行任何用户代码前会执行 `setlocale(LC_ALL,"C")` 的等价代码。尽管返回类型为 `char*` ，修改被指向的字符是未定义行为。

- 因为 `setlocale`修改影响依赖本地环境的函数执行的全局状态，故而一个线程调用它，同时另一个线程执行任何下列函数是未定义行为：`fprintf` 、 `isprint` 、 `iswdigit` 、`localeconv` 、 `tolower` 、 `fscanf` 、`ispunct` 、`iswgraph` 、`mblen` 、`toupper` 、`isalnum` 、`isspace` 、`iswlower` 、 `mbstowcs` 、`towlower` 、`isalpha` 、`isupper`、`iswprint` 、`mbtowc` 、 `towupper` 、 `isblank` 、 `iswalnum` 、`iswpunct` 、`setlocale` 、`wcscoll` 、`iscntrl` 、`iswalpha` 、`iswspace` 、`strcoll` 、 `wcstod` 、`isdigit` 、`iswblank` 、`iswupper`、`strerror` 、`wcstombs` 、`isgraph`、`iswcntrl` 、 `iswxdigit` 、`strtod` 、`wcsxfrm`、`islower`、`iswctype` 、`isxdigit` 。



#### 1.7. 知识补充

- `category` 的值使用的是 `locale.h` 中定义的宏：

| 常量    | 解释                                                         |
| -------- | ------------------------------------------------------------ |
| LC_ALL | 选择整个 C 本地环境                   |
| LC_COLLATE   | 选择 C 本地环境中的对照类别 |
| LC_CTYPE | 选择 C 本地环境中的字符分类类别    |
| LC_MONETARY | 选择 C 本地环境中的货币格式化类别     |
| LC_NUMERIC | 选择 C 本地环境中的数值格式化类别    |
| LC_TIME | 选择 C 本地环境中的时间格式化类别      |





- `locale` 用来设置地域设置的名称（字符串），也就是设置为哪种地域。

| 地域设置名称 | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| "C"          | 默认的地域设置，C语言程序启动时就使用`"C"` 地域设置。`"C"` 是一种非常中立的地域设置，不偏向任何一个地区，它会尽量少地含地域设置信息，这些只是让C语言程序能够正常运行，大多数情况下，`"C"` 仅仅是对小数点进行了设置（设置为`.`)，其他的信息被置空。 |
| " "          | 使用当前操作默认系统设置。根据操作系统的版本自动选择语言。   |
| NULL         | 不指定任何名称。此时函数不会对地域设置进行任何修改，仅仅返回当前地域设置的名称。换句话说，如果我们仅仅想知道当前使用的哪种地域设置，而不想改变它没那么就可以将 `locale` 参数设置为 NULL。 |