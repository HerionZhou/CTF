### 1. strtof 函数使用说明

strtof - - convert ASCII string to floating-point number



| 文档版本 | 作者   | 修改日期  | 备注       |
| -------- | ------ | --------- | ---------- |
| V0.1     | 卿俊成 | 2019.12.1 | 创建此文档 |
|          |        |           |            |
|          |        |           |            |





#### 1.1. 函数原型

```c
#include <stdlib.h>
float strtof(const char *nptr, char **endptr);
```



#### 1.2. 功能描述

C 库函数 `strtof()` 将字符型指针指向 `*nptr` 的字符型的数字转化为 `float` 型的数字，并将该数字后的第一个字符地址传入二重指针 `**endptr` 指向的已定义字符串地址 `*endptr` 中。





#### 1.3. 使用示例

使用 `strtof()` 将含有字母及数字的混合字符串转化为浮点型数据，使用 `printf()` 打印输出数据。由于该函数存在第二个传入参数，故在其第二参数为空或非空的情况下分别测试。

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char astring[] = "The Result Is 12345.6.Next Is";
	float fstring_1 = 0;
	float fstring_2 = 0;
	float fstring_3 = 0;
	char **pp_null = NULL;
	char *next;
	
	fstring_1 = strtof(astring, pp_null);
	fstring_2 = strtof(astring + 14, pp_null);

	fstring_3 = strtof(astring +14, &next);

	printf("原始字符串为：%s\n", astring);
	printf("字符串直接转换后为：%f\n", fstring_1);
	printf("字符串对应数字转换后为(第二参数为NULL)：%f\n", fstring_2);
	printf("字符串对应数字转换后为(第二参数非NULL)：%f\n", fstring_3);
	printf("数字后的字符为：%s\n", next);

	return 0;
}
```

运行结果：

```
原始字符串为：The Result Is 12345.6.Next Is
字符串直接转换后为：0.000000
字符串对应数字转换后为(第二参数为NULL)：12345.599609
字符串对应数字转换后为(第二参数非NULL)：12345.599609
数字后的字符为：.Next Is
```

由上述运行结果可知，当待转换字符串起始地址不是数字时，该函数并不会报错，也不会对字符串中非数字字符自动略过。当我们需要转换字符串中的某个数字时，需要手动指明对应数字的起始地址，数字之后的字母会被自动略过，因此我们只需要指明待转换数字的首地址即可。

第二参数为转换为数字的字符的下一地址，由函数自行赋值，只需传入一个已经定义的字符指针的地址即可。从该字符指针打印数据即可得到数字之后的字符串（不会有数字之前的字符串出现）。





#### 1.4. 参数说明

- `*nptr`：该指针指向带转换数字的首地址。
- `**endptr`：该指正指向存放转换数字后首字符的地址。







#### 1.5. 函数返回值

- 返回值为转换后的 `float` 型数据。







#### 1.6. 使用注意事项

- `strtof` 函数是一个线程安全函数，在多线程环境中可以放心使用。
