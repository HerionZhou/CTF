#### fclose函数使用说明

| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 胡松 | 2019.12.10 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |

#### 函数原型

```c
int fclose(FILE * stream);
```

#### 功能描述
关闭给定的文件流，任何未写入的缓冲数据将刷新到操作系统，任何未读取的缓冲数据都将被丢弃，刷新所有的缓冲区。
无论操作是否成功，数据流不再与文件关联，并且如果使用自动分配，则由`setbuf`或分配的缓冲区`setvbuf`也会被解除关联并解除分配。
如果指针的值`stream`在`fclose`返回后使用，则行为未定义。
#### 使用示例

```c
#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    FILE* fp = fopen("file.txt", "r"); //file content:Hello world!
    if(!fp) {
        perror("File opening failed");
        return EXIT_FAILURE;
    }
 
    int c; // note: int, not char, required to handle EOF
    while ((c = fgetc(fp)) != EOF)  // standard C I/O file reading loop
    {
       putchar(c);
    }
 
    if (ferror(fp))
        puts("\nI/O error when reading\n");
    else if (feof(fp))
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
- `stream`： 这是指向`FILE`对象的指针，该 `FILE` 对象指定了要被关闭的流
#### 函数返回值

- `0`：流关闭成功；
- `EOF`：流关闭失败
