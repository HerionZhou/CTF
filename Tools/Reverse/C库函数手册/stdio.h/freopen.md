#### freopen函数使用说明

| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 胡松 | 2019.12.10 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |

#### 函数原型

```c
FILE *freopen(const char *filename, const char *mode, FILE* stream);	//直到C99
FILE *freopen(const char *restrict filename, const char *restrict mode, FILE*restrict stream);	//自C99以来
errno_t freopen_s(FILE *restrict*restrict newstreamptr, const char *restrict filename, const char *restrict mode, FILE *restrict stream);	//自C11以来
```
#### 功能描述
1）首先，试图关闭与之相关的文件`stream`，忽略任何错误。然后，如果`filename`不为`null`，则尝试打开通过`filename`使用`modeas` 指定的文件`fopen`，并将该文件与指向的文件流相关联`stream`。如果`filename`是空指针，那么函数将尝试重新打开已经关联的文件`stream`（在此情况下，它是实现定义允许哪些模式更改）。
2）与（1）相同，不同之处在于`mode`，处理方式如下，`fopen_s`指向文件流的指针被写入，`newstreamptr`并且在运行时检测到以下错误并调用当前安装的约束处理函数：

- `newstreamptr` 是一个空指针

- `stream` 是一个空指针

- `mode` 是一个空指针

作为所有的边界检查函数，`freopen_s`只能保证`__STDC_LIB_EXT1__`是由实现定义的，并且如果用户在包含之前定义`__STDC_WANT_LIB_EXT1__`为整数常量。

#### 使用示例


```c
#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    puts("stdout is printed to console");
    if (freopen("file_reopen.txt", "w", stdout) == NULL)
    {
       perror("freopen() failed");
       return EXIT_FAILURE;
    }
    puts("stdout is redirected to a file"); // this is written to file_reopen.txt
    fclose(stdout);
    
    getchar(); //for console pause
    return 0;
}
```
编译并运行上面的程序，将发下列行到标准输出`STDOUT`，运行结果：
```
stdout is printed to console
```
在调用`freopen()`之后，它会关联标准输出`STDOUT`到文件file_reopen.txt，无论我们在标准输出`STDOUT`中写了什么都会被写入file_reopen.txt，所以文件file_reopen.txt的内容如下：
```
stdout is redirected to a file
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
- `stream`: 这是指向 FILE 对象的指针，该 FILE 对象标识了要被重新打开的流。

#### 函数返回值

如果文件成功打开，则函数返回一个指针，指向用于标识流的对象。否则，返回空指针。

#### 使用注意事项
`freopen`是通过I / O操作或通过I / O操作建立后，改变流的窄/宽方向的唯一方法`fwide`。