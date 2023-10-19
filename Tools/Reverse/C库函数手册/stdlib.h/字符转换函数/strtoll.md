### 1. strtoll 函数使用说明

strtoll - - convert a string to a long integer



| 文档版本 | 作者   | 修改日期  | 备注       |
| -------- | ------ | --------- | ---------- |
| V0.1     | 卿俊成 | 2019.12.1 | 创建此文档 |
|          |        |           |            |
|          |        |           |            |





#### 1.1. 函数原型

```c
#include <stdlib.h>
long long int strtoll(const char *nptr, char **endptr, int base);
```



#### 1.2. 功能描述

C 库函数 `strtoll()` 将字符型指针指向 `*nptr` 的字符型的数字转化为 `long int` 型的数字，并将该数字后的第一个字符地址传入二重指针 `**endptr` 指向的已定义字符串地址 `*endptr` 中。其中，待转换数字的进制由 `base` 参数指定，将 `base` 进制的数字转换为十进制数，其有效值范围为 2 ~ 36 。





#### 1.3. 使用示例

该示例程序来自于 man 手册。

该程序的测试依赖于 main 函数的参数传递。

```c
#include <stdlib.h>
#include <limits.h>
#include <stdio.h>
#include <errno.h>

int main(int argc, char *argv[])
{
	int base;
	char *endptr, *str;
	long val;

	if (argc < 2) {
	   fprintf(stderr, "Usage: %s str [base]\n", argv[0]);
	   exit(EXIT_FAILURE);
	}

	str = argv[1];
	base = (argc > 2) ? atoi(argv[2]) : 10;

	errno = 0;    /* To distinguish success/failure after call */
	val = strtoll(str, &endptr, base);
	
	/* Check for various possible errors */

	if ((errno == ERANGE && (val == LONG_MAX || val == LONG_MIN))
		   || (errno != 0 && val == 0)) {
		perror("strtoll");
		exit(EXIT_FAILURE);
	}

	if (endptr == str) {
		fprintf(stderr, "No digits were found\n");
		exit(EXIT_FAILURE);
	}

	/* If we got here, strtoll() successfully parsed a number */

	printf("strtoll() returned %ld\n", val);

	if (*endptr != '\0')        /* Not necessarily an error... */
		printf("Further characters after number: %s\n", endptr);

	exit(EXIT_SUCCESS);
}
```

运行结果：

```bash
$ ./a.out 20astr 8
strtoll() returned 16
Further characters after number: astr

$ ./a.out 20astr 10
strtoll() returned 20
Further characters after number: astr

$ ./a.out 20astr 16
strtoll() returned 522
Further characters after number: str
```

由上述运行结果可知，当待转换字符串起始地址不是数字时，该函数并不会报错，也不会对字符串中非数字字符自动略过。当我们需要转换字符串中的某个数字时，需要手动指明对应数字的起始地址，数字之后的字母会被自动略过，因此我们只需要指明待转换数字的首地址即可。

第二参数为转换为数字的字符的下一地址，由函数自行赋值，只需传入一个已经定义的字符指针的地址即可。从该字符指针打印数据即可得到数字之后的字符串（不会有数字之前的字符串出现）。

假设数字为八进制时， `20` 处理后的结果为 `16`；数字为十进制时， `20` 处理后的结果为 `20`；数字为十六进制时， `20a` 处理后的结果为 `522`。





#### 1.4. 参数说明

- `*nptr`：该指针指向带转换数字的首地址。
- `**endptr`：该指正指向存放转换数字后首字符的地址。
- `base`：表明待转换数字的进制数，即基数。





#### 1.5. 函数返回值

- 返回值为转换后的 `long long int` 型数据。





#### 1.6. 使用注意事项

- `strtoll` 函数是一个线程安全函数，在多线程环境中可以放心使用。
