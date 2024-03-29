- 在混合类型的表达式中，Python首先将被操作的对象转换成其中最复杂的操作数的类型，然后再对相同类型的操作数进行数学运算。
- 混合类型转换仅适用于数值类型（整数、浮点数、复数）
- 多态指的是：操作的意义由操作对象来决定。
- 浮点数因为有限的比特位数，并不能精确地表示某些值的事实
- 在python中： 
   - 变量在第一次赋值时被创建。
   - 变量在表达式中使用时，会被替换成它们的值。
   - 变量在表达式中使用之前，必须已被赋值。
   - 变量引用对象，而且从不需要事先声明。
- str 和 repr 的显示格式 
   - 从技术上来说，就是print和默认的交互式命令的区别。
   - repr会产生看起来像代码的结果。
   - str转换为一种通常对用户更加友好的形式。
- 十六进制、八进制、二进制 
   - oct函数会将十进制数转换为八进制数。
   - hex函数会将十进制数转换为十六进制数。
   - bin函数会将十进制数转换为二进制数。
   - 内置函数int会将一个数字的字符串转换为一个整数，并能通过可选的第二位参数来确定转换后数字的进制。
```python
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
# 64 64 64 64
```

   - **可以使用eval函数来表示**
```python
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
# 64 64 64 64
```

   - **也可以使用字符串格式化的方式**
```python
print('{0:o},{1:x},{2:b}'.format(64,64,64))
# 100,40,1000000
print('%o,%x,%x,%X' % (64, 64, 255, 255))
# 100,40,ff,FF
```

- 内置函数pow和abs分别用于计算幂和绝对值。
- 函数round会四舍六入并舍弃小数位数，但仍会在内存中产生一个浮点数结果
- 字符串格式化则会产生一个字符串
- python2.4引入了小数对象，正式名称是：Decimal，小数是精度固定的浮点数。
- 当你在表达式中混合使用不同精度的小数时，python会自动转换为最高精度的小数位数
- decimal模块中的getcontext().prec函数可以指定小数的位数
```python
import decimal
print(decimal.Decimal(1)/decimal.Decimal(7))
# 0.1428571428571428571428571429
decimal.getcontext().prec = 4
print(decimal.Decimal(1)/decimal.Decimal(7))
# 0.1429
```

- Python2.6和3.0引入了分数，名称为：Fraction，它显式地保持了一个分子和一个分母，从而避免了浮点数运算地某些不精确性和局限性。
```python
from fractions import Fraction
x = Fraction(1, 3)
y = Fraction(4, 6)
print(y)  # 2/3
print(x+y, x-y, x*y)  # 1 -1/3 2/9
```

- 还可以用浮点字符串直接创建
```python
z = Fraction('.25')
print(z)  # 1/4
a = Fraction('1.25')
print(a)  # 5/4
print(Fraction('.25')+Fraction('1.25'))  # 3/2
```

- 集合 
   - 集合只能包含不可变的数据类型
   - 函数frozenset会创建一个不可变的集合，该集合不可修改，并且可以嵌套到其他集合中。
   - 集合是无序的，顺序在集合中并不重要。
- 布尔型 
   - 只包含True和False两个值。
   - 是整数1和0的定制版。
