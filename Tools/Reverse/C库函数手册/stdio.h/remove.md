#### remove函数使用说明

| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 胡松 | 2019.12.10 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |

#### 函数原型

```c
int remove(const char * filename);
```
#### 功能描述
删除`filename`指向的文件
如果该文件当前由该进程或其他进程打开，则此函数的行为是由实现定义的（特别是，POSIX系统取消链接文件名，尽管在上次运行进程关闭文件之前文件系统空间不会被回收; Windows会不允许删除文件）。
#### 使用示例
```c
#include <stdio.h>
int main(void)
{
    FILE* fp = fopen("file_remove.txt", "w"); // create file
    if(!fp) { perror("file_remove.txt"); return 1; }
    puts("Created file_remove.txt");
    fclose(fp);
 
    int rc = remove("file_remove.txt"); 
    if(rc) { perror("remove"); return 1; }
    puts("Removed file_remove.txt");
 
    fp = fopen("file_remove.txt", "r"); // Failure: file does not exist
    if(!fp) perror("Opening removed file failed");
 
    rc = remove("file_remove.txt"); // Failure: file does not exist
    if(rc) perror("Double-remove failed");
    
    getchar(); //for console pause
    return 0;
}
```
运行结果：

```
Created file_remove.txt
Removed file_remove.txt
Opening removed file failed: No such file or directory
Double-remove failed: No such file or directory
```
#### 参数说明
- `filename`：这是 C 字符串，包含了要被删除的文件名称。

#### 函数返回值

- `0`:删除成功
- `-1`:删除失败，并设置`errno`

#### 使用注意事项

- `POSIX`为这个函数的行为指定了许多额外的细节。
