## 序列操作
  任何序列（或者可迭代对象）都可以通过一个赋值操作来分解为单独的变量，**唯一的要求就是变量的总数要与序列相吻合**
  ```python
    temp = (4,5)
    a,b = temp
    print(a)  # 4 
    print(b)  # 5
  ```
  只要对象是可迭代的（字符串，文件，迭代器，生成器），就可以执行分解操作
  ```python
  strings = 'Hello'
  a, b, c, d, e = strings
  print(a, b, c, d, e)  # H e l l o
  ```
  如果想丢弃某些特定的值，可以选一个用不到的变量名，**但是请确保该变量名没有用过**
  ```python
  data = ['zws', '0828', 27, 3]
  name, _, num, _ = data
  print(name, num)  # zws 27
  ```
  从任意长度的可迭代对象中分解元素
  ```python
  def avg_score(grades):
      first,*middle,last = grades  
      return middle  
  print(avg_score([99,95,94,92,80,75,60,59,0]))  #[95,94,92,80,75,60,59]
  ```
  使用**collection.deque**保留最后的N个元素:
  ```python
  from collections import deque
  q = deque(maxlen = 3)  # 设置了该队列的长度，当有新数据加入而队列已满时会自动移除数据最老的那条
  for i in range(10):
      q.append(i)
  print(q)  # deque([7, 8, 9], maxlen=3)
  ```
  deque同时也是一个简单队列
  ```python
  from collections import deque
  q = deque()
  for i in range(5):
      q.append(i)
  print(q)  # deque([0, 1, 2, 3, 4])
  q.appendleft(5) 
  print(q)  # deque([5, 0, 1, 2, 3, 4])
  q.pop()  # 4
  q.popleft()  # 5
  print(q)  # deque([0, 1, 2, 3])
  ```
  使用**heapq模块**找到最大或最小的N个元素
  heapq模块中有**nlargest**()和**nsmallest**()两个函数
  ```python
  import heapq
  nums = [1, 4, 3, 9, 6, -2, 99, -7, 8, ]
  print(heapq.nlargest(3, nums))  # [99, 9, 8]
  print(heapq.nsmallest(3, nums))  # [-7, -2, 1]
  ```
  这两个函数都可以接受一个参数key,从而允许它们工作在更加复杂的数据结构之上
  ```python
  import heapq

  books = [
      {"name": '红楼梦', "price": 100, "author": '曹雪芹'},
      {"name": '三体', "price": 90, "author": '刘慈欣'},
      {"name": '百年孤独', "price": 120, "author": '加西亚马尔克斯'},
      {"name": '明朝那些事儿', "price": 110, "author": '当年明月'},
      {"name": '围城', "price": 115, "author": '钱钟书'},
  ]
  cheap = heapq.nsmallest(1, books, key=lambda s: s['price'])
  expensive = heapq.nlargest(1, books, key=lambda s: s['price'])
  print(cheap[0]['name'])  # 三体
  print(expensive[0]['name'])  # 百年孤独
  ```
  heapq模块还可以用来实现**优先级队列**,拥有相同优先级的元素，返回的顺序与他们插入到队列的顺序相同。
  ```python
  class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('a'), 4)
q.push(Item('b'), 3)
q.push(Item('c'), 9)
q.push(Item('d'), 6)
q.push(Item('e'), 3)
print(q.pop())  # Item('c')
print(q.pop())  # Item('d')
print(q.pop())  # Item('a')
print(q.pop())  # Item('b')
print(q.pop())  # Item('e')
  ```
在上面的代码中，队列以元组（-priority,index,item）的形式组成，把priority取负值是为了能让队列按照元素的优先级从高到底排列，这与正常的堆排列顺序相反，一般情况下堆是按从小到大的顺序排序的。

变量index的作用是为了将具有相同优先级的元素以适当的顺序排列，通过维护一个不断递增的索引，元素将以它们入队列时的顺序来排列。

**通过collections模块中的defaultdict类来实现在字典中的键映射多个值**
```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

d = defaultdict(set)
d['a'].add(1)
d['b'].add(2)
d['b'].add(3)
```
当然你也可以在普通的字典上用setdefault()方法来取代
```python
d = {}  # 一个普通的字典
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('a',[]).append(4)
```
初始化时,defaultdict的好处就显现出来了
```python
from collections import defaultdict
temp = [(1, 1), (2, 3), (5, 8), (13, 21)]
# 普通字典初始化
d = {}
for key, value in temp:
    if key not in d:
        d[key] = []
    d[key].append(value)

# defaultdict 初始化
d = defaultdict(list)
for key, value in temp:
    d[key].append(value)
```
**对字典进行计算(最大最小值,排序等)**
```python
d = {
    "红楼梦": 55,
    "三体": 90,
    "百年孤独": 45,
    "围城": 50,
    "飘": 40
}
# 我们通常会用zip函数将字典的键和值反转过来
min_price = min(zip(d.values(), d.keys()))
print(min_price)  # (40, '飘')
max_price = max(zip(d.values(), d.keys()))
print(max_price)  # (90, '三体')
```
同样的,要对数据排序只需要使用zip()再配合sorted()就可以了
```python
price_sorted = sorted(zip(d.values(), d.keys()))
print(price_sorted)
# [(40, '飘'), (45, '百年孤独'), (50, '围城'), (55, '红楼梦'), (90, '三体')]
```
zip函数只是创建了一个迭代器,它的内容只能被消费一次
```python
price_and_names = zip(d.values(), d.keys())
print(min(price_and_names))  # (40, '飘')
print(max(price_and_names))  # ValueError: max() arg is an empty sequence
```
**在两个字典中寻找相同点**,注意:字典的values()方法不支持集合操作
```python
a = {
    'x': 2,
    'y': 4,
    'z': 6,
}
b = {
    'w': 4,
    'x': 3,
    'y': 9,
    'z': 6,
}
# 查找相同的键
print(a.keys() & b.keys())  # {'x', 'y', 'z'}
# 查找在b字典却不在a字典的键
print(b.keys()-a.keys())  # {'w'}
# 查找ab字典中相同的键值对
print(a.items() & b.items())  # {('z', 6)}
```
使用字典推导式去掉某些不用的键
```python
c = {key: b[key] for key in b.keys()-{'z', 'w'}}
print(c)  # {'x': 3, 'y': 9}
```
**从序列中移除重复项且保持元素间顺序不变**
* 如果序列中的值是可哈希(在生存期内不可变,需要有一个__hash__方法,例如:整数,浮点数,字符串,元组)的:
  ```python
  def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    
  a=[1,4,3,9,6,2,2,0,0]
  print(list(dedupe(a)))  # [1, 4, 3, 9, 6, 2, 0]
  ```
* 如果想在不可哈希的对象序列中去重,需要对上述代码稍作修改
  ```python
  def dedupe(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
  a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
  print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
  print(list(dedupe(a, key=lambda d: (d['x']))))
  ```
 * 如果仅仅是想去重,且不考虑顺序的话,那么集合是你更好的选择.
    ```python
    a = [1, 4, 3, 9, 6, 2, 2, 0, 0]
    print(set(a))  # {0, 1, 2, 3, 4, 6, 9}
    ```

**对切片命名**
```python
items = [x for x in range(10)]
a = slice(2, 4)
print(items[2:4])  # [2, 3]
print(items[a])  # [2, 3]
items[a] = [10, 11]
print(items)  # [0, 1, 10, 11, 4, 5, 6, 7, 8, 9]
```
如果有一个slice对象的实例s,我们还可以通过s.start,s.stop,s.step 来获取这个实例的信息
```python
a = slice(10, 50, 2)
print(a.start, a.stop, a.step)  # 10 50 2
```
**找出序列中出现最多的元素**
```python
from collections import Counter
result = ['idly', 'glow', 'idly', 'isolation', 'glow', 'glow', 'ideal', 'locality', 'imaginary', 'heap', 'imaginary', 'imaginary', 'heap', 'locality', 'idly', 'heap', 'idly', 'glow', 'imaginary', 'ideal', 'miserable', 'heap', 'locality', 'isolation', 'idly',
          'isolation', 'ideal', 'imaginary', 'heap', 'isolation', 'miserable', 'idly', 'ideal', 'isolation', 'ideal', 'imaginary', 'miserable', 'heap', 'locality', 'ideal', 'locality', 'glow', 'glow', 'glow', 'miserable', 'imaginary', 'idly', 'idly', 'heap', 'glow']
words = Counter(result)
print(words.most_common(3))  # [('idly', 8), ('glow', 8), ('imaginary', 7)] 
```
可以给Counter对象提供任何可哈希的对象序列作为输入,在底层的实现中,Counter是一个字典,在元素和它们出现的次数做了映射.例如:
```python
print(words['idly'])  # 8
print(words['miserable'])  # 4
```
如果想要手动增加计数,只需要简单自增即可
```python
morewords = ['idly', 'glow', 'imaginary', 'heap',
             'ideal', 'isolation', 'locality', 'miserable']
for i in morewords:
    words[i] += 1
print(words['idly'])  # 9
```
或者使用update方法()
```python
words.update(morewords)
```
Counter对象还可以做一些数学运算
```python
a = Counter(result)
b = Counter(morewords)
c = a+b
d = a-b
# Counter({'idly': 9, 'glow': 9, 'imaginary': 8, 'heap': 8, 'ideal': 7, 'isolation': 6, 'locality': 6, 'miserable': 5})
print(c)
# Counter({'idly': 7, 'glow': 7, 'imaginary': 6, 'heap': 6, 'ideal': 5, 'isolation': 4, 'locality': 4, 'miserable': 3})
print(d)
```
**通过公共键对字典列表排序**
```python
from operator import itemgetter
users = [
    {'fname': 'Zeng', 'lname': 'WeiSong', 'uid': 1003, },
    {'fname': 'Zhang', 'lname': 'JiaWei', 'uid': 1001, },
    {'fname': 'Wang', 'lname': 'ZhiYuan', 'uid': 1002, },
    {'fname': 'Li', 'lname': 'JunJie', 'uid': 1005, },
    {'fname': 'Li', 'lname': 'JunHua', 'uid': 1004, },
]
sorted_by_id = sorted(users, key=itemgetter('uid'))
sorted_by_fname = sorted(users, key=itemgetter('fname'))
print(sorted_by_id)
# [
# {'fname': 'Zhang', 'lname': 'JiaWei', 'uid': 1001}, 
# {'fname': 'Wang', 'lname': 'ZhiYuan', 'uid': 1002}, 
# {'fname': 'Zeng', 'lname': 'WeiSong', 'uid': 1003}, 
# {'fname': 'Li', 'lname': 'JunHua', 'uid': 1004}, 
# {'fname': 'Li', 'lname': 'JunJie', 'uid': 1005},
# ]
print(sorted_by_fname)
# [
# {'fname': 'Li', 'lname': 'JunJie', 'uid': 1005}, 
# {'fname': 'Li', 'lname': 'JunHua', 'uid': 1004}, 
# {'fname': 'Wang', 'lname': 'ZhiYuan', 'uid': 1002}, 
# {'fname': 'Zeng', 'lname': 'WeiSong', 'uid': 1003}, 
# {'fname': 'Zhang', 'lname': 'JiaWei', 'uid': 1001},
# ]
```
itemgetter()函数还可以接受多个键
```python
sorted_by_flname = sorted(users, key=itemgetter('fname', 'lname'))
print(sorted_by_flname)
# [
# {'fname': 'Li', 'lname': 'JunHua', 'uid': 1004}, 
# {'fname': 'Li', 'lname': 'JunJie', 'uid': 1005}, 
# {'fname': 'Wang', 'lname': 'ZhiYuan', 'uid': 1002}, 
# {'fname': 'Zeng', 'lname': 'WeiSong', 'uid': 1003}, 
# {'fname': 'Zhang', 'lname': 'JiaWei', 'uid': 1001},
# ]
```
也可以通过使用匿名函数来实现这个功能
```python
sorted_by_lname = sorted(users,key = lambda r:r['lame'])
sorted_by_flname = sorted(users,key = lambda r:r['fname'],r['lname'])
```
但是使用匿名函数的方法可读性较差,且通常itemgetter()方法会运行得快一点

min和max函数也可以作用在这个函数上
```python
print(min(users, key=itemgetter('uid')))
#{'fname': 'Zhang', 'lname': 'JiaWei', 'uid': 1001}
print(max(users, key=itemgetter('uid')))
#{'fname': 'Li', 'lname': 'JunJie', 'uid': 1005}
```
**对不原生支持比较操作的对象进行排序**
```python
class User:
    def __init__(self,user_id) -> None:
        self.user_id=user_id
    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)
users=[User(32),User(56),User(27)]
print(sorted(users,key = lambda a:a.user_id))
```
也可以使用operator.attrgetter()函数来实现

```python
print(sorted(users,key = operator.attrgetter('user_id')))
```
attrgetter函数的速度更快，而且支持多个值；max和min函数可以作用在attrgetter函数上
```python
print(sorted(users, key=operator.attrgetter('user_id','first_name')))
print(min(users, key=operator.attrgetter('user_id')))  # User(27)
print(max(users, key=operator.attrgetter('user_id')))  # User(56)
```
**使用itertools.groupby()函数来对数据进行分组**
```python
books = [
    {"name": '红楼梦', "price": 100, "author": '曹雪芹'},
    {"name": '三体', "price": 90, "author": '刘慈欣'},
    {"name": '百年孤独', "price": 120, "author": '加西亚·马尔克斯'},
    {"name": '明朝那些事儿', "price": 110, "author": '当年明月'},
    {"name": '围城', "price": 110, "author": '钱钟书'},
    {"name": '人生的智慧', "price": 120, "author": '叔本华'},
    {"name": '活着', "price": 110, "author": '余华'},
    {"name": '1984', 'price': 100, "author": '乔治·奥威尔'},
    {"name": "飘", 'price': 90, "author": '玛格丽特·米切尔'},
    {"name": '白夜行', 'price': 90, "author": '东野圭吾'},
]
# 使用itemgetter方法先将数据按price来排序
results = sorted(books, key=itemgetter('price'))
# 使用group by 函数
for price, items in groupby(results, key=itemgetter('price')):
    print(price,'价位：')
    for i in items:
        print(' ',i)
```
输出结果如下：
```python
90 价位：
  {'name': '三体', 'price': 90, 'author': '刘慈欣'}
  {'name': '飘', 'price': 90, 'author': '玛格丽特·米切尔'}
  {'name': '白夜行', 'price': 90, 'author': '东野圭吾'}
100 价位：
  {'name': '红楼梦', 'price': 100, 'author': '曹雪芹'}
  {'name': '1984', 'price': 100, 'author': '乔治·奥威尔'}
110 价位：
  {'name': '明朝那些事儿', 'price': 110, 'author': '当年明月'}
  {'name': '围城', 'price': 110, 'author': '钱钟书'}
  {'name': '活着', 'price': 110, 'author': '余华'}
120 价位：
  {'name': '百年孤独', 'price': 120, 'author': '加西亚·马尔克斯'}
  {'name': '人生的智慧', 'price': 120, 'author': '叔本华'}
```
函数groupby()通过扫描序列找出拥有相同值的序列项，并将它们分组，groupby()返回一个元组，元组的第一个数据是相同值，第二个数据是一个子迭代器，这个子迭代器可以产生所有在该分组内具有该值的项。在这里要注意的是，**groupby()只能检查连续的项**，所有要将数据先排序

使用**列表推导式**来筛选序列中的元素
```python
mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print([x for x in mylist if x % 2 == 1])  # [1, 1, 3, 5, 13, 21]
```
如果原始输入非常大的话，列表推导式会产生一个庞大的结果，如果内存有限，可以使用生成器表达式，它只会产生一个迭代器
```python
temp = (x for x in mylist if x % 2 == 1)
print(temp)  # <generator object <genexpr> at 0x0000019F39FDE900>
for i in temp:
    print(i)
# 1
# 1
# 3
# 5
# 13
# 21
```
有时候简单的推导式没办法使用复杂的筛选标准，这个时候可以构建一个函数，然后使用内置的filter函数来处理，filter函数返回的也是一个迭代器，如果你想要的结果是一个列表，记得使用list函数
```python
values = ['abc', 'zws', '4396', '2200', '27', 'zjwsb', 'wzysb']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


results = filter(is_int, values)
print(list(results))  # ['4396', '2200', '27']
```
列表推导式和生成器表达式不仅是筛选数据最简单直接的方式，还可以用来修改数据
* 将输入的值转换为整型
  ```python
  nums = [int(x) for x in input().split()]
  ```
* 将列表里小于0的数筛掉，剩下的求平方根
  ```python
  import math
  num_list = [1, 4, -5, 10, -3, 9, 16, -7, -1]
  # [1.0, 2.0, 3.1622776601683795, 3.0, 4.0]
  print([math.sqrt(x) for x in num_list if x > 0])
  ```
* 也可以添上else语句用新值替换掉不满足条件的值
  ```python
  num_list = [1, 4, -5, 10, -3, 9, 16, -7, -1]

  print([x if x > 0 else 0 for x in num_list])  # [1, 4, 0, 10, 0, 9, 16, 0, 0]
  ```
还有一个不错的筛选工具是 itertools.compress()，它接受一个可迭代对象和一个布尔选择器序列作为输入，它会输出所有在相应的布尔选择器中为True的可迭代对象元素
```python
from itertools import compress
num_list = [1, 4, -5, 10, -3, 9, 16, -7, -1]

book_lists = ['红楼梦', '百年孤独', '三体', '明朝那些事儿', '飘', '围城', '活着', '1984', '人生的智慧']

# 先构建一个布尔序列
TF_list = [x < 0 for x in num_list]
print(TF_list)  # [False, False, True, False, True, False, False, True, True]
print(list(compress(book_lists, TF_list)))  # ['三体', '飘', '1984', '人生的智慧']
```
**使用字典推导式从字典中提取子集**
```python
books = {
    "红楼梦": 120,
    "百年孤独": 110,
    "三体": 100,
    "围城": 90,
    "人生的智慧": 120
}
new_books = {key: value for key, value in books.items() if value > 100}
print(new_books)  # {'红楼梦': 120, '百年孤独': 110, '人生的智慧': 120}
cBooks = ["红楼梦", '三体', '围城']
c_books = {key: value for key, value in books.items() if key in cBooks}
print(c_books)  # {'红楼梦': 120, '三体': 100, '围城': 90}
```
**使用collections.namedtuple()将名称映射到序列的元素当中**
* 实际上，collections.namedtuple()是一个工厂方法，他返回的是python中标准元组类型的子类。我们给它提供一个类型名称以及相应的字段，它就返回一个可实例化的类，为你已经定义好的字段传入值等
  ```python
  from collections import namedtuple

  Friends = namedtuple('Friends', ['name', 'age'])
  zjw = Friends('ZhangJiaWei', 19)
  wzy = Friends('WangZhiYuan', 20)
  print(zjw, wzy)
  # Friends(name='ZhangJiaWei', age=19) Friends(name='WangZhiYuan', age=20)
  ``` 
* namedtuple的实例是可以与普通元组互换的，而且支持所有普通元组所支持的操作，例如索引和解包等
  ```python
  print(len(zjw))  # 2
  w_name, w_age = wzy
  print(f'{w_name}的年龄是{w_age}')  # WangZhiYuan的年龄是20
  ```
* 通过位置来引用元素常常使得代码的可读性不够好，而且也很依赖于记录的具体结构，namedtuple的一种可能用法是作为字典的替代，后者需要更多的空间来存储。如果要构建涉及字典的大型数据结构，使用namedtuple更高效，但是namedtuple是不可变的：
  ```python
  zjw.age = 18  # AttributeError: can't set attribute
  ```
* 如果需要修改任何属性，可以使用namedtuple实例的_replace()方法来实现，该方法会创建一个全新的命名元组，并对相应的值做替换
  ```python
  wzy = wzy._replace(age=21)
  print(wzy)  # Friends(name='WangZhiYuan', age=21)
  ```
**在函数参数里面使用生成器表达式来同时对数据做转换和换算**
```python
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)  # 55
```
**使用collections.ChainMap类将多个映射合并为单个映射**
* ChainMap可接受多个映射然后在逻辑上使它们表现为一个单独的映射结构，但是这些映射在字面上并不会合并在一起
  ```python
  from collections import ChainMap
  a = {'x': 1, 'y': 2}
  b = {'y': 3, 'z': 4}
  c = ChainMap(a, b)
  print(list(c.keys()))  # ['y', 'z', 'x']
  print(list(c.values()))  # [2, 4, 1]
  print(c)  # ChainMap({'x': 1, 'y': 2}, {'y': 3, 'z': 4})
  ```
* 如果有重复的键，那么这里会采用第一个映射中所对应的值，修改映射的操作也总是会作用在一个映射结构上
  ```python
  print(c['x'])  # 1
  print(c['y'])  # 2
  print(c['z'])  # 4
  c['z'] = 10
  c['w'] = 40
  del c['x']
  print(a)  # {'y': 2, 'z': 10, 'w': 40}
  ```
* 我们也可以使用字典的update()方法将多个字典合并在一起
  ```python
  a = {'x': 1, 'y': 2}
  b = {'y': 3, 'z': 4}
  merged = dict(b)
  merged.update(a)
  print(merged['x'])  # 1
  print(merged['y'])  # 2
  print(merged['z'])  # 4
  ``` 
* 但是这样需要单独构建一个字典，而且对原始字典做了修改，并不会反应到合并后的字典中
  ```python
  a['x'] = 40
  print(merged['x'])  # 1
  ```
* 而ChainMap使用的就是原始的字典
  ```python
  c = ChainMap(a, b)
  print(c['x'])  # 1
  a['x'] = 40
  print(c['x'])  # 40
  ``` 