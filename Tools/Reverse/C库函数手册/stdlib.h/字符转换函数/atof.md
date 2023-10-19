### 1. atof 函数使用说明

atof - convert a string to a double



| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 卿俊成 | 2019.11.24 | 内容初填 |
|          |        |            |          |
|          |        |            |          |





#### 1.1. 函数原型

```c
#include <stdlib.h>
double atof (const char *__nptr);
```



#### 1.2. 功能描述

C 库函数 `atof()` 字符型的数字转化为 `double` 型的数字。





#### 1.3. 使用示例

使用 `atof()` 将含有字母及数字的混合字符串转化为浮点型数据，使用 `printf()` 打印输出数据。

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char astring[] = "The Result Is 12345.6.Next Is";
	float fstring_1 = 0;
	float fstring_2 = 0;

	fstring_1 = atof(astring);
	fstring_2 = atof(astring + 14);

	printf("原始字符串为：%s\n",astring);
	printf("字符串直接转换后为：%f\n",fstring_1);
	printf("字符串对应数字转换后为：%f\n",fstring_2);

	return 0;
}
```

运行结果：

```
原始字符串为：The Result Is 12345.6.Next Is
字符串直接转换后为：0.000000
字符串对应数字转换后为：12345.599609
```

由上述运行结果可知，当待转换字符串起始地址不是数字时，该函数并不会报错，也不会对字符串中非数字字符自动略过。当我们需要转换字符串中的某个数字时，需要手动指明对应数字的起始地址，数字之后的字母会被自动略过，因此我们只需要指明待转换数字的首地址即可。





#### 1.4. 参数说明

`atof()` 传入参数为非空指针 `*nptr`，该指针指向带转换数字的首地址。







#### 1.5. 函数返回值

- 返回值为转换后的浮点型数据。







#### 1.6. 使用注意事项

- `atof` 函数是一个线程安全函数，在多线程环境中可以放心使用。
- 由于该函数不对参数进行判断，需自行指明待转换数据中数字的首地址。
