- 函数（function）是完成特定任务的独立程序代码单元。
- 为什么要使用函数？首先，使用函数可以省去编写重复代码的苦差。如果程序要多次完成某项任务，那么只需编写一个合适的函数，就可以在需要时使用这个函数，或者在不同的程序中使用该函数，就像许多程序中使用putchar()一样。其次，即使程序只完成某项任务一次，也值得使用函数。因为函数让程序更加模块化，从而提高了程序代码的可读性，更方便后期修改、完善。
- 描述性的函数名能清楚地表达函数的用途和组织结构。
- 许多程序员喜欢把函数看作是根据传入信息（输入）及其生成的值或响应的动作（输出）来定义的“黑盒”。如果不是自己编写函数，根本不用关心黑盒的内部行为。例如，使用printf()时，只需知道给该函数传入格式字符串或一些参数以及printf()生成的输出，无需了解printf()的内部代码。以这种方式看待函数有助于把注意力集中在程序的整体设计，而不是函数的实现细节上。因此，在动手编写代码之前，仔细考虑一下函数应该完成什么任务，以及函数和程序整体的关系。
- 实参可以是符号常量、变量和表达式。
- 和定义在函数中变量一样，形式参数也是局部变量，属该函数私有。这意味着在其他函数中使用同名变量不会引起名称冲突。每次调用函数，就会给这些变量赋值。
- ANSI C要求在函数形参的每个变量前都声明其类型。
- 简而言之，形式参数是被调函数（called function）中的变量，实际参数是主调函数（calling function）赋给被调函数的具体值。
- 因为被调函数使用的值是从主调函数中拷贝而来，所以无论被调函数对拷贝数据进行什么操作，都不会影响主调函数中的原始数据。
- 调用函数时，创建了声明为形式参数的变量并初始化为实际参数的求值结果。
- 返回值不仅可以赋给变量，也可以被用作表达式的一部分。
- 返回值不一定是变量的值，也可以是任意表达式的值。
- 实际得到的返回值相当于把函数中指定的返回值赋给与函数类型相同的变量所得到的值。
- 使用return语句的另一个作用是，终止函数并把控制返回给主调函数的下一条语句。
- return;这条语句会导致终止函数，并把控制返回给主调函数。因为return后面没有任何表达式，所以没有返回值，只有在void函数中才会用到这种形式。
- 函数类型指的是返回值的类型，不是函数参数的类型。
- 函数原型要声明在第一次使用该函数前。
- 主调函数把它的参数存储在被称为栈（stack）的临时存储区，被调函数从栈中读取这些参数。
- 当float类型被作为参数传递时会被升级为double类型。
- 如果参数的类型不匹配，编译器会把实际参数的类型转换为形式参数的类型。
- 之所以使用函数原型，是为了让编译器在第1次执行到该函数之前就知道如何使用它。
- 递归和循环的选择
  - 一般而言，选择循环比较好。首先，每次递归都会创建一组变量，所以递归使用的内存更多，而且每次递归调用都会把创建的一组新变量放在栈中。递归调用的数量受限于内存空间。其次，由于每次函数调用要花费一定的时间，所以递归的执行速度较慢。
- 递归既有优点也有缺点。优点是递归为某些编程问题提供了最简单的解决方案。缺点是一些递归算法会快速消耗计算机的内存资源。另外，递归不方便阅读和维护。
- main()函数是否与其他函数不同？是的，main()的确有点特殊。当main()与程序中的其他函数放在一起时，最开始执行的是main()函数中的第1条语句，但是这也是局限之处。main()也可以被自己或其他函数递归调用—尽管很少这样做。
- 更好的做法是，把#define指令放进头文件，然后在每个源文件中使用#include指令包含该文件即可。
- 把函数原型和已定义的字符常量放在头文件中是一个良好的编程习惯。
- 如果主调函数不使用return返回的值，则必须通过地址才能修改主调函数中的值。
- 指针（pointer）是一个值为内存地址的变量（或数据对象）。正如char类型变量的值是字符，int类型变量的值是整数，指针变量的值是地址。
- 因为声明指针变量时必须指定指针所指向变量的类型，因为不同的变量类型占用不同的存储空间，一些指针操作要求知道操作对象的大小。另外，程序必须知道存储在指定地址上的数据类型。
- 类型说明符表明了指针所指向对象的类型，星号（*）表明声明的变量是一个指针。int *pi;声明的意思是pi是一个指针，\*pi是int类型
- 编写程序时，可以认为变量有两个属性：名称和值（还有其他性质，如类型，暂不讨论）。计算机编译和加载程序后，认为变量也有两个属性：地址和值。地址就是变量在计算机内部的名称。
- 普通变量把值作为基本量，把地址作为通过&运算符获得的派生量，而指针变量把地址作为基本量，把值作为通过*运算符获得的派生量。