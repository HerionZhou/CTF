# qsort 函数使用说明

qsort - sort an array



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void qsort(void *base, size_t nmemb, size_t size,
           int (*compar)(const void *, const void *));
```



### **功能描述**

C 库函数 `qsort()` 按照升序对 `base` 指向的给定数组进行排序。 对象数由 `nmenb` 给定，对象元素大小由 `size` 给定。排序方式由自定义函数 `compar` 给定。





### **使用示例**

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
 
int compare_ints(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}
 
int main(void)
{
    int ints[] = { -2, 99, 0, -743, 2, INT_MIN, 4 };
    int size = sizeof ints / sizeof *ints;
 
    qsort(ints, size, sizeof(int), compare_ints);
 
    for (int i = 0; i < size; i++) {
        printf("%d ", ints[i]);
    }
 
    printf("\n");
}
```

运行结果：

```
-2147483648 -743 -2 0 2 4 99
```

通过运行结果，我们可以看到，通过调用 `qsort()` 进行数组的升序输出，该数组排序的方式由函数 ``compar`` 决定。



### **函数返回值**

- 无返回值。







### **使用注意事项**

- 线程安全。

