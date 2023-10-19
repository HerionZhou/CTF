# fegetround函数使用说明

| 文档版本 |            作者             |  修改日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|   V0.1   | [恒成立](1332417183@qq.com) | 2019.12.19 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

```c
#include <fenv.h>

int fegetround(void);//(C99起)
```

### 功能描述

试图建立等于参数 `round` 的浮点舍入方向，期待参数为浮点舍入宏之一。

返回对应当前舍入方向的浮点舍入宏。

### 使用示例

```c
// filename:file_fegetround.c
#include <stdio.h>
#include <math.h>
#include <fenv.h>
 
#pragma STDC FENV_ACCESS ON
void show_fe_current_rounding_method(void)
{
    printf("current rounding method:  ");
    switch (fegetround()) {
           case FE_TONEAREST:  printf ("FE_TONEAREST");  break;
           case FE_DOWNWARD:   printf ("FE_DOWNWARD");   break;
           case FE_UPWARD:     printf ("FE_UPWARD");     break;
           case FE_TOWARDZERO: printf ("FE_TOWARDZERO"); break;
           default:            printf ("unknown");
    };
    printf("\n");
}
 
int main(void)
{
    /* 默认舍入方法 */
    show_fe_current_rounding_method();
    printf("+11.5 -> %+4.1f\n", rint(+11.5)); /* 两整数的中央值 */
    printf("+12.5 -> %+4.1f\n", rint(+12.5)); /* 两整数的中央值 */
 
    /* 保存舍入方法。 */
    int curr_method = fegetround();
 
    /* 临时更改当前舍入方法。 */
    fesetround(FE_DOWNWARD);
    show_fe_current_rounding_method();
    printf("+11.5 -> %+4.1f\n", rint(+11.5));
    printf("+12.5 -> %+4.1f\n", rint(+12.5));
 
    /* 恢复舍入方法。 */
    fesetround(curr_method);
    show_fe_current_rounding_method(); 
 
    return 0;
}
```

输出结果：

```shell
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_fegetround.c -o app -lm && ./app
// 输出结果
current rounding method:  FE_TONEAREST
+11.5 -> +12.0
+12.5 -> +12.0
current rounding method:  FE_DOWNWARD
+11.5 -> +11.0
+12.5 -> +12.0
current rounding method:  FE_TONEAREST
```

### 参数说明

`round` : 舍入方向，浮点舍入宏之一。

### 函数返回值

1) 成功时为 0 ,否则为非零。

2) 描述当前舍入方向的浮点舍入宏，或若不能确定方向则为负值。

