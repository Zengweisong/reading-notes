- 对于计算机科学而言，一门语言应该提供以下3种形式的程序流： 
   - 执行语句序列
   - 循环
   - 分支
- scanf()返回成功读取项的数量。
- 用一种简单的句子表示程序思路的方法，它与计算机语言的形式相对应，就叫做伪代码，伪代码的好处之一是：可以把注意力集中在程序的组织和逻辑上，不用在设计程序时还要分心如何用编程语言来表达自己的想法。
- 比较浮点数时，尽量只使用<和>。因为浮点数的舍入误差会导致在逻辑上应该相等的两数却不相等。
- 一般而言，所有非零值都视为真，只有0被视为假。
- 如果scanf()读取指定形式的输入失败，就把无法读取的输入留在输入队列中，供下次读取。
- 关系运算符的优先级比算术运算符（包括+和-）低，比赋值运算符高。
- 运算符优先级：
- for循环： 
   - 关键字for后面的圆括号中有三个表达式，分别用两个分号隔开。第一个表达式是初始化，只会在for循环开始执行一次。第二个表达式是测试条件，在执行循环之前对表达式求值。如果表达式为假，循环结束。第三个表达式执行更新，在每次循环结束时求值。
- for循环的灵活性： 
   - 可以使用递减运算符来递减计数器：

```c
#include <stdio.h>
int main()
{
  int num;
  for (num = 5; num > 0; num--)
    printf("%d\n", num);
  // 5
  // 4
  // 3
  // 2
  // 1
  return 0;
}
```

- 可以让计数器递增2、10等
- 可以用字符代替数字计数
- 除了测试迭代次数外，还可以测试其他条件
- 可以让递增的量几何增长，而不是算术增长，也就是说，每次都乘上一个而不是加上一个固定的量。
- 第三个表达式可以使用任意合法的表达式
- 可以省略一个或多个表达式，但是不能省略分号，只要在循环中包含能结束循环的语句即可。
- 省略第二个表达式会被视为真，所以下面的循环会一直运行：

```c
for (; ; )
  printf("hello");
```

- 第一个表达式不一定是给变量赋初值，也可以使用printf()，记住，在执行循环的其他部分之前，只对第一个表达式求值一次或执行一次。
- 循环体中的行为可以改变循环头中的表达式。
- 与一般形式相比，组合形式的赋值运算符生成的机器代码更高效。
- 逗号运算符的性质： 
   - 它保证了被它分隔的表达式从左往右求值（换言之，逗号是一个序列点，所以逗号左侧项的所有副作用都在程序执行逗号右侧项之前发生）。
   - 逗号也可作为分隔符。
   - 逗号运算符把两个表达式连接成一个表达式，并保证最左边的表达式最先求值。逗号运算符在for循环头的表达式中用于包含更多的信息，整个逗号表达式的值是逗号表达式右侧表达式的值。

```c
#include <stdio.h>
int main()
{
  int num;
  printf("%d\n", num = (249, 500)); // 500
  printf("%d", num);                // 500
  return 0;
}
```

- do while 循环是出口条件循环，至少执行循环体一次。
- 一般而言，当循环涉及到初始化和更新变量时，用for循环比较合适，而在其他情况下用while循环更好。
- 数组时按顺序存储的一系列类型相同的值。
- char类型的数组末尾包含一个字符串末尾的空字符\0,则该数组中的内容就构成了一个字符串。
- 用于识别数组的数字被称为下标、索引或偏移量。
- scanf()会跳过空白字符，所以可以在一行输入10个数字，也可以每行只输入一个数字。（因为输入是缓冲的，只有当用户在键入enter键后数字才会被发送给程序）
- 用#define指令创建的明示变量（SIZE）来指定数组的大小，这样就可以在定义数组和设置循环边界时使用该明示常量。
- 模块化隐含的思想是：应该把程序划分为一些独立的单元，每个单元执行一个任务。这样做提高了程序的可读性，模块化使程序的不同部分彼此独立，方便后续更新和修改程序。
- 声明函数，调用函数，定义函数，使用关键字return 都是定义和使用带返回值函数的基本要素。
- 如果把函数定义置于main()的文件顶部，就可以省略前置声明，但是这不是C的标准风格，因为main()通常只提供整个程序的框架，最好把main()放在所有函数定义的前面。
- 创建循环要注意下面三个方面： 
   - 注意循环的测试条件要能使循环结束。
   - 确保循环测试中的值在首次使用之前已初始化。
   - 确保循环在每次迭代都更新测试的值。
```c
#include <stdio.h>
int main()
{
  char alphabet[27] = "abcdefghijklmnopqrstuvwxyz";
  int i;
  for (i = 0; i < 26; i++)
  {
    printf("%c", alphabet[i]);
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i, j;
  for (i = 0; i < 6; i++)
  {
    for (j = 0; j <= i; j++)
    {
      printf("$");
    }
    printf("\n");
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i, j;
  for (i = 70; i >= 65; i--)
  {
    for (j = 70; j >= i; j--)
    {
      printf("%c", j);
    }
    printf("\n");
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i, j, count = 1;
  for (i = 65; i < 86; count += 1)
  {
    for (j = i; j < i + count; j++)
    {
      printf("%c", j);
    }
    printf("\n");
    i += count;
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i, j, k;
  char ch = 0;
  printf("please input the letter:");
  scanf("%c", &ch);
  for (i = 65; i <= ch; i++)
  {
    for (j = 65; j <= i; j++)
      printf("%c", j);
    for (k = i - 1; k >= 65; k--)
      printf("%c", k);
    printf("\n");
  }

  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i;
  int upper, lower;
  printf("please enter the Upper and lower:");
  scanf("%d,%d", &upper, &lower);
  for (i = lower; i <= upper; i++)
    printf("%d %d %d\n", i, i * i, i * i * i);
  return 0;
}

```
```c
#include <stdio.h>
#include "string.h"
int main()
{
  char ch[30];
  int i;
  printf("please input a word:");
  scanf("%s", ch);
  for (i = strlen(ch); i >= 0; i--)
    printf("%c", ch[i]);

  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  float x, y;
  int i;
  while (1)
  {
    if (scanf("%f %f", &x, &y) != 2)
      break;
    printf("%.2f\n", (x - y) / (x * y));
  }
  return 0;
}

```
```c
#include <stdio.h>
float foo(float x, float y);
int main()
{
  float num, num1;
  int i;
  while (1)
  {
    if (scanf("%f %f", &num, &num1) != 2)
      break;
    printf("%f\n", foo(num, num1));
  }
  return 0;
}
float foo(float x, float y)
{
  return (x - y) / (x * y);
}

```
```c
#include <stdio.h>
int main()
{
  int i, j;
  while (1)
  {
    printf("Enter lower and upper integar limits:");
    scanf("%d %d", &i, &j);
    if (i == j)
      break;
    printf("The sums of the squares from %d to %d is %d\n", i * i, j * j, (i * i + j * j));
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int num[8], i;
  for (i = 0; i < 8; i++)
  {
    scanf("%d", &num[i]);
  }
  for (i = 7; i >= 0; i--)
  {
    printf("%d ", num[i]);
  }

  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int i, j, k, sum = 1, sum2 = 1;
  scanf("%d", &i);
  for (j = 0; j <= i; j++)
  {
    sum += 1.0 / j;
  }
  for (j = 0, k = 0; k <= i; j += 2, k += 2)
  {
    sum2 += 1.0 / j;
    sum2 -= 1.0 / k;
  }
  printf("%d", sum);
  printf("%d", sum2);
  return 0;
}

```
```c
#include <stdio.h>
#include "math.h"
int main()
{
  int num[8], i;
  for (i = 0; i < 8; i++)
    num[i] = pow(2, i + 1);
  i = 0;
  do
    printf("%d\n", num[i]);
  while (i++ < 8);
  return 0;
}

```
```c
#include <stdio.h>
#include "math.h"
int main()
{
  double num[8], num2[8], sum = 0;
  int i;
  for (i = 0; i < 8; i++)
  {
    scanf("%lf", &num[i]);
    sum += num[i];
    num2[i] = sum;
  }
  for (i = 0; i < 8; i++)
    printf("%.2lf ", num[i]);
  printf("\n");
  for (i = 0; i < 8; i++)
    printf("%.2lf ", num2[i]);
  return 0;
}

```
```c
#include <stdio.h>
#include "string.h"
int main()
{
  char words[257], ch;
  int len, i = 0;
  while (1)
  {
    scanf("%c", &words[i]);
    if (words[i] == '\n')
      break;
    i++;
  }
    for (len = strlen(words); len >= 0; len--)
      printf("%c", words[len]);
  return 0;
}

```
```c
#include <stdio.h>
#include "string.h"
int main()
{
  float da = 100;
  float de = 100;
  int year = 1;
  do
  {
    da += 10;
    de += 0.05 * de;
    year++;
  } while (da > de);
  printf("%d", year);
  return 0;
}

```
```c
#include <stdio.h>
#include "string.h"
int main()
{
  float cl = 100;
  int year = 0;
  while (cl > 0)
  {
    cl += cl * 0.08;
    cl -= 10;
    year++;
  }
  printf("%d", year);
  return 0;
}

```
```c
#include <stdio.h>
#include "string.h"
int main()
{
  int i, friend = 5;
  for (i = 1; friend <= 150; i++)
  {
    friend = (friend - i) * 2;
    printf("%d weeks has %d friends\n", i, friend);
  }
  return 0;
}
```
