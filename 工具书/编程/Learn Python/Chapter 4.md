## 为什么要使用内置类型
- 内置对象使程序更容易编写。
- 内置对象是可扩展的组件。
- 内置对象往往比定制的数据结构更有效率。
- 内置对象是语言标准的一部分。
## Python核心数据类型

- 数字：1234，3.1415，3+4j，0b111，Decimal()，Fraction()
- 字符串：'spam'，"Bob's"，b'a\x01c'，u'sp\xc4m'
- 列表：[1,[2,3],4]，list(range(10))
- 字典：{'food':'spam','taste':'yum'}，dict(hours=10)
- 元组：(1,'spam',4,'U')，tuple('spam')，namedtuple
- 集合：set('abc')，{'a','b','c'}
- 文件：open('egg.txt')
- 其他核心类型：类型，None，布尔型
- 程序单元类型：函数，模块，类
- Python实现相关类型：已编译代码、调用栈跟踪

## 不可变性

- 数字、字符串和元组是不可变的
- 列表、字典和集合是可变的
- bytearray支持文本的原位置转换，但仅仅适用于字符编码至多8位宽的文本。
```python
B = bytearray(b'spam')
B.extend(b'eggs')
print(B.decode())  # spameggs
```
## 特定类型方法
```python
line = 'aaa,bbb,cccc,dd,\n'
print(line.split(','))  # ['aaa', 'bbb', 'cccc', 'dd', '\n']
print(line.rstrip().split(','))  # ['aaa', 'bbb', 'cccc', 'dd', '']
```

- 注意第三行代码，它在调用split()方法之前调用了rstrip()方法，Python遵循从左到右的执行顺序，每次前一步方法调用结束，都会为后一步方法调用产生一个临时对象。
- 可作用于多种类型的通用操作都是以内置函数或表达式的形式呈现的，如：len(X)，X[0]
- 类型特定的操作是以方法调用的形式出现，如：aString.upper()
## 寻求帮助

- dir函数简单地给出了方法的名称。
```python
a = "helloWorld"
print(dir(a))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
#'__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
#'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
#'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
#'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
#'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
#'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```

- help函数可以来查询它们是做什么的。
```python
a = "helloWorld"
print(help(a.count))
# Help on built-in function count:

# count(...) method of builtins.str instance
#     S.count(sub[, start[, end]]) -> int

#     Return the number of non-overlapping occurrences of substring sub in
#     string S[start:end].  Optional arguments start and end are
#     interpreted as in slice notation.
```
## 小结

- 在python中，我们编写对象接口（被支持的操作）而不是类型，这意味着，我们关注一个对象能做什么，而非它是什么。
- python中的每一样东西都是一个”对象“。
- 一个操作的意义取决于被操作的对象。
