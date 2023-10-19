#### rename函数使用说明

| 文档版本 | 作者 | 修改日期   | 备注       |
| -------- | ---- | ---------- | ---------- |
| V0.1     | 胡松 | 2019.12.10 | 创建此文档 |
|          |      |            |            |
|          |      |            |            |

#### 函数原型

```c
int rename(const char *old_filename, const char *new_filename);
```
#### 功能描述
更改文件的文件名。
该文件由指向的字符串标识`old_filename`。新文件名由指向的字符串标识`new_filename`。
如果`new_filename`存在，则行为是实现定义的。
#### 使用示例

```c
#include <stdio.h>
int main(void)
{
    FILE* fp = fopen("file_name.txt", "w"); // create file "file_name.txt"
    if(!fp) { perror("file_name.txt"); return 1; }
    fputc('a', fp); // write to "file_name.txt"
    fclose(fp);
 
    int rc = rename("file_name.txt", "file_rename.txt");
    if(rc) { perror("rename"); return 1; }
 
    fp = fopen("file_rename.txt", "r");
    if(!fp) { perror("file_rename.txt"); return 1; }
    printf("%c\n", fgetc(fp)); // read from "to.txt"
    fclose(fp);
    
    getchar(); //for console pause
    return 0;
}
```

运行结果：

```
a
```
#### 参数说明
|函数参数|说明|
|--------|---------|
|old_filename|指向包含标识要重命名的文件的路径的以null结尾的字符串的指针|
|new_filename|指向包含文件新路径的以null结尾的字符串的指针|

#### 函数返回值

- 函数运行成功，返回值`0`；
- 函数运行失败，返回`-1`,并设置`errno`。

#### 使用注意事项
`POSIX`指定了该函数语义的许多附加细节。