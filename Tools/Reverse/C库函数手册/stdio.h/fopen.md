#### fopen函数使用说明

| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 胡松 | 2019.12.10 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |

#### 函数原型

```c
FILE *fopen(const char *filename, const char *mode);	//直到C99
FILE *fopen(const char *restrict filename, const char *restrict mode);	//自C99以来
errno_t fopen_s(FILE *restrict*restrict streamptr, const char *restrict filename, const char *restrict mode);	//自C11以来
```
#### 功能描述
1）打开由该文件指示的文件` filename `并返回指向与该文件关联的文件流的指针。` mode ` 用于确定文件访问模式。

2)  与（1）相同，出写入指向文件流的指针` streamptr `以及在运行时检测到一下错误并调用当前安装的约束处理函数：

 - ` streamptr ` 是一个空指针

 - ` filename` 是一个空指针

 - ` mode ` 是一个空指针

作为所有边界检查函数，` fopen_s ` 只是在被 ` __STDC_LIB_EXT1__ ` 实现定义 ` __STDC_WANT_LIB_EXT!__ ` 并且 ` 1 ` 在包含之前用户定义为整数常量时才能保证可用 ` <stdio.h> `。
#### 使用示例


```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE* fp = fopen("file.txt","r"); //file content: Hello world!
	if(!fp)
	{
		perror("File opening faild");
		return EXIT_FAILURE;
	}
	
	int c; //note:int, not char, required to handle EOF
	while((c = fgetc(fp)) != EOF) //standard C I/O file reading loop
	{
		putchar(c);
	}
	
	if(ferror(fp))
		puts("\nI/O error when reading\n");
	else if(feof(fp))
		puts("\nEnd of file reached successfully\n");

	fclose(fp);

    getchar(); //for console pause
    return 0;
}
```
运行结果：

```
Hello world!
End of file reached successfully
```


#### 参数说明
- `filename` :这是 C 字符串，包含了要打开的文件名称。
- `mode` :这是 C 字符串，包含了文件访问模式，模式如下：
|   模式   |    描述          |
| ---- | ---- |
|   "r"   |	打开一个用于读取的文件。该文件必须存在。      |
|   "w"   | 创建一个用于写入的空文件。如果文件名称与已存在的文件相同，则会删除已有文件的内容，文件被视为一个新的空文件。     |
|   "a"   | 追加到一个文件。写操作向文件末尾追加数据。如果文件不存在，则创建文件。     |
|   "r+"   | 打开一个用于更新的文件，可读取也可写入。该文件必须存在。     |
|   "w+"   | 创建一个用于读写的空文件。     |
|   "a+"   | 打开一个用于读取和追加的文件。     |



#### 函数返回值

- 该函数返回一个 FILE 指针。否则返回 NULL，且设置全局变量 errno 来标识错误。

#### 使用注意事项

格式`filename`是实现定义的，并不一定是指文件（例如它可能是控制台或通过文件系统API可访问的其他设备）。在支持它们的平台上，`filename`可能包括绝对或相对的文件系统路径。