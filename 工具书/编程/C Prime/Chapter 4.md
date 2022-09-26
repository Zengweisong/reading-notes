## 字符串简介

- C语言没有专门用于存储字符串的变量类型，字符串都被存储在char类型的数组中。
- 数组的末尾位置的字符\0，这是空字符，C语言用它标记字符串的结束。它是非打印字符，其ASCII码值是0
- 数组是同类型数据元素的有序序列。
- sizeof运算符，它以字节为单位给出对象的大小
- strlen()给出字符串中的字符长度。
- sizeof会把末尾的\0也给计算上，strlen()则不会。
## 常量

- 用大写表示符号常量是C语言一贯的传统。
- 还有一个不常用的命名规定：在名称前带c或k前缀来表示常量。
- C90标准新增了const关键字，用于限定一个变量为只读。
## printf()和scanf()

- 一些转换说明：
- 一些修饰符：
- 当printf()使用%c打印336时，它只会查看存储336的2字节中的后1字节，相当于用一个整数除以256，保留其余数。
- float类型的值作为printf()参数时会被转换成double类型。
- 计算机根据变量类型把要传递的值放入栈中，然后控制转到printf()函数，该函数根据转换说明从栈中读取值。
- printf()函数有返回值，它返回打印字符的个数，如果有输出错误，printf()则返回一个负值。
- scanf()把输入的字符串转换成整数、浮点数、字符或字符串，而printf()正好相反，把整数、浮点数、字符和字符串转换成显示在屏幕的文本。
- 如果用scanf读取基本变量类型的值，在变量名前要加一个&。
- 如果是把字符串读入字符数组中，则不用，因为数组名称就是这个数组的首地址。
- scanf()函数使用空白(换行符、制表符和空格)把输入分成多个字段，只要在每个输入项之间输入至少一个换行符、空格或制表符即可。唯一例外的是%c,根据%c，scanf()会读取每个字符。
- 如果使用字段宽度，scanf()函数会在字段结尾或第一个空白字符处停止读取。
- 如果使用带多个转换说明的scanf()，C规定在第一个出错处停止读取输入。
- 当scanf()把字符串放进指定数组中时，它会在字符序列的末尾加上'\0'，让数组中的内容成为一个C字符串。
- scanf()函数允许把普通字符放在格式字符串中。除空格字符外的普通字符必须与输入字符串严格匹配。
- 如果格式化字符串中把空格放到%c的前面，scanf()便会跳过空格，从第一个非空白字符开始读取。
- scanf()函数返回成功读取的项数，如果没有读取任何项，且需要读取一个数字而用户却输入一个非数值字符串，scanf()便会返回0，当scanf()检测到“文件结尾”时，会返回EOF;
- printf()函数和scanf()函数都可以使用*修饰符来修改转换说明的含义
- printf()函数中，如果转换说明是%*d，那么参数列表中应包含*和d对应的值。
```c
int width = 3;
float num = 1.2345;
printf("%.*f",width,num);
// 1.235
```

- scanf()中的*用法：把*放在%和转换字符之间时，会使得scanf()跳过相应的输入项。
```c
char fname[30];
char lname[30];
printf("please input your lastname:\n");
scanf("%s",lname);
printf("please input your firstname:\n");
scanf("%s",fname);
printf("Hello,%s,%s",lname,fname);
```
```c
char name[30];
printf("please input your name:\n");
scanf("%s",name);
printf("\"%s\"\n",name);
printf("\"%20s\"\n",name);
printf("\"%-20s\"\n",name);
printf("\"%*s\"\n",strlen(name)+3,name);
return 0;
```
```c
  printf("please input a float num:");
  scanf("%f", &num);
  printf("The input is %.1f or %.1e.\n", num, num);
  printf("The input is %.3f or %.3e.", num, num);
```
```c
  float height;
  char name[30];
  printf("please input your height(cm) and name:");
  scanf("%f %s", &height, name);
  printf("%s,your are %.1f m tall.",name,height/100);
```
```c
  float dspeed,memory,speed;
  printf("please input your downloadspeed and the file's memory:");
  scanf("%f %f",&dspeed,&memory);
  printf("At %f megabits per second,a file of %f megabytes\n\
  downloads in %f seconds",dspeed,memory,memory/dspeed);
```
```c
  char fname[30],lname[30];
  int fnum,lnum;
  printf("please input your firstname:");
  scanf("%s",fname);
  printf("please input your lastname:");
  scanf("%s",lname);
  printf("%s %s\n",fname,lname);
  fnum = strlen(fname);
  lnum = strlen(lname);
  printf("%*d %*d",fnum,fnum,lnum,lnum);
```
```c
  double num = 1.0/3.0;
  float num1 = 1.0/3.0;
  printf("%.6f %.6f\n",num,num1);
  printf("%.12f %.12f\n",num,num1);
  printf("%.17f %.17f\n",num,num1);
  printf("%d,%d",FLT_DIG,DBL_DIG);
  return 0;
```
```c
#define GALON 3.785
#define MILES 1.609
int main()
{
  float miles, gasoline, permg;
  printf("please input your miles(miles) and The amount of gasoline consumed(galon): ");
  scanf("%f %f", &miles, &gasoline);
  permg = miles / gasoline;
  printf("The amount of gas consumed per mile is %.1f\n", permg);
  permg = miles * MILES / gasoline * GALON;
  printf("The amount of gas consumed per mile is %.1f", permg);
  return 0;
}
```
