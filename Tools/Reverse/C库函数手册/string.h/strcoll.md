### 1. `strcoll`函数使用说明

定义于头文件`<string.h>`





| 文档版本 | 作者   | 修改日期   | 备注     |
| -------- | ------ | ---------- | -------- |
| V0.1     | 梁磊磊 | 2019.12.19 | 内容初填 |
|          |        |            |          |





### 1.1原型声明

int strcoll(const char *str1, const char *str2)；



### 1.2功能描述

strcoll() 会依环境变量 LC_COLLATE 所指定的文字排列次序按ASCII字符的大小来比较 str1 和 str2 字符串。

 默认情况下，LC_COLLATE 为"POSIX"或"C"，。

 对于设置了 LC_COLLATE 语言环境的情况下，则根据 LC_COLLATE 设置的语言排序方式进行比较。例如，汉字会根据拼音进行比较。

### 1.3参数说明

src和dest所指内存区域不可以重叠，并且dest必须有足够的空间来容纳src的字符串。



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

strncat函数比strcat函数更安全，但速度也慢一些。

strncat()将会从字符串src的开头拷贝n个字符串尾部，dest要有足够的空间来容纳要拷贝的字符串。如果n大于字符串的长度，那么仅将src指向的字符串内容追加到dest的尾部。

strncat()会将dest字符串最后的'\n'覆盖掉，字符追加完成后，再追加'\n'。

