### 相关的 Issue


### 原因（目的、解决的问题等）


### 描述（做了什么，变更了什么）

### 测试用例

### **标题格式说明**

- 标题采用三级标题、加粗
- 表格中的第一行标题也采用加粗格式

### **文档格式注意事项**：

- 标点的中英文格式、圆角半角
- 在中文中加入英文单词，记得单词两边要留空格。
- 示例：单词 apple 的中文意思是苹果。



### 代码风格示例：

```c
#include <stdio.h>

#define PRICE 5

int calculate_money (int weight)
{
	int money = 0;
	money = PRICE * weight; //对语句的注释示例：根据重量计算需付钱款
	return money;
} 

int main (void)
{
	int apple_weight; //对定义变量的注释示例：用户购买的苹果重量
	int pay_money = 0; //用户需要付的钱款
	
	printf ("input weight:");
	scanf ("%d", &apple_weight);  
	if (apple_weight < 0)
	{
		printf ("Your input error!\n");
	} 
	else
	{
		pay_money = calculate_money (apple_weight);
		printf ("You need pay: %d yuan\n", pay_money);		
	}
	
	return 0;
}
```

### **标识符命名**

- 标识符一般分为三类：关键字（如 int 、while）、预定义标识符（如include、define、库函数名）和用户自定义标识符（如用户自定义变量、函数名），用户自定义标识符不要与关键字、预定义标识符冲突
- 定义的宏统一用大写
- 命名统一采用下划线格式如：calculate_money，而不是类似 CalculateMoney 的驼峰命名法

### **代码排版与缩进**

- 嵌套的大括号代码块，每嵌套一层，缩进一个tab键（4个空格），括号对对齐写，而不是采用内核风格的写在行尾
- 在一个表达式中，运算符（如 *、+、=）两侧要留一个空格
- 函数名后和后面的小括号建议也留一个空格，小括号里的参数列表之间用逗号隔开，留一个空格

### **注释风格**

- 添加注释，可以帮助别人更好地理解你写的代码
- 如果函数比较复杂，代码量比较大，可以采用 /**/ 多行注释在函数开头前
- 一般采用单行注释 // 即可，注释符 // 和语句结束符 ; 之间为了美观，要空一格。

