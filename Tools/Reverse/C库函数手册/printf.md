# printf 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 王利涛   | 2019.11.21   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdio.h>
int printf (const char *format, ...);
int fprintf (FILE *stream, const char *format, ...);
int dprintf (int fd, const char *format, ...);
int sprintf (char *str, const char *format, ...);
int snprintf (char *str, size_t size, const char *format, ...);

#include <stdarg.h>
int vprintf (const char *format, va_list ap);
int vfprintf (FILE *stream, const char *format, va_list ap);
int vdprintf (int fd, const char *format, va_list ap);
int vsprintf (char *str, const char *format, va_list ap);
int vsnprintf (char *str, size_t size, const char *format, va_list ap);
```



### **功能描述**

C 库函数 printf() 用来格式化打印数据。在内存中存储的数据，我们可以使用不同的格式符去打印到屏幕上





### **使用示例**

分别使用不同的格式符去打印内存中的一个数据：

```c
#include <stdio.h>

int main (void)
{
	int a = 0xff223344;
	
	printf ("%d\n", a);
	printf ("%u\n", a);
	printf ("%c\n", a);
	printf ("%x\n", a);
	 
	return 0;
}
```

运行结果：

```
-14535868
4280431428
D
ff223344
```

通过运行结果，我们可以看到，虽然打印的是内存中的同一个数据，但是我们使用不同的格式符，打印的结果可能不一样。





### **参数说明**

printf 函数是一个变参函数，每次调用，可以有不同参数列表，支持不同格式的打印。我们经常使用的参数如下表格所示：



| **函数参数** | **说明**                 |
| ------------ | ------------------------ |
| %d           | 格式化打印整型数据       |
| %u           | 格式化打印无符号整型数据 |
| ...          | ...                      |
|              |                          |
|              |                          |
|              |                          |
|              |                          |
|              |                          |
|              |                          |





### **函数返回值**

- 函数运行成功，返回值为成功打印的字符个数 (不包括 \0 )
- 函数运行失败，返回值为一个负数





### **高级使用技巧**

通过 ANSI C  标准中定义的标准预定义宏，可以打印更多程序运行的信息：比如程序所在文件、函数、行号信息、程序的编译时间等

```c
#include <stdio.h>

int main (void)
{
	printf ("%s\%s:%d\n", __FILE__, __func__, __LINE__);
    printf ("build time: %s:%s\n", __DATE__, __TIME__);
    printf ("C99: %d\n",__STDC__);
	return 0;
}
```





### **使用注意事项**

- printf 函数是一个线程安全函数，在多线程环境中可以放心使用
- 转义字符问题...
- 域宽问题
- 隐式类型转换问题





### **更多使用示例**

[printf等级打印、打印开关控制视频教程](https://space.bilibili.com/382223675/channel/detail?cid=92965)