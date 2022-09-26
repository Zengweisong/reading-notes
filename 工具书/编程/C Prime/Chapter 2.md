## 头文件
- 通常，在C程序顶部的信息集合被称为头文件。
- 头文件中可以定义一些常量，或者指明函数名以及如何使用它们。
- 头文件帮助编译器把你的程序正确地组合在一起。
- #include的#表明，C预处理器在编译器接手之前处理这条指令。
## 声明

- 关键字是语言定义的单词，不能做其他用途。
- 在C语言中，所有变量必须先声明才能使用。
- 名称的第一个字符必须是字母或下划线，不能是数字。
- C语言中名称区分大小写。
- 在执行 int num;声明时，编译器在计算机内存中为变量名num预留了空间，然后在执行赋值表达式语句时，把值存储在之前预留的位置。可以给num赋不同的值，这就是num之所以被称为变量的原因。
## 程序结构

- 程序由一个或多个函数组成，必须有main()函数
- main()函数是C程序要调用的第一个函数。
## 编程练习
```c
#include "stdio.h"
int main()
{
  printf("Zeng weisong");
  printf("\nZeng\nWeisong");
  printf("\nZeng");
  printf(" Weisong");
  return 0;
}
```
```c
#include "stdio.h"
int main()
{
  printf("My name is Zengweisong,My address is shenzhen");
  return 0;
}
```
```c
#include "stdio.h"
int main()
{
  int age = 20;
  printf("my age is %d years old,convert to day is %d days",age,age*365);
  return 0;
}
```
```c
#include "stdio.h"
void jolly();
void deny();
int main()
{
  jolly();
  jolly();
  jolly();
  deny();
  return 0;
}

void jolly()
{
  printf("For he's a jolly good fellow!\n");
}
void deny()
{
  printf("Which nobody can deny!");
}
```
```c
#include "stdio.h"
void br();
void ic();
int main()
{
  br();
  ic();
  printf("\n");
  ic();
  printf("\n");
  br();
  return 0;
}
void br()
{
  printf("Brazil,Russia");
}
void ic()
{
  printf("India,China");
}
```
```c
#include "stdio.h"

int main()
{
  int toes = 10;
  printf("toes = %d,double toes = %d Square of toes = %d",toes,toes*2,toes*toes);
  return 0;
}
```
```c
#include "stdio.h"
void smile();
int main()
{
  smile();smile();smile();
  printf("\n");
  smile();smile();
  printf("\n");
  smile();
  return 0;
}
void smile()
{
  printf("Smile!");
}
```
```c
#include "stdio.h"
void two();
void one_three();
int main()
{
  printf("starting now:\n");
  one_three();
  printf("\ndone!");
  return 0;
}
void one_three()
{
  printf("one\n");
  two();
  printf("\n");
  printf("three");
}
void two()
{
  printf("two");
}
```
