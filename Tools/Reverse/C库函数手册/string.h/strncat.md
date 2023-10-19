### 1. `strncat`函数使用说明

定义于头文件`<string.h>`





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 梁磊磊 | 2019.12.19 | 内容初填 |
|          |        |            |          |





### 1.1原型声明

char * strncat(char *dest,const char *src,size_t n);



### 1.2功能描述

把 src 所指字符串的前n个字符添加到 dest 所指字符串的结尾处，并覆盖 dest 所指字符串结尾的'\0',从而实现字符串的连接。



### 1.3参数说明

 src 和 dest 所指内存区域不可以重叠，并且 dest 必须有足够的空间来容纳 src 的字符串。



### 1.4函数返回值

*dest



### 1.5程序实例

```c
 #include<stdio.h>
 #include<string.h>
 int main(void)
 {
 	int n;
 	char dest[20]="hello";
 	char src[10]="world";
 	strncat(dest,src,5);
 	printf("%s\n",dest);
 	return 0;
 }
```



运行结果：helloworld





### 1.6使用注意事项

strncat 函数比 strcat 函数更安全，但速度也慢一些。

strncat() 将会从字符串 src 的开头拷贝n个字符串尾部，dest 要有足够的空间来容纳要拷贝的字符串。如果n大于字符串的长度，那么仅将 src 指向的字符串内容追加到 dest 的尾部。

strncat() 会将 dest 字符串最后的'\n'覆盖掉，字符追加完成后，再追加'\n'。

