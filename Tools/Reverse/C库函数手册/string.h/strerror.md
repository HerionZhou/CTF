### 1.`strerror`函数使用说明

定义于头文件 `<string.h>`



| 文档版本 |  作者  |  修改日期  |   备注   |
| :------: | :----: | :--------: | :------: |
|   V0.1   | 梁磊磊 | 2019.01.19 | 内容初填 |
|          |        |            |          |







### 1.1函数原型

```c
char *strerror(int errnum);
```



### 1.2功能描述

   依参数errnum 的错误代码 ，获得错误的描述字符串 ，将单纯的错误标号转为字符串描述，方便用户查找错误。 

### 1.3参数说明

 errnum：错误标号，通常用errno(标准错误号，定义在errno.h中) 

### 1.4函数返回值

 指向错误信息的[指针]（即：错误的描述字符串）。 

### 1.5程序实例



```c
#include<stdio.h>
#include<string.h>
#include<errno.h>
#include<stdlib.h>
int main(void)
{
FILE*fp;
extern int errno;
char*message;
if(NULL==(fp=fopen("/dev/dsp","r+")))
{
	printf("errno=%d\n",errno);
	message=strerror(errno);
	printf("Mesg:%s\n",message);
}
exit(0);
} 
```



输出结果：errno=2
Mesg:No such file or directory

### 1.6使用注意事项

无
