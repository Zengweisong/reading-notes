-  左值是C语言的术语，用于标识特定数据对象的名称或表达式。 
-  对象指的是实际的数据存储，而左值是用来标识或定位存储位置的标签。 
-  右值指的是能赋值给可修改左值的量，且本身不是左值。 
-  赋值的顺序是从右往左。 
-  整数除法结果的小数部分被丢弃，这一过程被称为截断。 
-  浮点数和整数混合运算的时候，编译器会将两个运算对象转换成相同的类型。 
-  C99标准前，C语言给语言的实现者留有一点空间，不同的实现采用不同的方法，但是C99规定使用趋零截断。 
-  运算符优先级： 
-  结合律只适用于共享同一运算对象的运算符。例如：表达式12/3*2中，共享运算对象是3,因此，从左往右的结合律在这种情况起作用。 
-  sizeof运算符以字节为单位返回运算对象的大小；运算对象可以是具体的数据对象或类型。如果运算对象是类型，则必须要用圆括号将其括起来。 
-  C语言规定，sizeof返回size_t类型的值 
-  C头文件系统可以使用typedef把size_t作为unsigned int 或 unsigned long的别名 
-  如果第1个运算对象是负数，那么求模的结果为负数；反之亦然。 
```c
//正负求模运算
```

-  递增运算符使得程序更为简洁，可读性更高，通常它生成的机器语言代码效率更高。 
-  ++的后缀形式是先使用该值，再递增，前缀则相反。 
```c
//一段前缀和后缀的区别
```

- 递增运算符只能影响一个变量
- 编译器可以自行选择先对函数中的哪个参数求值，这样做提高了编译器的效率。
- 如果一个变量出现在一个函数的多个参数中或多次出现在一个表达式中，不要对该变量使用递增或递减运算符。
- 表达式由运算符和运算对象组成。
- 每一个表达式都有一个值
- 语句是C程序的基本构建块，一条语句相当于一条完整的计算机指令
- 声明创建了名称和类型，并为其分配内存位置。
- 序列点是程序执行的点，在该点上，所有的副作用都在进入下一步之前发生。
- 语句的分号标记了一个序列点。一个完整表达式的结束也是一个序列点。
- 不是另一个更大的表达式的子表达式就是完整表达式。例：表达式语句中的表达式和while循环作为测试条件的表达式。
- 缩进对编译器不起作用，编译器通过花括号和while循环的结构来识别和解释指令。
- 涉及到两种类型的运算，两个值会被分别转换成两种类型的更高级别
- 类型的级别由高到低依次是：long double、double、float、unsigned longlong、longlong、unsigned long、long、unsigned int、int。
- 当作为函数参数传递时，char和short被转换成int，float被转换成double。
- 目标类型时无符号整型，且待赋的值是整数时，额外的位将被忽略，例如：如果目标类型是8位un-signed char,待赋的值是原始值求模256
- 变量名是函数私有的，即在函数中定义的变量名不会和别处的相同名称发生冲突。
```c
#include <stdio.h>
int main()
{
  const int m_h = 60;
  int min;
  do
  {
    printf("please input a number:");
    scanf("%d", &min);
    if (min <= 0)
      break;
    printf("%d hours %d minutes\n", min / m_h, min % m_h);
  } while (min > 0);
  return 0;
}
```
```c
#include <stdio.h>
int main()
{
  int num;
  int flag = 0;
  printf("please input a number:");
  scanf("%d", &num);
  while (flag++ <= 10)
  {
    printf("%d ", num++);
  }
  return 0;
}

```
```c
#include <stdio.h>
int main()
{
  int day;
  const int week = 7;
  do
  {
    printf("please input a day:");
    scanf("%d", &day);
    if (day <= 0)
      break;
    printf("%d days are %d week,%d days\n", day, day / week, day % week);
  } while (day > 0);

  return 0;
}
```
```c
#include <stdio.h>
const float inches = 0.39;
const float feet = 0.032;
int main()
{
  float height = 0;
  while (1)
  {
    printf("Enter a height in cm:");
    scanf("%f", &height);
    if (height < 0)
    {
      printf("bye\n");
      break;
    }
    printf("%.1f cm = %.1f feet,%.1f inches\n", height, height * feet, height * inches);
  }

  return 0;
}

```
```c
#include <stdio.h>
const float inches = 0.39;
const float feet = 0.032;
int main()
{
  int count = 0, sum = 0, day;
  printf("please input a day:");
  scanf("%d", &day);
  while (day--)
  {
    count++;
    sum += count;
  }
  printf("%d", sum);
  return 0;
}
```
```c
#include <stdio.h>
const float inches = 0.39;
const float feet = 0.032;
int main()
{
  int count = 0, sum = 0, day;
  printf("please input a day:");
  scanf("%d", &day);
  while (day--)
  {
    count++;
    sum += (count * count);
  }
  printf("%d", sum);
  return 0;
}

```
```c
#include <stdio.h>
void cubic(double num);
int main()
{
  double c_num;
  printf("please input a double number:");
  scanf("%lf", &c_num);
  cubic(c_num);
  return 0;
}
void cubic(double num)
{
  printf("%f",num*num*num);
}
```
```c
#include <stdio.h>
int main()
{
  int second, first;
  printf("Enter an integer to serve as the second operand:");
  scanf("%d", &second);
  while (1)
  {
    printf("Now enter the first operand:");
    scanf("%d", &first);
    if (first <= 0)
      break;
    printf("%d %% %d is %d\n", first, second, first % second);
  }
  printf("Done!");
  return 0;
}
```
```c
#include <stdio.h>
void Temperatures(float temp);
int main()
{
  float hua;
  while (1)
  {
    printf("Enter an temperture(hua):");
    if (!(scanf("%f", &hua)) || hua == 'q')
      break;
    Temperatures(hua);
  }

  return 0;
}
void Temperatures(float temp)
{
  const float sheshi = (temp - 32) /1.8;
  const float kai = sheshi + 273.16;
  printf("%f,%f,%f\n", temp, sheshi, kai);
}
```
