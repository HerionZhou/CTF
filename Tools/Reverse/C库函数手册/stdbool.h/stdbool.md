# stdbool.h文档说明

| 文档版本 |            作者             |  创建日期  |   备注   |
| :------: | :-------------------------: | :--------: | :------: |
|  V 0.1   | [恒成立](1332417183@qq.com) | 2019.12.27 | 创建文档 |
|          |                             |            |          |
|          |                             |            |          |

### 函数原型

在 C 中定义 `true`、`false` 及 `bool`，它们在 `C++` 中是关键词。

### 使用示例

```c
// filename : file_stdbool.c
#include <stdbool.h>
#include <stdio.h>

int main(){
	bool flag = true;
	if(flag){
		printf("The Flag is TRUE!\n");
	}else{
		printf("The Flag is FALSE!\n");
	}
	return 0;
}

```

运行输出 : 

```
// 编译环境
Linux VM-0-17-ubuntu 4.15.0-54-generic
gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)
// 编译指令
gcc file_stdbool.c -o app -lm && ./app
// 输出结果
The Flag is TRUE!
```

