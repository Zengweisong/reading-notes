- 元组 
   - 任意对象的有序集合。
   - 通过偏移量存取
   - 属于不可变序列。
   - 固定长度，多样性，任意嵌套
   - 对象引用的数组
   - 元组的圆括号可以忽略，除了出现在一个函数调用中，或是嵌套在一个更大的表达式内。
   - 圆括号有助于增加脚本的可读性。
- 列表推导可以用在任何可迭代对象上。
- 元组的不可变性只适用于元组的顶层而非其内容，如果元组嵌套一个列表，该列表是可以改变的。
- 元组的不可变性提供了某种一致性，这样你可以确保元组在程序中不会被另一个引用修改。
- 列表适用于可能需要进行修改的有序集合，元组能够处理其他固定关系的情况。
- 具名元组
```python
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)  # Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])
```
- 文件
  - 文件迭代器最适合逐行读取
  - 内容是字符串不是对象
  - 文件是被缓冲的以及可定位的
  - close通常是可选的：回收时自动关闭。
- 常见的文件操作：
- 在Python3.0:
  - 文本文件把内容表示为常规的str字符串，自动执行Unicode编码和解码，并且默认执行行末换行。
  - 二进制文件把内容表示为一个特殊的bytes字节串类型，并且允许程序不修改地访问文件内容。
- 要转换文件所存储的列表和字典，我们可以运行eval()函数
- pickle模块可以让我们在文件中存储几乎任何Python对象的高级工具
```python
D = {'a':1,'b':2 }
F = open('datafile.pkl','wb')
import pickle
pickle.dump(D,F)
F.close()
F = open('datafile.pkl','wb')
E = pickle.load(F)
print(E)  # D = {'a':1,'b':2 }
```
- 在Python对象和文件中，JSON数据字符串之间的相互转换都是非常直接的，一旦你将JSON文本转换成Python对象之后，你就可以用一般的Python对象操作来处理数据。
- csv模块支持Python对象与XML格式的相互转换。
- struct模块能够构造并解析打包二进制数据。
```python
import struct

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)  #b'\x00\x00\x00\x07spam\x00\x08'
F.write('data')
F.close()
F = open('data.bin', 'rb')
data = F.read()
print(data)  #b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)  #(7, b'spam', 8)
print(values)
```
- 文件上下文管理器：with
  - 在所以Python版本中都能保证操作系统资源的释放，而且对于确保刷新输出文件缓冲区更加有用
- Python中的其他文件工具：
  - 标准流：在sys模块中预先打开的文件对象
  - os模块中的描述文件：文件的整数参数，能够支持如文件锁定之类的较低级工具
  - 套接字、管道和FiFO文件：用于同步进程或者通过网络进行通信的类文件对象。
  - 通过键来存取的文件：如shelve模块
  - shell命令流：如os.popen和subprocess.Popen
- 核心类型复习与总结：
  - 