

### 1. localeconv  函数使用说明





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 范东洋 | 2019.12.09 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <locale.h>
struct lconv *localeconv(void);
```



#### 1.2. 功能描述

函数用来返回区域设置（地域设置、本地设置）中与数字和货币有关信息。函数获得指向 `struct lconv` 类型静态指针，该对象表示当前 C 本地环境的数值和货币格式化规则。





#### 1.3. 使用示例

```c
#include <locale.h>
#include <stdio.h>
 
int main(void)
{
    setlocale(LC_ALL, "ja_JP.UTF-8");
    struct lconv* lc = localeconv();
    printf("Japanese currency symbol: %s(%s)\n", lc->currency_symbol, lc->int_curr_symbol);
}
```

运行结果：

```
Japanese currency symbol: ￥(JPY)
```







#### 1.4. 参数说明
无







#### 1.5. 函数返回值

指向当前 `struct lconv` 对象的指针。







#### 1.6. 使用注意事项

-  通过返回的指针修改对象是未定义行为。 

-  `localeconv` 修改静态对象，从不同线程调用它而不同步是未定义行为。 



#### 1.7. 知识补充

`struct lconv`  含有 C 本地环境定义的数值和货币格式化规则。此结构体的对象可由 `localeconv`获得。 `std::lconv` 的成员为 `char` 类型和 `char*` 类型值。除了 `decimal_point` ，每个 `char*` 成员都可以指向空字符（即为空 C 字符串）。 char 类型成员均为非负数，而且若任一者在当前 C 本地环境中不可用，则为 `CHAR_MAX` 。 

##### 成员对象

######  非货币数值格式化参数

|参数 | 解释              |
| ------------------- | ---------------------------------------------- |
| char* decimal_point | 用作小数点的字符  (公开成员对象)               |
| char* thousands_sep | 用于在小数点前分隔数位组的字符  (公开成员对象) |
| char* grouping      | 字符串，其元素指示数位组的大小  (公开成员对象) |




######  货币数值格式化参数
|参数 | 解释              |
| ----------------------- | ---------------------------------------------- |
| char* mon_decimal_point | 用作小数点的字符  (公开成员对象)               |
| char* mon_thousands_sep | 用于在小数点前分隔数位组的字符  (公开成员对象) |
| char* mon_grouping      | 字符串，其元素指示数位组的大小  (公开成员对象) |
| char* positive_sign     | 用于指示非负货币量的字符串  (公开成员对象)     |
| char* negative_sign     | 用于指示负货币量的字符串  (公开成员对象)       |



######  本地货币数值格式化参数
|参数 | 解释              |
| --------------------- | ------------------------------------------------------------ |
| char* currency_symbol | 当前 C 本地环境中用于通货的符号  (公开成员对象)              |
| char frac_digits      | 货币量中小数点后显示的位数  (公开成员对象)                   |
| char p_cs_precedes    | 若 currency_symbol 置于非负值前则为 1 ，于其后则为 0  (公开成员对象) |
| char n_cs_precedes    | 若 currency_symbol 置于负值前则为 1 ，于其后则为 0  (公开成员对象) |
| char p_sep_by_space   | 指示 `currency_symbol` 、 `positive_sign` 及非负货币值的分隔  (公开成员对象) |
| char n_sep_by_space   | 指示 `currency_symbol` 、 `positive_sign` 及负货币值的分隔  (公开成员对象) |
| char p_sign_posn      | 指示非负货币值中 `positive_sign` 的位置  (公开成员对象)      |
| char n_sign_posn      | 指示负货币值中 `negative_sign` 的位置  (公开成员对象)        |




######  国际货币数值格式化参数
|参数 | 解释              |
| ---------------------------- | ------------------------------------------------------------ |
| char* int_curr_symbol        | 当前 C 本地环境中用作国际通货名的字符串  (公开成员对象)      |
| char int_frac_digits         | 国际货币量中小数点后显示的位数  (公开成员对象)               |
| char int_p_cs_precedes(C99)  | 若 int_curr_symbol 置于非负值前则为 1 ，于其后则为 0  (公开成员对象) |
| char int_n_cs_precedes(C99)  | 若 int_curr_symbol 置于负值前则为 1 ，于其后则为 0  (公开成员对象) |
| char int_p_sep_by_space(C99) | 指示 `int_curr_symbol` 、 `positive_sign` 及非负国际货币值的分隔  (公开成员对象) |
| char int_n_sep_by_space(C99) | 指示 `int_curr_symbol` 、 `positive_sign` 及负国际货币值的分隔  (公开成员对象) |
| char int_p_sign_posn(C99)    | 指示非负国际货币值中 `positive_sign` 的位置  (公开成员对象)  |
| char int_n_sign_posn(C99)    | 指示负国际货币值中 `positive_sign` 的位置  (公开成员对象)    |