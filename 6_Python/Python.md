# Python Grammar

## 输入输出

* 输入 `inpput()` 值是 `str`

```py
name = input() # 
# ... 等待输入，eg:Steven
print(name) # 输出 eg: Steven

name2 = input('please enter your name:')
# please enter your name:... 等待输入，eg:Steven
print('hello ',name2) # 输出 eg: hello Steven
```

* 输出 `print()`

```py
print('hello, world') # hello, world
print('The quick brown fox', 'jumps over', 'the lazy dog') #The quick brown fox jumps over the lazy dog
```

---

## 基础

大小写敏感；
`#` 单行注释； `'''`(单引号) 或 `"""`(双引号) 多行注释；
当语句以冒号`:`结尾时，缩进的语句视为代码块
4个空格的缩进
  
```py
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
```

### 数据类型

* 整数：十进制  `1`,`200`,`-300`,`0`; 十六进制：`0x` 开头 `0xff00`; 数字分隔`_`，`10_000_000_000`(=`10000000000`),`0xa1b2_c3d4`。

* 浮点数： `1.23`，`3.14`，`-9.01` ; `1.23e9`(1.23x10<sup>9</sup>) `1.2e-5`(0.000012)

* 字符串： `'`(单引号),`"`(双引号) 括起来的任意文本 `'abc'`，`"xyz"`; `\` 换义字符;`'''...'''` 表示多行(`r'''...'''`);

```py
print('''line1
line2
line3''')
# 加 r 表示
print(r'''hello,\n
world''')
```

* 布尔值：`True`、`False`; 可以用`and`、`or`和`not`运算

* 空值： `None`

* 变量： 变量名必须是大小写英文、数字和`_`的组合，且不能用数字开头

```py
a = 1               # a 是一个整数
t_007 = 'Steven'    # t_007 是一个字符串
Angel = True        # Angel 是一个布尔值

stra = 'ABC'        # 1.内存中创建 ABC 字符串，2.内存中创建变量 stra 并指向 ABC
strb = stra
stra = 'XYZ'
print(strb)         # ABC
```

* 常量 ： 大写的变量表示，`PI = 3.14159265359`; `//`除法只取结果的整数部分,`10//3 # 值为 3`

### 字符串和编码

#### 字符编码

ASCII:
Unicode:
UTF-8: “可变长编码”;1-6个字节;常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节;为了节约空间

ASCII编码是1个字节，而Unicode编码通常是2个字节

|字符|ASCII|Unicode|UTF-8|
|:---:|:---:|:---:|:---:|
|A|01000001|00000000 01000001|01000001|
|中|x|01001110 00101101|11100100 10111000 10101101|

#### 字符串

字符串类型是`str`，在内存中以`Unicode`表示

单个字符的编码;`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符

```py
ord('A')    # 65
ord('中')   # 20013
chr(66)     # 'B'
chr(25991)  # '文'
```

由于Python的字符串类型是`str`，在内存中以`Unicode`表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`

`bytes`类型的数据用带`b`前缀的单引号或双引号 `x = b"ABC"`

* `encode()` 以Unicode表示的`str`编码为指定的`bytes`
* `decode()` 把`bytes`变为`str`
* `len()`    计算`str`包含多少个字符,计算`bytes`字节数
* `replace()` 替换

```py
'ABC'.encode('ascii')  # b'ABC'
'中文'.encode('utf-8') # b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('ascii') # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

b'ABC'.decode('ascii')                      # 'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # '中文'
b'\xe4\xb8\xad\xff'.decode('utf-8')         # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') # '中'

len('ABC')     # 3
len('中文')    # 2

len(b'ABC')   # 3
len(b'\xe4\xb8\xad\xe6\x96\x87')  # 6
len('中文'.encode('utf-8'))   # 6

a = 'abc'
b = a.replace('a', 'A') 
a  # 'abc'
b  # 'Abc'
```

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#### 格式化

```py
'Hi, %s, you have $%d.' % ('Michael', 1000000) # 'Hi, Michael, you have $1000000.'
print('%2d-%02d' % (3, 1))  #  3-01  （注意前面有个空格）
print('%.2f' % 3.1415926)   # 3.14
'growth rate: %d %%' % 7    # 'growth rate: 7 %'  （双百分号 %% 表示 %）
```

|占位符|替换内容|
|---|---|
|%d|整数|
|%f|浮点数|
|%s|字符串|
|%x|十六进制整数|

`format()` : 用传入的参数依次替换字符串内的占位符`{0}`、`{1}` `……`
`f-string` : 字符串如果包含`{xxx}`，就会以对应的变量替换

```py
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125) # 'Hello, 小明, 成绩提升了 17.1%'
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}') # The area of a circle with radius 2.5 is 19.62
```

### `list` 和 `tuple`

#### `list`

有序集合;索引访问(从0开始),可倒序访问(-1);元素数据类型可不同

* `len()`     : 获得`list`元素个数
* `append()`  : 末尾追加元素
* `insert(1,'test')` : 插入指定位置
* `pop()` : 不带参删除末尾元素，带参删除指定位置参数

```py
classmates = ['Michael', 'Bob', 'Tracy'] 
classmates[0]        # 'Michael'
classmates[1]        # 'Bob'
classmates[2]        # 'Tracy'
classmates[3]        # IndexError: list index out of range
classmates[-1]       # 'Tracy'
classmates[-2]       # 'Bob'
classmates[-3]       # 'Michael'
classmates[-4]       # IndexError: list index out of range

classmates.append('Tom')    # ['Michael', 'Bob', 'Tracy', 'Tom']
classmates.insert(1,'Jack') # ['Michael', 'Jack', 'Bob', 'Tracy', 'Tom']

classmates.pop()        # ['Michael', 'Jack', 'Bob', 'Tracy']
classmates.pop(1)       # ['Michael', 'Bob', 'Tracy']

classmates[1] = 'Tom'   # ['Michael', 'Tom', 'Tracy']

s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)   # 4
s[2][1]  # 'php'
```

#### `tuple`

元素初始化后不能修改(“指向不变”)；1个元素的`tuple`时，加一个逗号`,`

```py
classmates = ('Michael', 'Bob', 'Tracy') # ('Michael', 'Bob', 'Tracy')
classmates[2]=222  # TypeError: 'tuple' object does not support item assignment

t = ()    # ()
t = (1,)  # (1,)
```

### 条件判断

`if`;`if else`;`if elif else`; 注意 `:`
条件变量：非零数值、非空字符串、非空`list`等，就判断为`True`，否则为`False`

```py
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

s = input('birth: ')
birth = int(s)       # input 输入的是字符串，int转换成整数
if birth < 2000:
    print('00前')
else:
    print('00后')
```

### 循环

`for...in`
`while`
`break`:跳出循环
`contiune`：跳过本次循环

`range()` : 生成整数序列
`list()`  : 转换成 `list`

```py
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# Michael
# Bob
# Tracy

list(range(5)) # [0, 1, 2, 3, 4]

i = 0
while i<len(names):
    print(names[i]) 
    i=i+1
# Michael
# Bob
# Tracy
```

### `dict`和`set`

#### `dict`

dictionary(map),键-值（key-value）存储;查找速度快；key必须是**不可变对象**

`in` 判断key存在否
`get()` 获取key对应的值，key不存在返回`None`,可自定义key不存在返回值
`pop(key)` 删除key以及对应的value

```py
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']  # 95

d['Adam'] = 67
d  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}
d['Adam'] = 100
d  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 100}

'Tom' in d  # False

d.get('Tom')
d.get('Tom',False)  # False

d.pop('Bob')  # 75
d # {'Michael': 95, 'Tracy': 85, 'Adam': 100}
```

`dict`和`list`比较

|dict|list|
|---|---|
|查找和插入的速度极快，不会随着key的增加而变慢|查找和插入的时间随着元素的增加而增加|
|占用大量的内存，内存浪费多|占用空间小，浪费内存很少|

#### `set`

key不能重复的集合，不存储value;创建`set`,需要提供一个`list`作为输入集合
；不可放入**可变对象**；交集、并集操作

`add(key)`    添加元素
`remove(key)` 删除元素

```py
s = set([1, 2, 3])  # 初始化
s  # {1, 2, 3}

s = set([1, 1, 2, 2, 3, 3]) # 重复元素自动过滤
s # {1, 2, 3}

s.add(4)  # {1, 2, 3, 4}
s.add(4)  # {1, 2, 3, 4} 重复添加无效

s.remove(4) # {1, 2, 3} 
s.remove(4) # KeyError: 4 重复删除报错 

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2  # 交集 {2, 3}
s1 | s2  # 并集 {1, 2, 3, 4}
```

---

## 函数

写一次，多次调用； [python内置函数](https://docs.python.org/3/library/functions.html)

函数名:指向一个函数对象引用

`help(函数名)` 查看函数帮助
`abs()` 绝对值
`hex()` 整数转换成十六进制

```py
help(abs)
# Help on built-in function abs in module builtins:
# abs(x, /)
#    Return the absolute value of the argument.

a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数

hex(255)  # '0xff'
```

### 数据类型转换

```py
int('123')      # 123
int(12.34)      # 12
float('12.34')  # 12.24
str(1.23)       # '1.23'
str(100)        # '100'
bool(1)         # True
bool('')        # Flase
```

### 定义函数

`def` 函数名、括号、括号中的参数和冒号`:` `return`

导入保存的函数 `abstest.py`
`from abstest import my_abs`

```py
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

#### 空函数

```py
def nop():
    pass
```

#### 参数检查

参数个数不对,Python解释器会自动检查，抛出`TypeError`
参数类型不对,无法检查

`isinstance()` 数据类型检查

```py
my_abs(1, 2) # TypeError: my_abs() takes 1 positional argument but 2 were given
my_abs('a')  # TypeError: '>=' not supported between instances of 'str' and 'int'
abs('a')     # TypeError: bad operand type for abs(): 'str'
```

```py
def my_abs(x):
    if not  (x, (int, float)):  # x,tuple
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs('a')  # TypeError: bad operand type
```

#### 返回多个值

```py
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6) # 其实返回的还是但一个值，tuple
print(r)     # (151.96152422706632, 70.0)
```

定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用`return`随时返回函数结果；
函数执行完毕也没有`return`语句时，自动`return None`。
函数可以同时返回多个值，但其实就是一个`tuple`

### 函数参数

必选参数，默认参数、可变参数和关键字参数

#### 必选参数(位置参数)

```py
def power(x, n):  # 必选参数，计算x的 n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

#### 默认参数

特比注意：**默认参数必须指向不变对象**

```py
def power(x, n=2): # 默认参数(必选在前，默认在后)
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin') # city参数用传的值,其他默认参数继续使用默认值
```

```py
def add_end(L=[]):  # [] 可变
    L.append('END')
    return L 

add_end([1, 2, 3]) # [1, 2, 3, 'END']
add_end(['x', 'y', 'z']) # ['x', 'y', 'z', 'END']
add_end()   # ['END']
add_end()   # ['END', 'END']
add_end()   # ['END', 'END', 'END']

def add_end(L=None): # None 不可变
    if L is None:
        L = []
    L.append('END')
    return L

add_end() # ['END']
add_end() # ['END']
```

#### 可变参数

传入参数个数可变
可变参数在函数调用时自动组装为一个`tuple`

```py
def calc(*numbers):  # def calc(numbers) 可通过传入 list 或 tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2) # 5
calc()     # 0

# list或tuple前面加一个 * 变成可变参数
nums =[1,2,3]
calc(*nums)  # 14
```

#### 关键字参数

允许你传入0个或任意个含参数名的参数
关键字参数在函数内部自动组装为一个`dict`
扩展函数功能

```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30) # name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing') # name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
# kw获得的dict是extra的一份拷贝,修改 kw 不会影响 extra
person('Jack', 24, **extra) # name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

```

#### 命名关键字参数

```py
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, job):  # 只接收 city 和 job 作为关键字的参数
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer') # Jack 24 Beijing Engineer
a = {'city':'Beijing', 'job':'Engineer'}
person('Jack',24,**a)               # Jack 24 Beijing Engineer

# 函数定义中已经有了一个可变参数，它后面的命名关键字参数不需要分隔符*
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 必须传入参数名 不传报错
person('Jack', 24, 'Beijing', 'Engineer') # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

```

#### 参数组合

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

任意函数通过类似`func(*args, **kw)`的形式调用

```py
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)                # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)           # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')   # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None) # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3) 
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

小结

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

`*args`是可变参数，`args`接收的是一个`tuple`；

`**kw`是关键字参数，kw接收的是一个`dict`。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：`func(1, 2, 3)`，又可以先组装`list`或`tuple`，再通过`*args`传入：`func(*(1, 2, 3))`；

关键字参数既可以直接传入：`func(a=1, b=2)`，又可以先组装`dict`，再通过`**kw`传入：`func(**{'a': 1, 'b': 2})`。

使用`*args`和`**kw`是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符`*`，否则定义的将是位置参数。

### 递归函数

函数在内部调用自身本身;

函数调用通过栈（`stack`）实现，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。栈的大小不是无限的，递归调用的次数过多，会导致栈溢出；解决递归调用栈溢出通过**尾递归**，函数返回时，调用自身本身；

阶乘：$fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n$

```py
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
# return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算

# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120
```

```py
# 汉诺塔游戏
def move(n, a, b, c):
    #如果n=1,直接a到c
    if n == 1:
        print(a, '-->', c)
    #n＞1,视为1个最大的圆盘和剩余n-1个圆盘当一个整体移动,
    #那n-1个移到b,最大那个移到c,即可实现递归
    else:
        move(n-1,a,c,b)  # n-1个以整体移到b
        print(a,'-->',c) # 剩下那个最大的移到c
        move(n-1,b,a,c)  # n-1个变成新的问题:如何将n-1个从b移到c.(递归即可)

move(3, 'A', 'B', 'C')

```

---

## 高级特性

### 切片

```py
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3] # ['Michael', 'Sarah', 'Tracy']
L[:3]  # ['Michael', 'Sarah', 'Tracy']
L[-2:] # ['Bob', 'Jack']
L[-2:-1] # ['Bob']

L = list(range(100)) # [0, 1, 2, 3, ..., 99]
L[:10] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L[-10:] # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
L[10:20] # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
L[:10:2] # [0, 2, 4, 6, 8] 前10个数，每两个取一个
L[::5] # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] 所有数，每5个取一个
L[:] # [0, 1, 2, 3, ..., 99] 原样复制list

list(rang(6,0,-1))  # [6, 5, 4, 3, 2, 1]
```

### 迭代

使用`for`循环，只要作用于一个**可迭代对象**即可正常运行

通过`collections.abc`模块的`Iterable`类型判断可迭代

`enumerate`函数可以把一个`list`变成**索引-元素**

```py
from collections.abc import Iterable
L = [2,4,7]
for i in L:   # list 迭代
    print(i)

T = (3,6,9)
for t in T:  # tuple 迭代
    print(t)

D = {'a': 1, 'b': 2, 'c': 3} 

for key in D: # dict 迭代, 默认迭代的是 key
    print(key)

for value in D.values(): # dict 迭代 value
    print(value)

for k, v in D.items(): # 同时迭代 key 和 value
   print(f'key:{k},value:{v}')

for ch in 'ABC': # 迭代字符串
    print(ch)

isinstance('abc', Iterable)   # str是否可迭代 True
isinstance([1,2,3], Iterable) # list是否可迭代 True
isinstance(123, Iterable) # 整数是否可迭代 False

for i, value in enumerate(['A', 'B', 'C']):  # 0 A   1 B   2 C
    print(i,value)

# 同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:  # 1 1   2 4    3 9
    print(x,y)
```

### 列表生成式

列表生成式即 *List Comprehensions*

```py
list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1, 11):
    L.append(x * x)
L   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 这行代替上面的
[x * x for x in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for 后面还能跟 if
[x * x for x in range(1, 11) if x % 2 == 0] # [4, 16, 36, 64, 100]

# 两层循环，全排列
[m + n for m in 'ABC' for n in 'XYZ'] # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os # 导入os模块
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
#  ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
```

`for`循环其实可以同时使用两个甚至多个变量，比如`dict`的`items()`可以同时迭代`key`和`value`

```py
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# x = A
# y = B
# z = C

# 列表生成式使用两个变量生成list
[k + '=' + v for k, v in d.items()] # ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]  # ['hello', 'world', 'ibm', 'apple']
```

列表生成式中的 `if ... else`:

* `for` 后面的 `if` 是一个筛选条件，不能带 `else`
* `for` 前面的 `if` 是一个表达式，必须带`else`

```py
[x for x in range(1, 11) if x % 2 == 0] # [2, 4, 6, 8, 10]
[x if x % 2==0 else -x for x in range(1,11)] # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

```

`isinstance`函数可以判断一个变量是不是字符串

### 生成器

循环过程中不断推算出后面的元素

```py
L = [x * x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10)) # <generator object <genexpr> at 0x7f831c7c7050>
next(g) # 0
next(g) # 1
next(g) # 4

for n in g:
    print(n)   # 9 16, 25, 36, 49, 64, 81

def fib(max):   # <function fib at 0x7f831da6fd40>
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b # 相当于 t = (b, a + b);a = t[0];b = t[1]  # t 是一个tuple
        n = n+1
    return 'done'

fib(6) # 1 1 2 3 5 8 'done'
```

generator 函数 遇到 `yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。

**调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。**

```py
# generator 函数
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'

f = fib(6) # f => <generator object fib at 0x7f831dacf150>

for n in fib(6):
    print(n)     # 1 1 2 3 5 8

g = fib(6)
while True:
    try:
        x= next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# g:1 g:1 g:2 g:3 g:5 g:8 Generator return value: done

# 杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L = L + [0]
        L = [L[i]+L[i-1] for i in range(len(L))]

n=0
results = []
for t in triangles():
    results.append(t)
    n = n+1
    if n ==10:
        break

for t in results:
    print(t)

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

```

### 迭代器

作用于 `for` 的数据类型

* 集合，`list`,`tuple`,`dict`,`set`,`str`等
* `generator`,带 `yield` 的 generator function

可直接作用于 `for` 循环的对象统称为可迭代独享：`Iterable`
可以被`next()`函数调用不断返回下一个值的对象 `Iterator`
`iter()` 把 `list`,`dict`,`str` 等 `Iterable` 变成 `Iterator`
Python的`for`循环本质上就是通过不断调用`next()`函数实现的

使用 `isinstance()` 判断

```py
from collections.abc import Iterable

isinstance([],Iterable) # True
isinstance({},Iterable) # True
isinstance('abc',Iterable) # True
isinstance((x for x in range(10)), Iterable) # True
isinstance(123,Iterable) # False

from collections.abc import Iterator

isinstance((x for x in range(10)), Iterator) # True
isinstance([],Iterator) # False
isinstance({},Iterator) # False
isinstance('abc',Iterator) # False

isinstance(iter([]),Iterator)     # True
isinstance(iter('abc'), Iterator) # True
```

为什么`list`、`dict`、`str`等数据类型不是`Iterator`？
>因为Python的`Iterator`对象表示的是一个**数据流**，`Iterator`对象可以被`next()`函数调用并不断返回下一个数据，直到没有数据时抛出`StopIteration`错误。可以把这个数据流看做是一个**有序序列**，但我们却不能提前知道序列的长度，只能不断通过`next()`函数实现按需计算下一个数据，所以`Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算。
>`Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用`list`是永远不可能存储全体自然数的。

[Collections Abstract Base Classes, Iterator Types](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes)

* `Iterable` 对象需要实现 `__iter__` 方法
* `Iterator` 继承自 Iterable, 因而也必须实现 `__iter__` 方法， 并且原则上此方法应直接返回 `self`, 即对象本身，但非强制。
* `Iterator` 还需要实现 `__next__` 方法

一个 `Iterator` 对象需且仅需同时具有 `__iter__` 和 `__next__` 方法
生成器是一个用于创建迭代器的简单而强大的工具，也就是说生成器也是迭代器

## 函数式编程(Functional Programming)

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python不是纯函数式编程语言(可以使用变量)

### 高阶函数

* 变量可以指向函数(函数可以复制给变量)
* 函数名也是变量
* 传入参数（高阶函数：一个函数接收另一个函数作为参数）

```py
abs(-10) # 10
abs      # <built-in function abs>
x = abs(-10)
x        # 10
f = abs
f        # <built-in function abs>
f(-10)   # 10

abs = 10
abs(-10) # Traceback (most recent call last):  File "<stdin>", line 1, in <module>  TypeError: 'int' object is not callable

def add(x, y, f):    # 高阶函数
    return f(x)+f(y)

add(-5,6,abs)  # 11
```

#### `map`、`reduce`

* `map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回

```py
def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])  # r 是Iterator 惰性序列
list(r)     #  [1, 4, 9, 16, 25, 36, 49, 64, 81]

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 把这个list所有数字转为字符串
```

* `reduce()`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是

`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

```py
from functools import reduce
def add(x,y):
    return x + y
reduce(add, [1,3,5,7,9]) # 25

def fn(x,y):
    return x*10 +y
reduce(fn,[1,3,5,7,9])   # 13579

def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
    return digits[s]

reduce(fn, map(char2num,'13579')) # 13579
```

把`str`转换为`int`

```py
from functools import reduce

DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}

def str2int(s):
    def fn(x,y):
        return x*10 +y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num,s))

def char2num2(s):
    return DIGITS[s]

def str2int2(s):  # 最简化
    return reduce(lambda x, y:x*10+y, map(char2num, s))
```

把字符串`'123.456'`转换成浮点数`123.456`

```py
from functools import reduce
def str2float(s):
    s1 ,s2 = s.split('.')
    num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(x):
        return num_dict[x]
    return reduce(lambda x,y : x*10+y ,map(char2num , s1)) + reduce(lambda x,y: x/10+y, map(char2num , s2[::-1]))/10 # s2[::-1] 字符串反转
```

#### `filter`

`filter()`函数用于过滤序列。`filter()`把传入的函数依次作用于每个元素，根据返回值`True`,`False`决定是否保留该元素
`filter()`函数返回的是一个`Iterator`惰性序列，要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回`list`。

```py
# 在list中删掉偶数保留奇数
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

# 删掉序列中的空字符串
def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']
```

计算素数的一个方法是[埃氏筛法](https://baike.baidu.com/item/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95/374984?fromtitle=%E5%9F%83%E6%8B%89%E6%89%98%E8%89%B2%E5%B0%BC%E7%AD%9B%E9%80%89%E6%B3%95&fromid=4524938)

首先，列出从`2`开始的所有自然数，构造一个序列：
`2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...`
取序列的第一个数`2`，它一定是素数，然后用`2`把序列的`2`的倍数筛掉：
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...`
取新序列的第一个数`3`，它一定是素数，然后用3把序列的`3`的倍数筛掉：
`5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...`
取新序列的第一个数`5`，然后用`5`把序列的`5`的倍数筛掉：
`7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...`
不断筛下去，就可以得到所有的素数

```py
# (从3开始的奇数序列) 生成器-无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 生成器 不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列  it = filter(lambda x: x % n > 0, it)

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

```py
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n):
    return str(n)==str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
```

#### `sorted`

排序算法

```py
sorted([36, 5, -12, 9, -21])
# 对list排序 [-21, -12, 5, 9, 36]

# key指定的函数将作用于list的每一个元素上
sorted([36, 5, -12, 9, -21], key=abs)
# [5, 9, -12, -21, 36]

sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']

# 反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=lambda t : t[0])  # 按姓名排序
print(L2)
L3 = sorted(L, key=lambda t : -t[1])  # 按分高到低排序
print(L3)
L4 = sorted(L, key=lambda t : t[1], reverse=True)  # 按分高到低排序
print(L4)
```

### 返回函数

#### 函数作为返回值

```py
# 求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 返回求和函数，在需要的时候调用
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9) # <function lazy_sum.<locals>.sum at 0x0000018999D6D160>
f()  # 25
# 调用lazy_sum()时，每次都会返回一个新的函数，即使传入相同的参数

f1 = lazy_sum(1, 3, 5, 7, 9)
f == f1 # False  f()和f1()调用结果互不影响
```

#### 闭包

当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
**返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**

```py
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

f1() # 9
f2() # 9
f3() # 9

def count2():
    def f(j):
        def g():
            return j*j
        return g    # lambda : j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f12, f22, f32 = count2()

f12() # 1
f22() # 4
f32() # 9
```

nonlocal

使用闭包，内层函数引用了外层函数的局部变量。只读外层变量，返回的闭包函数调用一切正常

**使用闭包时，对外层变量赋值前，需要先使用`nonlocal`声明该变量不是当前函数的局部变量。**

```py
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

# 对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量
def inc():
    x = 0
    def fn():
        # nonlocal x   # 解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1
        x = x + 1 # UnboundLocalError: local variable 'x' referenced before assignment(x作为局部变量并没有初始化，直接计算x+1是不行的)
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2


def createCounter():
    num = 0
    def counter():
        nonlocal num 
        num = num + 1
        return num
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
```

### 匿名函数

关键字`lambda`表示匿名函数，
缺点：只能有一个表达式，不用写`return`，返回值就是该表达式的结果
有点：不必担心函数名冲突，函数对象可赋值给变量

```py
f = lambda x: x * x
f(5) # 25

L = list(filter(lambda x: x%2 ==1, range(1, 20))) # 奇数
```

跟普通函数一样，lambda 也支持 无参数、默认参数 和可变参数
无参数：`lambda :100 #传入一个固定值或者其他值`
默认参数：`lambda a,b=20,c=30 :a+b+c`
可变参数：`fn=lambda *a:list(a) ; print(fn(1,2,3)) #输出[1,2,3]`
可变参数：`fn=lambda **kws: kws ; print(fn(l1=1,l2=2,l3=3)) #输出{'l1': 1, 'l2': 2, 'l3': 3}`

### 装饰器

Python的decorator可以用函数实现，也可以用类实现。

```py
def now():
    print('2015-3-25')

f = now
f()  # 2015-3-25
now.__name__ #'now'
f.__name__ #'now'
```

假设增强`now()`函数的功能，比如，在函数调用前后自动打印日志，但又不修改`now()`函数的定义，在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。decorator就是一个返回函数的高阶函数

```py
# 接受一个函数作为参数，并返回一个函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 借助Python的@语法，把decorator置于函数的定义处
@log   # now = log(now)
def now():
    print('2015-3-25')

now() # call now():
      # 2015-3-25
```

由于`log()`是一个decorator，返回一个函数，所以，原来的`now()`函数仍然存在，只是现在同名的`now`变量指向了新的函数，于是调用`now()`将执行新函数，即在`log()`函数中返回的`wrapper()`函数。
`wrapper()`函数的参数定义是`(*args, **kw)`，因此，`wrapper()`函数可以接受任意参数的调用。在`wrapper()`函数内，首先打印日志，再紧接着调用原始函数。

```py
# decorator本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')   # now = log('execute')(now)
def now():
    print('2015-3-25')

now()  # execute now():
       # 2015-3-25
now.__name__ # 'wrapper'
```

首先执行`log('execute')`，返回的是`decorator`函数，再调用返回的函数，参数是`now`函数，返回值最终是`wrapper`函数
因为返回的那个`wrapper()`函数名字就是`'wrapper'`，所以需要把原始函数的`__name__`等属性复制到`wrapper()`函数中，否则，有些依赖函数签名的代码执行就会出错

不需要编写`wrapper.__name__ = func.__name__`这样的代码，使用Python内置的`functools.wraps`

```py
import functools

def log(func):
    @functools.wraps(func)  # 处理函数名等属性
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func) # 处理函数名等属性
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

```py
# 打印函数执行时间
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t = time.time()
        ret = fn(*args, **kw)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, t2-t))
        return ret
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
```

```py
# 既支持  @log 又支持 @log('execute')
def log(func):
    # print(func)
    if callable(func):  # 检查一个对象是否是可调用的. 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
        @functools.wraps(func)
        def wrap(*args, **kw):
            print('no args %s():' % (func.__name__))
            print("begin call")
            r = func(*args, **kw)
            print("end call")
            return r
        return wrap
    
    def decorator(fn):
        @functools.wraps(fn)
        def wrap(*args, **kw):
            print('args  %s %s():' % (func, fn.__name__))
            print("begin call")
            r = fn(*args, **kw)
            print("end call")
            return r
        return wrap  
    return decorator        
```

### 偏函数

`functools`模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

```py
int('12345')            # 12345
# 传入base参数，就可以做N进制的转换
int('12345', base=8)    # 5349
int('12345', 16)        # 74565

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)

int2('1000000')  # 64
int2('1010101')  # 85
```

利用`functools.partial`创建一个偏函数,把一个函数的某些参数给固定住(设置默认值),返回一个新的函数，调用这个新函数会更简单

```py
import functools
int2 = functools.partial(int, base=2)
int2('1000000')  # 64
int2('1010101')  # 85
# 也可以传入 base 值
int2('1000000', base=10) # 1000000

int2('10010') # 相当于 kw = { 'base': 2 }  int('10010', **kw)
```
