# bsearch 函数使用说明

bsearch - binary search of a sorted array



| **文档版本** | **作者** | **修改日期** | **备注**   |
| ------------ | -------- | ------------ | ---------- |
| V0.1         | 卿俊成   | 2019.12.30   | 创建此文档 |
|              |          |              |            |
|              |          |              |            |







### **函数原型**

```c
#include <stdlib.h>

void *bsearch(const void *key, const void *base,
              size_t nmemb, size_t size,
              int (*compar)(const void *, const void *));
```



### **功能描述**

C 库函数 `bsearch()` 对 `nitems` 对象的数组执行二分查找，`base` 指向进行查找的数组，`key` 指向要查找的元素，`size` 指定数组中每个元素的大小。

数组的内容应根据 `compar` 所对应的比较函数升序排序。





### **使用示例**

```c
#include <stdlib.h>
#include <stdio.h>

struct data {
    int nr;
    char const *value;
} dat[] = {
    {1, "Foo"}, {2, "Bar"}, {3, "Hello"}, {4, "World"}
};

int data_cmp(void const *lhs, void const *rhs) 
{
    struct data const *const l = lhs;
    struct data const *const r = rhs;
 
    if (l->nr < r->nr) return -1;
    else if (l->nr > r->nr) return 1;
    else return 0;
}

int main(void) 
{
    struct data key = { .nr = 3 };
    struct data const *res = bsearch(&key, dat, sizeof dat / sizeof dat[0],
                                     sizeof dat[0], data_cmp);
    if (res) {
        printf("No %d: %s\n", res->nr, res->value);
    } else {
        printf("No %d not found\n", key.nr);
    }
}
```

运行结果：

```
No 3: Hello
```

通过运行结果，我们可以看到，通过调用 `bsearch()` 进行排序数组的二分搜索，该数组排序的方式由函数 ``compar`` 决定，由于是二分法查找，要求数组为升序排序。



### **函数返回值**

- 成功时，返回指向要查找到的元素指针。
- 失败时，返回空指针。







### **使用注意事项**

- 线程安全。

