## 八进制和十六进制
- 以八进制显示数字，使用%o
- 以十六进制显示数字，使用%x
## 其他整数类型

- %hd表示以十进制显示short类型的整数
- 打印unsigned int 类型的值，使用%u转换说明
- 打印long类型的值，使用%ld转换说明。
- char是整数类型，因为char类型实际上存储的是整数而不是字符。
## 打印字符

- printf()函数中的转换说明决定了数据的显示方式，而不是数据的存储方式。
- 传递参数时，C编译器会把float类型的值自动转换为double类型。
- C99和C11提供了%zd转换说明匹配sizeof的返回类型。
- 浮点数可以有三种打印方法：
   - %f，小数形式
   - %e，指数形式
   - %a，十六进制记数法
## 使用数据类型

- 把一个类型的数值初始化给不同类型的变量时，编译器会把值转换成与变量匹配的类型，这可能会将部分数据丢失。
```c
#include <stdio.h>
int main()
{
  int cost = 12.99;
  printf("%d", cost); // 12F
	
  return 0;
}

```

- C编译器把浮点数转换为整数时，会直接丢弃（截断）小数部分，而不是进行四舍五入。
## 刷新输出

- printf()语句把输出发送到一个叫作缓冲区(buffer)的中间存储区域
- 当缓冲区满、遇到换行字符或需要输入的时候就会将缓冲区中的内容发送到屏幕上。
- 还有一种刷新缓冲区的方法是用fflush()函数。
## 编程练习
```c
#include <stdio.h>
int main()
{
  int ch;
  printf("please input a ASCII num:");
  scanf("%d",&ch);
  printf("%c",ch);
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  printf("\aStartled by the sudden sound,Sally shouted,\n\
\"By the Great Pumpkin, what was that !\"");
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  float num;
  printf("Enter a floating-point value:");
  scanf("%f",&num);
  printf("fixed-point notation:%f\n",num);
  printf("exponetial notation:%e\n",num);
  printf("p notation:%a",num);
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  long double num = 3.156E7;
  int age;
  printf("Enter your age:");
  scanf("%d",&age);
  printf("The number of seconds for your age is:%ld",age*num);
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  float quarts;
  float wm = 3E-23;
  printf("Please enter the number of quarts of water:");
  scanf("%f", &quarts);
  printf("the number of quarts is:%.1f,the number of water molecules is:%f"
  ,quarts,(quarts/wm)*950);
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  float height;
  printf("Please enter Your height(inches):");
  scanf("%f",&height);
  printf("your height is %.2f cm",height*2.54);
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  float cup;
  printf("please input the cup of number:");
  scanf("%f",&cup);
  printf("pint:%f,Oz.:%f,spoon:%f,tea spoon:%f",0.5*cup,cup*8,cup*16,cup*48);
  return 0;
}

```
                                                                              1
