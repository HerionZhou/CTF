### 1. `stddef` 函数使用说明

定义于头文件` <stddef.h>`



| 文档版本 |   作者   |  修改日期  |     备注     |
| ------------- | ---------- | -------------- | ------------- |
| V0.1         |  [饕餮人](admin@taotieren.com)  | 2019.12.1 | 内容初填 |
|                  |              |                    |                  |
|                  |              |                    |                  |





#### 1.1. 函数原型
- <无>



#### 1.2. 功能描述

`stddef .h` 头文件定义了各种变量类型和宏。这些定义中的大部分也出现在其它头文件中。

下面是头文件 `stddef.h` 中定义的变量类型：

| 变量          | 描述                                                                                    | 备注 |
| :------------ | :------------------------------------------------------------------------ | :------ |
| `ptrdiff_t`  | 这是有符号整数类型，它是两个指针相减的结果。    |          |
| `size_t`     | 这是无符号整数类型，它是 `sizeof` 关键字的结果。 |          |
| `wchar_t` | 这是一个宽字符常量大小的整数类型。	                     |          |


下面是头文件 `stddef.h` 中定义的宏：

| 宏                                                            | 描述                                                                                                                                                                                                                                                                                                        | 备注 |
| :-------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `NULL`                                                    | 这个宏是一个空指针常量的值。                                                                                                                                                                                                                                                        |          |
| `	offsetof(type, member-designator)` | 这会生成一个类型为 `size_t` 的整型常量，它是一个结构成员相对于结构开头的字节偏移量。<br>成员是由 `member-designator` 给定的，结构的名称是在 `type` 中给定的。 |          |





#### 1.3. 使用示例

- <无>






#### 1.4. 参数说明
- <无>








#### 1.5. 函数返回值
- <无>








#### 1.6. 使用注意事项
- <无>
