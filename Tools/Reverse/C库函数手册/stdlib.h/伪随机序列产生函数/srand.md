# srand 函数使用说明





| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.1    | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>
void srand(unsigned int seed);
```



### **功能描述**

C 库函数 `srand()` 产生伪随机数种子，该种子收到 `rand()` 函数的调用。





### **使用示例**

直接使用该函数打印随机数：

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
        int i;
        for(i = 0; i < 10; i++)
        {
                srand(i);
                printf("the rand number of %d is:%d\n", i, rand());
        }
        return 0;
}
```

运行结果：

```bash
the rand number of 0 is:1804289383
the rand number of 1 is:1804289383
the rand number of 2 is:1505335290
the rand number of 3 is:1205554746
the rand number of 4 is:1968078301
the rand number of 5 is:590011675
the rand number of 6 is:290852541
the rand number of 7 is:1045618677
the rand number of 8 is:757547896
the rand number of 9 is:444454915
```

通过运行结果，我们可以看到，当使用 `srand` 制作随机数种子，不同的随机数种子经过 `rand` 后，会生成伪随机数。





### **参数说明**

- 随机数种子






### **函数返回值**

- 无





### **使用注意事项**

- `srand` 函数是一个线程安全函数，在多线程环境中可以放心使用



