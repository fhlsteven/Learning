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
b'\xe4\xb8\xad\xff'.decode('utf-8')         
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
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
print(f'The area of a circle with radius {r} is {s:.2f}') 
# The area of a circle with radius 2.5 is 19.62
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
my_abs(1, 2) 
# TypeError: my_abs() takes 1 positional argument but 2 were given
my_abs('a') 
 # TypeError: '>=' not supported between instances of 'str' and 'int'
abs('a')     
# TypeError: bad operand type for abs(): 'str'
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
enroll('Adam', 'M', city='Tianjin') 
# city参数用传的值,其他默认参数继续使用默认值
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

person('Michael', 30) 
# name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing') 
# name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') 
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
# kw获得的dict是extra的一份拷贝,修改 kw 不会影响 extra
person('Jack', 24, **extra) 
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

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
person('Jack', 24, 'Beijing', 'Engineer') 
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

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
# return fact_iter(num - 1, num * product)仅返回递归函数本身
# ，num - 1和num * product在函数调用前就会被计算

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

max2 = functools.partial(max, 10) # 实际上会把10作为*args的一部分自动加到左边
max2(5, 6, 7) # args = (10, 5, 6, 7)   max(*args)
```

## 模块

模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

为了编写可维护的代码，把很多函数分组，分别放到不同的文件里，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
在Python中，一个.py文件就称之为一个模块（Module）。

可维护性高，可以被其他地方引用，避免函数名和变量名冲突

[python所有内置函数](https://docs.python.org/3/library/functions.html)

避免模块名冲突，Python引入了按目录来组织模块的方法，称为包（Package）

举例：一个`abc.py`是一个叫`abc`的模块，一个`xyz.py`是一个叫`xyz`的模块
避免冲突与其他模块冲突，使用顶层包名，比如`mycompany`，按照如下目录存放

```txt
mycompany
├─ __init__.py   # 必须存在,否则是普通目录，而不是一个包；可以是空文件，也可有代码，本身就是一个模块 mycompany
├─ abc.py        # mycompany.abc
└─ xyz.py        # mycompany.xyz

# 多级目录
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py     # mycompany.web.utils
 │  └─ www.py       # mycompany.web.www
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py        # mycompany.utils
```

**自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了`sys`模块，自己的模块就不可命名为`sys.py`，否则将无法导入系统自带的`sys`模块。**

注意：

* 模块名要遵循Python变量命名规范，不要使用中文、特殊字符;
* 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行`import abc`，若成功则说明系统存在此模块。

### 使用模块

```py
#!/usr/bin/env python3                     # 让代码直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-                    # 使用标准UTF-8编码

' a test module '                          # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Steven'                      # 

import sys                                 # 导入sys模块

def test():
    args = sys.argv                        # list存储了命令行的所有参数
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':                   # 命令行运行 hello 模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    test()
```

命令行运行` hello `模块文件时，Python解释器把一个特殊变量`__name__`置为`__main__`，而如果在其他地方导入该`hello`模块时，`if`判断将失败，因此，这种`if`测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

#### 作用域

通过`_`前缀控制作用域

正常的函数和变量名是公开的（`public`），可以被直接引用，比如：`abc`，`x123`，`PI`等；
类似`__xxx__`这样的变量是**特殊变量**，可以被直接引用，但是有特殊用途，比如上面的`__author__`，`__name__`就是特殊变量，hello模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不要用这种变量名；
类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（`private`），*不应该*被直接引用，比如`_abc`，`__abc`等；

### 安装第三方模块

`pip install Pillow`   Anaconda

添加自己的搜索目录：1.运行时添加要搜索的目录，运行结束后失效 2：设置环境变量`PYTHONPATH`，该环境变量的内容会被自动添加到模块搜索路径中。

```cmd
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
```

## 面向对象编程

Object Oriented Programming - OOP
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

```py
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 给对象发消息实际上就是调用对象对应的关联函数，称之为对象的方法（Method）
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

### 类(Class)和实例(Instance)

定义类是通过`class`关键字

```py
class Student(object):
    pass

>>> bart = Student()
>>> bart
<__main__.Student object at 0x000002518C453DC0>   
>>> Student
<class '__main__.Student'>
```

`class`后面紧接着是类名，即`Student`，类名通常是大写开头的单词，紧接着是`(object)`，表示该类是从哪个类继承的，如果没有合适的继承类，就使用`object`类，所有类最终都会继承`object`类。

使用特殊方法`__init__`，在创建实例的时候初始化属性  **注意：特殊方法“__init__”前后分别有两个下划线！！！**

注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去：

**`object` 和 `self`**

小结

* 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
* 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
* 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
* 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

### 访问限制

实例的变量名如果以`__`开头，就变成了一个私有变量(（)private)，只有内部可以访问，外部不能访问

在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。

不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量,不同版本的Python解释器可能会把`__name`改成不同的变量名

```py
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
```

```cmd
>>> bart = Student('Bart Simpson', 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
>>> bart._Student__name  # 不同版本的Python解释器可能会把__name改成不同的变量名
'Bart Simpson'

# 特别注意的错误写法
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！ 这个相当于新加了一个玩意儿
>>> bart.__name
'New Name'

>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
```

### 继承和多态

```py
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

```py
# 定义class 就是定义一种数据类型
class Animal(object):
    def run(self):
        print('Animal is running...')
    def eat(self):
        print('Eating meat...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
     def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()   # 子类的run()覆盖了父类的run()

cat = Cat()
cat.run()

a = list()      # a是list类型
b = Animal()    # b是Animal类型
c = Dog()       # c是Dog类型

isinstance(a, list)   # True
isinstance(b, Animal) # True
isinstance(c, Dog)    # True
isinstance(c, Animal) # True
isinstance(b, Dog)    # False

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# Animal is running...
# Animal is running...
run_twice(Dog())
# Dog is running...
# Dog is running...
run_twice(Cat())
# Cat is running...
# Cat is running...
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
# Tortoise is running slowly...
# Tortoise is running slowly...
```

对扩展开放：允许新增`Animal`子类；
对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。

#### 静态语言 vs 动态语言

对于**静态语言**（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。
对于Python这样的**动态语言**来说，则不一定需要传入`Animal`类型。只需要保证传入的对象有一个`run()`方法就可以了

### 获取对象信息

#### 使用`type()`

基本类型都可用`type()`判断
变量指向函数或者类可用`type()`判断

```py
type(123)   # <class 'int'>
type('str') # <class 'str'>
type(None)  # <type(None) 'NoneType'>

type(abs)  # <class 'builtin_function_or_method'>
# 比较两个变量的type类型是否相同
type(123)==type(456)        # True
type(123)==int              # True
type('abc')==type('123')    # True
type('abc')==str            # True
type('abc')==type(123)      # False

# 可以使用types模块中定义的常量,判断一个对象是否是函数
import types
def fn():
    pass

type(fn)==types.FunctionType                        # True
type(abs)==types.BuiltinFunctionType                # True
type(lambda x: x)==types.LambdaType                 # True
type((x for x in range(10)))==types.GeneratorType   # True
```

#### 使用`isinstance()`

判断`class`的类型，可以使用`isinstance()`函数
能用`type()`判断的基本类型可用`isinstance()`判断

**总是优先使用`isinstance()`判断类型，可以将指定类型及其子类“一网打尽”。**

```py
# object -> Animal -> Dog -> Husky
class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

# 判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
isinstance(h, Husky)    # True
isinstance(h, Dog)      # True
isinstance(h, Animal)   # True
isinstance(d, Dog) and isinstance(d, Animal) # True
isinstance(d, Husky)    # False

isinstance('a', str)    # True
isinstance(123, int)    # True
isinstance(b'a', bytes) # True

# 可以判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))  # True list
isinstance((1, 2, 3), (list, tuple))  # True tuple
```

#### 使用`dir()`

获得一个对象的所有属性和方法,返回一个包含字符串的`list`
配合`getattr()`、`setattr()`以及`hasattr()`，可直接操作一个对象的状态

```py
dir('ABC')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

len('ABC')          # 3
'ABC'.__len__()     # 3  在len()函数内部，它自动去调用该对象的__len__()方法

class MyCat(object):
    def __len__(self):
        return 100

cat = MyCat()
len(cat)            # 100

'ABC'.lower()       # 'abc'

class TObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = TObject()
hasattr(obj, 'x')       # 有属性'x'吗？ True
obj.x                   # 9
hasattr(obj, 'y')       # 有属性'y'吗？ False
setattr(obj, 'y', 19)   # 设置一个属性'y'
hasattr(obj, 'y')       # 有属性'y'吗？ True
getattr(obj, 'y')       # 获取属性'y'  19
obj.y                   # 获取属性'y'  19

# 试图获取不存在的属性，会抛出AttributeError的错误
getattr(obj, 'z')       # 获取属性'z' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'TObject' object has no attribute 'z'

getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404
# 404

hasattr(obj, 'power')   # 有属性'power'吗？True
getattr(obj, 'power')   # 获取属性'power'
# <bound method TObject.power of <__main__.TObject object at 0x0000027AA5633550>>

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn                         # fn指向obj.power
# <bound method TObject.power of <__main__.TObject object at 0x0000027AA5633550>>

# 从文件流fp中读取图像,首先要判断该fp对象是否存在read方法，存在，则是一个流；不存在，则无法读取
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

### 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者通过`self`变量：
**千万不要对实例属性和类属性使用相同的名字**

* 实例属性属于各个实例所有，互不干扰；
* 类属性属于类所有，所有实例共享一个属性

```py
class Student(object):
    name = 'Student' # 类属性

s = Student()        # 创建实例s
print(s.name)        # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print(Student.name)  # 打印类的name属性
# Student
s.name = 'Michael'   # 给实例绑定name属性
print(s.name)        # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name           # 如果删除实例的name属性
print(s.name)        # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student

# 统计学生人数
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

```

## 面向对象高级编程

基础：数据封装、继承和多态
多重继承、定制类、元类等高级概念

### 使用`__slots__`

限制实例的属性
`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

```py
class Student(object):
    pass

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)       # Michael

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)           # 调用实例方法
s.age                   # 测试结果  25

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
s2.set_age(25) # 尝试调用方法
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'set_age'

# 给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
s.score           # 100
s2.set_score(99)
s2.score          # 99
```

```py
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()       # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25          # 绑定属性'age'
s.score = 99        # 绑定属性'score'； 'score'没有被放到__slots__中 报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999          # 不报错，继承子类可以不受限制
```

### 使用`@property`

Python内置的`@property`装饰器负责把一个方法变成属性调用
**属性的方法名不要和实例变量重名**

```py
class Student(object):
    def get_score(self):
         return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)  # ok!
s.get_score()    # 60

s.set_score(9999)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 8, in set_score
# ValueError: score must between 0 ~ 100!
```

加上`@property`就可把一个`getter`方法变成属性,`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个`setter`方法变成属性赋值

```py
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60    # OK，实际转化为s.set_score(60)
s.score         # OK，实际转化为s.get_score()

s.score = 9999
# Traceback (most recent call last):
# ValueError: score must between 0 ~ 100!
```

```py
# birth可读写属性 age是只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2022 - self._birth

# 属性的方法名不要和实例变量重名 error 错误示例
class Student(object):
    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        self._width = val    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value    
    @property
    def resolution(self):
        return self._width * self._height

```

### 多重继承

Dog - 狗；Bat - 蝙蝠；Parrot - 鹦鹉；Ostrich - 鸵鸟。

```asi
# 哺乳动物和鸟类归类
            ┌────────┐
       ┌────┤ Animal ├────┐       
       │    └────────┘    │
       │                  │
  ┌────▼────┐        ┌────▼─────┐
  │  Mammal │        │   Bird   │
  └─┬─────┬─┘        └─┬──────┬─┘
    │     │            │      │
    │     │            │      │
┌───▼─┐ ┌─▼───┐  ┌─────▼──┐ ┌─▼───────┐
│ Dog │ │ Bat │  │ Parrot │ │ Ostrich │
└─────┘ └─────┘  └────────┘ └─────────┘

# 能跑”和“能飞”来归类
                ┌──────────┐
          ┌─────┤  Animal  ├───┐
          │     └──────────┘   │
          │                    │
          │                    │
    ┌─────▼─────┐        ┌─────▼──────┐
    │  Runnable │        │  Flyable   │
    └─┬──────┬──┘        └──┬───────┬─┘
      │      │              │       │
      │      │              │       │
 ┌────▼─┐ ┌──▼──────┐  ┌────▼───┐ ┌─▼───┐
 │ Dog  │ │ Ostrich │  │ Parrot │ │ Bat │
 └──────┘ └─────────┘  └────────┘ └─────┘

# 两种分类都包含进来
                          ┌───────────┐
                     ┌────┤   Animal  ├────┐
                     │    └───────────┘    │
                     │                     │
                ┌────▼─────┐         ┌─────▼────┐
                │  Mammal  │         │  Bird    │
                └┬───────┬─┘         └┬───────┬─┘
                 │       │            │       │
             ┌───▼──┐ ┌──▼───┐   ┌────▼─┐   ┌─▼─────┐
             │ MRun │ │ MFly │   │ BRun │   │ BFly  │
             └──┬───┘ └──┬───┘   └───┬──┘   └───┬───┘
                │        │           │          │
             ┌──▼───┐ ┌──▼───┐  ┌────▼────┐ ┌───▼────┐
             │ Dog  │ │ Bat  │  │ Ostrich │ │ Parrot │
             └──────┘ └──────┘  └─────────┘ └────────┘

```

避免类的数量呈指数增长采用多重继承

```py
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
```

#### MixIn

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，`Ostrich`继承自`Bird`。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让`Ostrich`除了继承自`Bird`外，再同时继承`Runnable`。这种设计通常称之为**MixIn**。
肉食动物`CarnivorousMixIn`和植食动物`HerbivoresMixIn`

```py
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')
class CarnivorousMixIn(object):
    def eat(self):
        print("eat mean .....")

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
```

Python自带的很多库也使用了MixIn。举个例子，Python自带了`TCPServer`和`UDPServer`这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由`ForkingMixIn`和`ThreadingMixIn`提供。通过组合，我们就可以创造出合适的服务来。

```py
# 编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 如果打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
```

### 定制类

`__len__()`方法是为了能让`class`作用于`len()`函数

#### `__str__`

`__str__()`返回用户看到的字符串; `__repr__()`返回程序开发者看到的字符串,为调试服务

```py
# ex 1
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
# <__main__.Student object at 0x0000029082FC7880>

# ex 2
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael'))
# Student object (name: Michael)

s = Student('Michael')
s
# <__main__.Student object at 0x0000029082FC7880>

# ex 3
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Student('Michael'))
# Student object (name: Michael)

s = Student('Michael')
s
# Student object (name: Michael)   
```

#### `__iter__`

用于`for ... in`循环,实现一个`__iter__()`方法,返回一个迭代对象,`for`循环会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环

```py
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)
# 1
# 1
# 2
# 3
# 5
# ...
# 46368
# 75025
```

#### `__getitem__`

`Fib`实例虽然能作用于`for`循环，和`list`有点像，但是，把它当成`list`来使用还是不行
按照下标取出元素，需要实现`__getitem__()`

```py
Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
f[0]    # 1
f[1]    # 1
f[2]    # 2
f[3]    # 3
f[10]   # 89
f[100]  # 573147844013817084101

list(range(100))[5:10] # list 切片方法
# [5, 6, 7, 8, 9]

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
f[0:5]  # [1, 1, 2, 3, 5]
f[:10]  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
f[:10:2] # 没有对step参数 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 也没有对负数作处理
```

如果把对象看成`dict`，`__getitem__()`的参数也可能是一个可以作`key`的`object`，例如`str`。
与之对应的是`__setitem__()`方法，把对象视作`list`或`dict`来对集合赋值。最后，还有一个`__delitem__()`方法，用于删除某个元素。

总之，通过上面的方法，定义的类表现得和Python自带的`list`、`tuple`、`dict`没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

#### `__getattr__`

`__getattr__`默认返回就是`None`

```py
class Student(object):
    def __init__(self):
        self.name = 'Michael'

s = Student()
print(s.name)       # Michael
print(s.score)
# Traceback (most recent call last):
#   ...
# AttributeError: 'Student' object has no attribute 'score'

# 避免错误 除了加上一个score属性外，可写一个__getattr__()方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = Student()
s.name     # Michael
s.score    # 99

# 返回函数也可以
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

s.age()  # 25

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

Chain().status.user.timeline.list  # /status/user/timeline/list

class Chain(object):
    def __init__(self, path='') -> None:
        self._path = path
    def __getattr__(self, path):
        return Chain("{}/{}".format(self._path, path))
    def __str__(self):
        return self._path
    def __call__(self, name):
        return Chain("{}/{}".format(self._path, name))
    __repr__ = __str__
# Chain().users('michael').repos     # /users/:user/repos

# 1. Chain()                            # 
# 2. Chain().users                      # /users                --> __getattr__
# 3. Chain().users('michael')           # /users/michael                          -->  __call__
# 4. Chain().users('michael').repos     # /users/michael/repos                                    --> __getattr__ --> __reper__ --> __str__
```

#### `__call__`

直接在实例本身上调用属性和方法
`__call__()`还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，完全可以把对象看成函数，把函数看成对象，这两者之间没啥根本的区别。
判断一个对象是否能被调用，能被调用的对象就是一个`Callable`对象

```py
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()             # self参数不要传入
# My name is Michael.

callable(Student())  # True
callable(max)        # True
callable([1, 2, 3])  # False
callable(None)       # False
callable('str')      # False
```

### 使用枚举类

`value`是自动赋给成员的`int`常量，默认从`1`开始。

```py
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

Month.Jan       # <Month.Jan: 1>

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

from enum import unique
# 精确控制枚举类型
@unique             # 检查保证没有重复值
class Weekday(Enum):
    Sun = 0  # Sun的value设为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)             # Weekday.Mon
print(Weekday.Tue)      # Weekday.Tue
print(Weekday['Tue'])   # Weekday.Tue
print(Weekday.Tue.value)# 2
print(day1 == Weekday.Mon) # True
print(day1 == Weekday.Tue) # False
print(Weekday(1))       # Weekday.Mon
print(day1 == Weekday(1)) # True
Weekday(7)        
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday

for name,member in Weekday.__members__.items():
    print(name, '=>', member)

# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
```

### 使用元类

#### `type()`

```py
# hello.py
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
from hello import Hello
h = Hello()
h.hello()  #Hello, world.

# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
print(type(Hello))  # <class 'type'>
print(type(h))      # <class 'hello.Hello'>
```

`type()`函数既可以返回一个对象的类型，又可以创建出新的类型

创建`class`对象，`type()`函数依次传入3个参数：

1. `class`的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了`tuple`的单元素写法；
3. `class`的方法名称与函数绑定，把函数`fn`绑定到方法名`hello`。

```py
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()           # Hello, world.
print(type(Hello))  # <class 'type'>
print(type(h))      # <class '__main__.Hello'>
```

#### `metaclass`

元类：`metaclass`允许创建类或者修改类。换句话说，可以把类看成是`metaclass`创建出来的“实例”

`__new__()`方法接收到的参数依次是：

1. 当前准备创建的类的对象；
2. 类的名字；
3. 类继承的父类集合；
4. 类的方法集合。

```py
# metaclass是类模板，必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass
#当传入关键字参数metaclass时，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
#在此，可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

L = MyList()
L.add(1)
L    # [1]

# 普通的list没有add()方法
L2 = list()
L2.add(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'add'
```

ORM全称“Object Relational Mapping”( 对象-关系映射)

```py
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# Found model: User
# Found mapping: id ==> <IntegerField:id>
# Found mapping: name ==> <StringField:username>
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
```

当用户定义一个`class User(Model)`时，Python解释器首先在当前类`User`的定义中查找`metaclass`，如果没有找到，就继续在父类`Model`中查找`metaclass`，找到了，就使用`Model`中定义的`metaclass`的`ModelMetaclass`来创建`User`类，也就是说，`metaclass`可以隐式地继承到子类，但子类自己却感觉不到。

在`ModelMetaclass`中，一共做了几件事情：

1. 排除掉对`Model`类的修改；
2. 在当前类（比如`User`）中查找定义的类的所有属性，如果找到一个`Field`属性，就把它保存到一个`__mappings__`的`dict`中，同时从类属性中删除该`Field`属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
3. 把表名保存到`__table__`中，这里简化为表名默认为类名。
4. 在`Model`类中，就可以定义各种操作数据库的方法，比如`save()`，`delete()`，`find()`，`update`等等。

我们实现了`save()`方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。

## 错误、调试和测试

bug，程序问题，用户问题，环境问题等

### 错误处理

约定返回错误代码

```py
def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass
```

#### `try`

内置`try...except...finally...`机制，所有的错误类型都继承自`BaseException`

常见错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

```py
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
# try...
# except: division by zero
# finally...
```

```py
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')      # 当没有错误发生时
finally:
    print('finally...')

# try...
# result: 5.0
# no error!
# finally...
```

可以跨越多层调用

```py
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()
# Error: division by zero
# finally...
```

#### 调用栈

如果错误没有被捕获，就会一直往上抛，最后被Python解释器捕获，打印错误信息，然后程序退出
**出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置**

```py
# err.py:
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()

# Traceback (most recent call last):
#   File "err.py", line 7, in <module>
#     main()
#   File "err.py", line 6, in main
#     bar('0')
#   File "err.py", line 4, in bar
#     return foo(s) * 2
#   File "err.py", line 2, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
```

#### 记录错误

Python内置的`logging`模块可以非常容易地记录错误信息,程序打印完错误信息后会继续执行，并正常退出
通过配置，`logging`可以把错误记录到日志文件。

```py
# err_logging.py
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')

# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "err_logging.py", line 8, in main
#     bar('0')
#   File "err_logging.py", line 5, in bar
#     return foo(s) * 2
#   File "err_logging.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# END
```

#### 抛出错误

定义一个错误的`class`，选择好继承关系，用`raise`语句抛出一个错误的实例
`raise`语句如果不带参数，就会把当前错误原样抛出
由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛

```py
# err_raise.py
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

# Traceback (most recent call last):
#   File "err_raise.py", line 9, in <module>
#     foo('0')
#   File "err_raise.py", line 6, in foo
#     raise FooError('invalid value: %s' % s)
# __main__.FooError: invalid value: 0
```

### 调试

1. `print`
2. `assert`
3. `logging`
4. ``

#### 断言

`print` 打印找错后续麻烦，断言(assert) 来代替
断言失败，`assert`语句本身就会抛出`AssertionError`
启动Python解释器时可以用`-O`参数来关闭`assert`(大写字母`O`)  `> python -O err.py`

```py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
main()

# Traceback (most recent call last):
#   File "err.py", line 7, in <module>
#     main()
#   File "err.py", line 6, in main
#     foo('0')
#   File "err.py", line 3, in foo
#     assert n != 0, 'n is zero!'
# AssertionError: n is zero!
```

#### `logging`

有`debug`，`info`，`warning`，`error`等几个级别
通过简单配置，一条语句可以同时输出到不同的地方，比如`console`和文件。

```py
import logging
logging.basicConfig(level=logging.INFO)  # 加这个,不指定级别 log不生效，生效的只是指定级别的log
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 6, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero
```

#### pdb

启动Python的调试器pdb,单步方式运行,随时查看运行状态

```txt
$ python -m pdb err.py
> c:\users\steven\downloads\err.py(2)<module>()
-> s = '0'

(Pdb) l  # 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
[EOF]

#  输入命令n可以单步执行代码：

(Pdb) n
> c:\users\steven\downloads\err.py(3)<module>()
-> n = int(s)
(Pdb) n
> c:\users\steven\downloads\err.py(4)<module>()
-> print(10 / n)

# 任何时候都可以输入命令p 变量名来查看变量
(Pdb) p s
'0'
(Pdb) p n
0

# 输入命令q结束调试，退出程序
(Pdb) q
```

`pdb.set_trace()` 不需要单步执行,可能出错的地方用它设置断点

```py
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
```

```txt
> c:\users\steven\downloads\err.py(7)<module>()
-> print(10 / n)

# 用命令p查看变量，或者用命令c继续运行
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "err.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

IDE
如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
PyCharm：http://www.jetbrains.com/pycharm/
另外，Eclipse加上pydev插件也可以调试Python程序。
**用IDE调试起来比较方便，但是logging才是终极武器**

### 单元测试

测试驱动开发（TDD：Test-Driven Development）

```py
# mydict.py
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
```

```py
# mydict_test.py
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):  # 继承自 unittest.TestCase

    def test_init(self):            #  test开头是测试方法，不以 test 开头认为不是测试方法，不会执行
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')   # assertEqual

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): # assertRaises
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
```

#### 运行单元测试

1. 最简单，在 `mydict_test.py` 最后加上两行代码

```py
if __name__ == '__main__':
    unittest.main()
```

把`mydict_test.py`当做正常的python脚本运行 `$ python mydict_test.py`
2. 命令行加参数 `-m unittest` 直接运行(**推荐**)

```txt
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

#### `setUp`与`tearDown`

`setUp()`和`tearDown()`这两个方法会分别在每调用一个测试方法的前后分别被执行。
测试需要启动数据库时，可以在`setUp()`中连接数据库，在`tearDown()`中关闭数据库

```py
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')
    def tearDown(self):
        print('tearDown...')
```

小结
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

### 文档测试

Python内置的“文档测试”（doctest）模块可以直接提取**注释中的代码**并执行测试。

```py
import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
# 'def'

def abs(n):
    '''
    Function to get absolute value of number.
    
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
```

```py
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#  当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest
if __name__=='__main__':
    import doctest
    doctest.testmod()
```

```bash
$ python mydict2.py
# 什么输出也没有 说明doctest运行都是正确的

# 把__getattr__()方法注释掉，再运行就会报错
$ python mydict2.py
**********************************************************************
File "mydict2.py", line 8, in __main__.Dict
Failed example:
    d1.x
Exception raised:
    Traceback (most recent call last):
      File "D:\Programs\Python\Python38\lib\doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.Dict[2]>", line 1, in <module>
        d1.x
    AttributeError: 'Dict' object has no attribute 'x'
**********************************************************************
File "mydict2.py", line 14, in __main__.Dict
Failed example:
    d2.c
Exception raised:
    Traceback (most recent call last):
      File "D:\Programs\Python\Python38\lib\doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.Dict[6]>", line 1, in <module>
        d2.c
    AttributeError: 'Dict' object has no attribute 'c'
**********************************************************************
1 items had failures:
   2 of   9 in __main__.Dict
***Test Failed*** 2 failures.
```

## IO编程

Input/Output，输入和输出
Stream（流）,只能单向流动
同步IO;异步IO

### 文件读写

在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）

#### 读文件

`open`传入文件名和标示符，打开文件对象
文件不存在，`open()`函数会抛出`IOError`错误

调用`read()`会一次性读取文件的全部内容，如果文件有10G，内存就爆了，保险起见，可以反复调用`read(size)`方法，每次最多读取`size`个字节的内容。另外，调用`readline()`可以每次读取一行内容，调用`readlines()`一次读取所有内容并按行返回`list`。因此，要根据需要决定怎么调用。

如果文件很小，`read()`一次性读取最方便；如果不能确定文件大小，反复调用`read(size)`比较保险；如果是配置文件，调用`readlines()`最方便：

```py
f = open('/Users/michael/test.txt', 'r')  #  r 代表只读
f2 = open('/Users/michael/notfound.txt', 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

f.read()    # 一次读取文件的全部内容，把内容读到内存，用一个str对象表示
# 'Hello, world!'
f.close()   # 文件使用完毕后必须关闭，文件对象会占用操作系统的资源，操作系统同一时间能打开的文件数量有限
```

```py
# 保证无论是否出错都能正确地关闭文件
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 和上面的try catch 效果一样
with open('/path/to/file', 'r') as f:
    print(f.read())

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

##### file-like Object

像`open()`函数返回的这种有个`read()`方法的对象，在Python中统称为**file-like Object**。除`file`外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个`read()`方法就行。
`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲。

##### 二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用`'rb'`模式打开文件即可：

```py
f = open('/Users/michael/test.jpg', 'rb')
f.read()
# b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

##### 字符编码

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数，例如，读取GBK编码的文件：

```py
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
# '测试'
```

遇到有些编码不规范的文件，可能会遇到`UnicodeDecodeError`，因为在文本文件中可能夹杂了一些非法编码的字符。这种情况，`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：`f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')`

#### 写文件

写文件和读文件是一样的，唯一区别是调用`open()`函数时，传入标识符`'w'`或者`'wb'`表示写文本文件或写二进制文件：

你可以反复调用`write()`来写入文件，但是务必要调用`f.close()`来关闭文件。写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用`close()`方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用`close()`的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，用`with`语句保险：

```py
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

要写入特定编码的文本文件，请给`open()`函数传入`encoding`参数，将字符串自动转换成指定编码。
以`'w'`模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。传入`'a'`以追加（append）模式写入。

### `StringIO`和`BytesIO`

从内存中读写`string`或者`bytes`与直接读写文件类似，有相同的接口

#### `StringIO`

`StringIO`在内存中读写`str`

```py
from io import StringIO
f = StringIO()
f.write('hello')
# 5
f.write(' ')
# 1
f.write('world!')
# 6
print(f.getvalue())     # hello world! # getvalue()方法获得写入后的str。


f = StringIO('Hello!\nHi!\nGoodbye!')  # 用str初始化
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# Hello!
# Hi!
# Goodbye!
```

#### `BytesIO`

操作二进制数据,内存中读写`bytes`

```py
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 6
print(f.getvalue())             # b'\xe4\xb8\xad\xe6\x96\x87'

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87') # 用bytes初始化BytesIO
f.read()    #b'\xe4\xb8\xad\xe6\x96\x87'
```

### 操作文件和目录

`os`模块可直接调用操作系统提供的接口函数。

```py
import os
os.name # 操作系统类型 posix:Linux、Unix或Mac OS X  ; nt:Windows
# nt 

os.uname() # 获取详细的系统信息 ; windows 上没有
# posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

os.environ # 操作系统中定义的环境变量
#environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Steven\\AppData\\Roaming', 'CLASSPATH': '.;D:\\Program Files\\Java\\jdk1.8.0_301\\lib;D:\\Program Files\\Java\\jdk1.8.0_301\\lib\\tools.jar', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', ...})

os.environ.get('PATH') # 获取某个环境变量的值, os.environ.get('key')
#  'C:\\Program Files\\Microsoft\\jdk-11.0.12.7-hotspot\\bin;D:\\Program Files (x86)\\VMware\\VMware Player\\bin\\;...'
```

#### 操作文件和目录

`os`模块，一部分在`os.path`模块

```py
os.path.abspath('.')        # 查看当前目录的绝对路径
# '/Users/michael'
os.path.join('/Users/michael', 'testdir') # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# '/Users/michael/testdir'

os.mkdir('/Users/michael/testdir')  # 创建一个目录
os.rmdir('/Users/michael/testdir')  # 删掉一个目录

os.path.split('/Users/michael/testdir/file.txt')  # 拆分路径
# ('/Users/michael/testdir', 'file.txt')

os.path.splitext('/path/to/file.txt')     # 得到文件扩展名
# ('/path/to/file', '.txt')
```

合并(`os.path.join()`)、拆分路径(`os.path.split`)函数不要求目录和文件要真实存在，它们只对字符串进行操作。处理不同操作系统的路径分隔符

```py
os.rename('test.txt', 'test.py')    # 对文件重命名
os.remove('test.py')                # 删掉文件

# shutil模块提供了copyfile()的函数
# 利用Python的特性来过滤文件

[x for x in os.listdir('.') if os.path.isdir(x)] # 列出当前目录下的所有目录
# ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] # 列出所有的.py文件
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
```

```py
# 前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def find(s: str, cur='.'):
    L = []
    if s.__len__() == 0:
        return L
    s = s.strip()

    def dfs(cur):
        for n in os.listdir(cur):
            # 如果不拼接下一目录则无法判断
            next_dir = os.path.join(cur, n)
            # 目录则递归
            if os.path.isdir(next_dir):
                dfs(next_dir)
            # 文件则返回绝对路径
            elif os.path.isfile(next_dir) and s in os.path.splitext(n)[0]:
                L.append(os.path.join(os.path.abspath('.'), n))
    return dfs(cur) or L

def find(s, name):
    d = [x for x in os.listdir(s) if os.path.isdir(os.path.join(s, x))]
    f = [x for x in os.listdir(s) if os.path.isfile(os.path.join(s, x)) and name in os.path.splitext(x)[0]]

    for x in f:
        print(os.path.join(s, x))
    for x in d:
        g = os.path.join(s, x)        
        find(g, name)
```

### 序列化

把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫`pickling`，在其他语言中也被称之为`serialization`，`marshalling`，`flattening`等等
把变量内容从序列化的对象重新读到内存里称之为反序列化，即`unpickling`

```py
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)     # 把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件; pickle.loads()
# b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

f = open('dump.txt', 'wb')
pickle.dump(d, f)       # 直接把对象序列化后写入一个file-like Object ； pickle.load()
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d           # {'age': 20, 'score': 88, 'name': 'Bob'}
```

JSON

JSON类型|Python类型
--|--
{}|dict
[]|list
"string"|str
1234.56|int或float
true/false|True/False
null|None

```py
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)                   # 返回 str,标准的JSON;  dump() 直接把JSON写入一个file-like Object
# '{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)            # loads() 把JSON的字符串反序列化; load() 从file-like Object中读取字符串并反序列化
# {'age': 20, 'score': 88, 'name': 'Bob'}

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
# Traceback (most recent call last):
#   ...
# TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable

def student2dict(std):  # Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))  # 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
# {"age": 20, "name": "Bob", "score": 88}

print(json.dumps(s, default=lambda obj: obj.__dict__))  # 把任意class的实例变为dict
# {"age": 20, "name": "Bob", "score": 88}
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# 把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
# <__main__.Student object at 0x000001D09E4C3190>

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
# '{"name": "\\u5c0f\\u660e", "age": 20}'
s = json.dumps(obj, ensure_ascii=False)
# '{"name": "小明", "age": 20}'
```

https://docs.python.org/3/library/json.html#json.dumps

## 进程和线程

多任务 多核CPU
轮流让各个任务交替执行
一个任务就是一个进程（Process）;进程内的“子任务”称为线程（Thread）

多任务的实现有3种方式：

1. 多进程模式；
2. 多线程模式；
3. 多进程+多线程模式。

Python既支持多进程，又支持多线程
线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂

### 多进程(multiprocessing)

Unix/Linux操作系统提供了一个`fork()`系统调用。普通的函数调用，调用一次，返回一次，但`fork()`调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回`0`，而父进程返回子进程的ID。一个父进程可以fork出很多子进程,父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

```py
import os

print("Process (%s) start ..." % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.

# multiprocessing模块就是跨平台版本的多进程模块
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 入一个执行函数和函数的参数
    print('Child process will start.')
    p.start()   # 启动线程
    p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')

# Parent process 21568.
# Child process will start.
# Run child process test (39220)...
# Child process end.
```

#### Pool

启动大量的子进程，用进程池的方式批量创建子进程

```py
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()        # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    print('All subprocesses done.')

# Parent process 39000.
# Waiting for all subprocesses done...
# Run task 0 (30104)...
# Run task 1 (38712)...
# Run task 2 (33176)...
# Run task 3 (40604)...
# Task 3 runs 0.34 seconds.
# Run task 4 (40604)...  # task 4要等待前面某个task完成后才执行,Pool的默认大小是4; p=Pool(5) no wait
# Task 4 runs 0.51 seconds.
# Task 1 runs 1.13 seconds.
# Task 0 runs 1.29 seconds.
# Task 2 runs 2.61 seconds.
# All subprocesses done.
```

#### 子进程

`subprocess`模块可以非常方便地启动一个子进程，然后控制其输入和输出

```py
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org']) # 命令行直接运行 nslookup www.python.org
print('Exit code:', r)

# $ nslookup www.python.org
# Server:  UnKnown
# Address:  172.22.68.1
# 
# Non-authoritative answer:
# Name:    dualstack.python.map.fastly.net
# Addresses:  2a04:4e42:1a::223
#           151.101.108.223
# Aliases:  www.python.org
# 
# Exit code: 0

# 子进程需要输入，则可通过communicate()方法输入
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # 在命令行执行命令 nslookup 然后手动输入 set q=mx python.org exit
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# $ nslookup
# Server:		192.168.19.4
# Address:	192.168.19.4#53
# 
# Non-authoritative answer:
# python.org	mail exchanger = 50 mail.python.org.
# 
# Authoritative answers can be found from:
# mail.python.org	internet address = 82.94.164.166
# mail.python.org	has AAAA address 2001:888:2000:d::a6
# 
# 
# Exit code: 0
```

#### 进程间通信

`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据

```py
# 一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

# Process to write: 23252
# Put A to queue...
# Process to read: 35356
# Get A from queue.
# Put B to queue...
# Get B from queue.
# Put C to queue...
# Get C from queue.
```

父进程所有Python对象都必须通过`pickle`序列化再传到子进程去，所以，如果`multiprocessing`在Windows下调用失败了，要先考虑是不是`pickle`失败了

在Unix/Linux下，可以使用`fork()`调用实现多进程。
要实现跨平台的多进程，可以使用`multiprocessing`模块。
进程间通信是通过`Queue`、`Pipes`等实现的。

### 多线程

Python的线程是真正的Posix Thread，不是模拟出来的线程。
`_thread`:低级模块，`threading`:高级模块

```py
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread') # 默认线程命名 Thread-1，Thread-2
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# thread MainThread is running...
# thread LoopThread is running...
# thread LoopThread >>> 1
# thread LoopThread >>> 2
# thread LoopThread >>> 3
# thread LoopThread >>> 4
# thread LoopThread >>> 5
# thread LoopThread is ended.
# thread MainThread ended.
```

#### Lock

```py
import time, threading
# 假定这是你的银行存款:
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)      # 29
```

```py
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):       
        lock.acquire()       # 先要获取锁
        try:           
            change_it(n)     # 放心地改吧
        finally:            
            lock.release()   # 改完一定要释放锁
```

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁,然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

```py

import threading, multiprocessing
def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
```

Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

### `ThreadLocal`

全局变量修改必须加锁,局部变量在函数调用时传递很麻烦

```py
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
```

每个线程处理不同的`Student`对象，不能共享

```py
# 用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象(理论上可行)
global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...
```

```py
import threading    
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()  # 线程程中方法参数传递

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)
```

`ThreadLocal`最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
一个`ThreadLocal`变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。`ThreadLocal`解决了参数在一个线程中各个函数之间互相传递的问题。

### 进程 vs. 线程

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用`fork`调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存;“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高,IIS服务器默认采用多线程模式

#### 线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去；线程切换需要消耗资源
多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降

#### 计算密集型 vs. IO密集型

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写

O密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

#### 异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。

### 分布式进程

在`Thread`和`Process`中，应当优选`Process`，因为`Process`更稳定且`Process`可以分布到多台机器上，而`Thread`最多只能分布到同一台机器的多个CPU上
`multiprocessing`模块不但支持多进程，其中`managers`子模块还支持把多进程分布到多台机器上,一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。`managers`模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

通过`managers`模块把`Queue`通过网络暴露出去，就可以让其他机器的进程访问`Queue`

```py
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')

# 在一台机器上写多进程程序时，创建的Queue可直接用，但在分布式多进程环境下，添加任务到Queue不可直接对原始task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
# task_worker.py
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

```

先启动`task_master.py`服务进程：

```bash
$ python3 task_master.py 
Put task 3411...
Put task 1605...
Put task 1398...
Put task 4729...
Put task 5300...
Put task 7471...
Put task 68...
Put task 4219...
Put task 339...
Put task 7866...
Try get results...
```

`task_master.py`进程发送完任务后，开始等待`result`队列的结果。现在启动`task_worker.py`进程：

```bash
$ python3 task_worker.py
Connect to server 127.0.0.1...
run task 3411 * 3411...
run task 1605 * 1605...
run task 1398 * 1398...
run task 4729 * 4729...
run task 5300 * 5300...
run task 7471 * 7471...
run task 68 * 68...
run task 4219 * 4219...
run task 339 * 339...
run task 7866 * 7866...
worker exit.
```

`task_worker.py`进程结束，在`task_master.py`进程中会继续打印出结果：

```bash
Result: 3411 * 3411 = 11634921
Result: 1605 * 1605 = 2576025
Result: 1398 * 1398 = 1954404
Result: 4729 * 4729 = 22363441
Result: 5300 * 5300 = 28090000
Result: 7471 * 7471 = 55815841
Result: 68 * 68 = 4624
Result: 4219 * 4219 = 17799961
Result: 339 * 339 = 114921
Result: 7866 * 7866 = 61873956
```

其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算`n*n`的代码换成发送邮件，就实现了邮件队列的异步发送。
`task_worker.py`中根本没有创建`Queue`的代码，所以，`Queue`对象存储在`task_master.py`进程中：

```txt
                                             │
┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
│task_master.py                           │  │  │task_worker.py                        │
│                                         │     │                                      │
│  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
│  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
│              │                          │  │  │              │                       │
│              │                          │     │              │                       │
│              ▼                          │  │  │              │                       │
│  ┌─────────────────────────────────┐    │     │              │                       │
│  │QueueManager                     │    │  │  │              │                       │
│  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
│  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
│  │ └────────────┘ └──────────────┘ │    │     │                                      │
│  └─────────────────────────────────┘    │  │  │                                      │
└─────────────────────────────────────────┘     └──────────────────────────────────────┘
                                             │

                                          Network
```

而`Queue`之所以能通过网络访问，就是通过`QueueManager`实现的。由于`QueueManager`管理的不止一个`Queue`，所以，要给每个`Queue`的网络调用接口起个名字，比如`get_task_queue`。

`authkey`有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果`task_worker.py`的`authkey`和`task_master.py`的`authkey`不一致，肯定连接不上。

总结：
Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
注意`Queue`的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

```py
# windows 测试可以过
# task_master.py
import queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

task_queue = queue.Queue()
result_queue = queue.Queue()

def return_task_queue():
    return task_queue
def return_result_queue():
    return result_queue

QueueManager.register('get_task_queue', callable=return_task_queue)
QueueManager.register('get_result_queue', callable=return_result_queue)

if __name__ == '__main__':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(100):
        print('向队列中插入了数字%d' % i)
        task.put(i)

    print('尝试从结果队列中取出结果')
    try:
        for i in range(100):
            r = result.get(timeout=100)
            print("结果：%s" % r)
    except queue.Empty:
        print('结果队列为空')

    manager.shutdown()
    print("主服务关闭")

# task_worker.py
import time, sys, queue
from multiprocessing.managers import BaseManager
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('正在连接主服务%s......' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

while True:
    try:
        n = task.get(timeout=1)
        print('从Queue取到了数字 %d' % n)
        print('正在执行运算 %d * %d' % (n, n))
        r = '%d * %d = %d  (from %s @ %s)' % (n, n, n * n, os.getpid(), ip)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('任务队列已空')
        break

print('工作进程【%s】已结束' % os.getpid())
```

## 正则表达式

用来匹配字符串的强有力的武器，用一种描述性的语言来给字符串定义一个规则

直接给出字符，就是精确匹配，用`\d`可以匹配一个数字，`\w`可以匹配一个字母或数字

* `'00\d'`可以匹配`'007'`，无法匹配`'00A'`
* `'\d\d\d'`可以匹配`'010'`
* `'\w\w\d'`可以匹配`'py3'`

`.`可以匹配任意字符

* `'py.'`可以匹配`'pyc'`、`'pyo'`、`'py!'`等

匹配变长的字符;用`*`表示任意个字符(包括0个)，用`+`表示至少一个字符，用`?`表示0个或1个字符，用`{n}`表示n个字符，用`{n,m}`表示n-m个字符

`\d{3}\s+\d{3,8}`: 可以匹配以任意个空格隔开的带区号的电话号码

1. `\d{3}`表示匹配3个数字，例如`'010'`
2. `\s`可以匹配一个空格(也包括Tab等空白符)，所以`\s+`表示至少有一个空格，例如匹配`' '，' '`等；
3. `\d{3,8}`表示3-8个数字，例如`'1234567'`。

`\d{3}\-\d{3,8}`：匹配`'010-12345'`;`'-'`是特殊字符，要用`'\'`转义

更精确地匹配，可以用`[]`表示范围

* `[0-9a-zA-Z\_]`可以匹配一个数字、字母或者下划线；
* `[0-9a-zA-Z\_]+`可以匹配至少由一个数字、字母或者下划线组成的字符串，比如`'a100'`，`'0_Z'`，`'Py3000'`等等；
* `[a-zA-Z\_][0-9a-zA-Z\_]*`可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
* `[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}`更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

`A|B`可以匹配A或B，所以(P|p)ython可以匹配`'Python'`或者`'python'`。
`^`表示行的开头，`^\d`表示必须以数字开头。
`$`表示行的结束，`\d$`表示必须以数字结束。

`py`也可以匹配`'python'`，但加上`^py$`变成整行匹配，只能匹配`'py'`

### `re`模块

`re`模块，包含所有正则表达式的功能
`match()`方法判断是否匹配，如果匹配成功，返回一个`Match`对象，否则返回`None`。

```py
s = 'ABC\\-001' # Python的字符串本身也用\转义
# 对应的正则表达式字符串变成：
# 'ABC\-001'

s = r'ABC\-001' # Python的字符串, 使用r前缀不用考虑转义问题
# 对应的正则表达式字符串不变：
# 'ABC\-001'

import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345') # <re.Match object; span=(0, 9), match='010-12345'>
re.match(r'^\d{3}\-\d{3,8}$', '010 12345') # 

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
```

用正则表达式切分字符串比用固定的字符更灵活

```py
# 不规范的输入转化成正确的数组
'a b   c'.split(' ')         # 无法识别连续的空格
# ['a', 'b', '', '', 'c']
re.split(r'\s+', 'a b   c')  # 无论多少个空格都可以正常分割
# ['a', 'b', 'c']
re.split(r'[\s\,]+', 'a,b, c  d')    # 加入,
# ['a', 'b', 'c', 'd']
re.split(r'[\s\,\;]+', 'a,b;; c  d') # 加入;
# ['a', 'b', 'c', 'd']
```

### 分组

提取子串;`()`表示要提取的分组(Group)

`^(\d{3})-(\d{3,8})$` 定义了两个组:直接从匹配的字符串中提取出区号和本地号码
在`Match`对象上用`group()`提取出子串
`group(0)`永远是与整个正则表达式相匹配的字符串，`group(1)`、`group(2)`……表示第1、2、……个子串。

```py
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m           # <re.Match object; span=(0, 9), match='010-12345'>
m.group(0)  # '010-12345'
m.group(1)  # '010'
m.group(2)  # '12345'

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)              # 识别合法的时间
m.groups()          # ('19', '05', '30')
```

有时,正则表达式也无法做到完全验证,比如识别日期 `'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'`;识别不了`'2-30'`，`'4-31'`这样的非法日期,需要程序配合识别

### 贪婪匹配

默认是贪婪匹配, 匹配尽可能多的字符

```py
# 匹配出数字后面的0
re.match(r'^(\d+)(0*)$', '102300').groups()         # ('102300', '')
# \d+ 采用贪婪匹配，把后面的0全部匹配，结果0*只能匹配空字符串

# 加个?就可以让\d+采用非贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()        # ('1023', '00')
```

### 编译

`re`模块内部会两件事情：

1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串

```py
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')   # 编译
re_telephone.match('010-12345').groups()
# ('010', '12345')
re_telephone.match('010-8086').groups()
# ('010', '8086')
```

```py
import re
def is_valid_email(addr):
    return re.match(r'^[A-Za-z0-9\u4e00-\u9fa5.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', addr)

# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')

def name_of_email(addr):
    names = re.match(r'^<([a-zA-Z\s]+)>|([a-zA-Z0-9\s]+)@[a-zA-z0-9]+\.[a-zA-Z0-9]+$', addr)
    if names:
        if names.group(1) == None:
            return names.group(2)
        else:
            return names.group(1)
    else:
        return ""

def name_of_email(addr):
    m=re.match(r'^\<?([a-zA-Z\s]+)\>?[a-zA-Z\s]*\@[a-zA-Z]+\.[a-zA-Z]+$',addr)
    print(m.group(1))
    return m.group(1)

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
```

## 常用内建模块

batteries included

### `datetime`

仅导入`import datetime`，必须引用全名`datetime.datetime`
1970年1月1日 00:00:00 UTC+00:00时区的时刻称为`epoch time`，记为`0`(1970年以前的时间timestamp为负数),当前时间就是相对于epoch time的秒数，称为timestamp。
`timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00`
BJ Tiem:`timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00`
timestamp的值与时区毫无关系

```py
## 获取当前日期和时间
from datetime import datetime
now = datetime.now()        # 获取当前datetime
print(now)          # 2022-07-21 10:58:54.283119
print(type(now))    # <class 'datetime.datetime'>

## 获取指定日期和时间
dt = datetime(2022, 5, 20, 13, 14) # 用指定日期时间创建datetime
print(dt)           # 2022-05-20 13:14:00

## datetime转换为timestamp
dt.timestamp()      # 1653023640.0    # 整数位表示秒

## timestamp转换为datetime
t = 1653023640.0
print(datetime.fromtimestamp(t))           # 2022-05-20 13:14:00  在timestamp和本地时间(当前操作系统设定的时区)做转换
# 本地时间(BJ UTC+8)：2022-05-20 13:14:00 UTC+8:00 --> 格林威治标准时间：2022-05-20 05:14:00 UTC+0:00
print(datetime.utcfromtimestamp(t)) # UTC时间
# 2022-05-20 05:14:00

## str转换为datetime
cday = datetime.strptime('2022-5-20 05:14:00', '%Y-%m-%d %H:%M:%S') # 需要日期和时间格式  详见 https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(cday)         # 2022-05-20 05:14:00

## datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))      # 需要一个日期和时间的格式化字符串
# Thu, Jul 21 11:26
```

`datetime`类型有时区属性`tzinfo`，默认`None`，无法区分`datetime`是哪个时区，除非给`datetime`设置一个时区

```py
## datetime加减
from datetime import datetime, timedelta
now = datetime.now()
now                 
# datetime.datetime(2022, 7, 21, 11, 29, 18, 265551)
now + timedelta(hours=10)
# datetime.datetime(2022, 7, 21, 21, 29, 18, 265551)
now - timedelta(days=1)
# datetime.datetime(2022, 7, 20, 11, 29, 18, 265551)
now + timedelta(days=2, hours=12)
# datetime.datetime(2022, 7, 23, 23, 29, 18, 265551)

## 本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
now
# datetime.datetime(2022, 7, 21, 17, 25, 5, 866983)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00(系统时区恰好是UTC+8:00,正确;否则，不能强制设置为UTC+8:00时区)
# datetime.datetime(2022, 7, 21, 17, 25, 5, 866983, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800)))

## 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00；基准时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)       # 2022-07-21 09:28:47.426871+00:00

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)        # 2022-07-21 17:28:47.426871+08:00
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)     # 2022-07-21 18:28:47.426871+09:00
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)    # 2022-07-21 18:28:47.426871+09:00
```

`datetime`表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
存储`datetime`，最佳方法将其转换为`timestamp`存储，`timestamp`的值与时区完全无关

```py
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    hour = int(re.match(r'^UTC([\+\-]\d+)\:\d+$', tz_str).group(1))
    tz = timezone(timedelta(hours=hour))
    dt = dt.replace(tzinfo=tz)
    return dt.timestamp() 

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
```

### `collections`

#### `namedtuple`

创建自定义`tuple`对象，并规定`tuple`元素个数，可用属性而不是索引来引用`tuple`的某个元素
具备`tuple`不变性，又可根据属性来引用，使用十分方便

```py
# 创建自定义tuple对象
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x             # 1
p.y             # 2

isinstance(p, Point)    # True
isinstance(p, tuple)    # True
```

#### `deque`

`deque`为了高效实现**插入****和删除**操作的*双向列表*，适合用于队列和栈
`deque`除实现`list`的`append()`和`pop()`外，还支持`appendleft()`和`popleft()`

```py
from collections import deque
q = deque(['a', 'b', 'c'])
q   # deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q   # deque(['y', 'a', 'b', 'c', 'x'])
```

#### `defaultdict`

`dict`，引用的Key不存在，抛出`KeyError`
`defaultdict` key不存在时，返回调用函数返回的默认值

```py
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1'] # key1存在
# 'abc'
dd['key2'] # key2不存在，返回默认值
# 'N/A'
```

#### `OrderedDict`

保持Key的顺序，按照Key插入的顺序

```py
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
d       # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# FIFO（先进先出）
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

d = LastUpdatedOrderedDict(2)
d['x'] = 3          # add ('x', 3)
d['y'] = 4          # add ('y', 4)
print(d)            # LastUpdatedOrderedDict([('x', 3), ('y', 4)])
d['z'] = 5          # remove: ('x', 3)   add ('z', 5)
print(d)            # LastUpdatedOrderedDict([('y', 4), ('z', 5)])
```

#### `ChainMap`

`ChainMap`本身是`dict`,把一组`dict`串起来并组成一个逻辑上的`dict`;按照顺序在内部`dict`依次查找
应用程序往往都需要传入参数，参数可通过命令行传入，可通过环境变量传入，还可有默认参数。可用`ChainMap`实现参数优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数

```py
from collections import ChainMap
import os, argparse

from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
```

```cmd
> python3 use_chainmap.py 
color=red
user=guest

> python3 use_chainmap.py -u bob
color=red
user=bob

# 同时传入命令行参数和环境变量，命令行参数的优先级较高
>user=admin color=green python3 use_chainmap.py -u bob
color=green
user=bob
```

#### `Counter`

```py
# 简单的计数器
from collections import Counter  # dict子类
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
c.update('hello') # 也可以一次性update
c
# Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})#
```

### base64

Base64是一种用64个字符来表示任意二进制数据的方法

Base64的原理:

1. 准备一个包含64个字符的数组,`['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']`
2. 对二进制数据进行处理，每3个字节一组，一共是`3x8=24`bit，划为4组，每组正好6个bit

    ```txt
    │       b1      │      b2       │      b3       │
    ┌───────────────┬───────────────┬───────────────┐
    │               │# # # # # # # #│               │
    └───────────────┴───────────────┴───────────────┘
    ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
    │ │ │ │ │ │ │ │ │#│#│#│#│#│#│#│#│ │ │ │ │ │ │ │ │
    └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
    ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
    │ │ │ │ │ │ │#│#│#│#│#│#│ │ │ │ │ │ │#│#│#│#│#│#│
    └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
    │    n1     │     n2    │    n3     │    n4     │
    ```

3. 得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串

Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
编码的二进制数据不是3的倍数，最后会剩下1个或2个字节？Base64用`\x00`字节在末尾补足后，再在编码的末尾加上1个或2个`=`号，表示补了多少字节，解码的时候，会自动去掉。

"url safe"的base64编码，把字符`+`和`/`分别变成`-`和`_`
Base64适用于小段内容编码，比如数字证书签名、Cookie的内容等
`=`用在URL、Cookie里面会造成歧义，很多Base64编码后会把`=`去掉;解码加上`=`把Base64字符串的长度变为4的倍数

```py
import base64
base64.b64encode(b'binary\x00string')
# b'YmluYXJ5AHN0cmluZw=='
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# b'binary\x00string'

## "url safe"的base64编码，把字符+和/分别变成-和_
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd--__'
base64.urlsafe_b64decode(b'abcd--__')
# b'i\xb7\x1d\xfb\xef\xff'

def safe_base64_decode(s):
    c = len(s) % 4
    for i in range(c):
        s = s+"="
    return base64.b64decode(s)

def safe_base64_decode(s):
    x = 4-len(s)%4
    s = s + '=' * x
    return base64.b64decode(s)

# 不足的=补足就行，多了也不会解错
def safe_base64_decode(s):
    return base64.b64decode(s+"====")

assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
```

### `struct`

没有专门处理字节的数据类型.`b'str'`可以表示字节,字节数组＝二进制str
`struct` 解决`bytes`和其他二进制数据类型的转换
`struct`的`pack`函数把任意数据类型变成`bytes`;
`>I`:`>`表示字节顺序是big-endian，也就是网络序，`I`表示4字节无符号整数
`>IH`:后面的b`ytes`依次变为`I`：4字节无符号整数和`H`：2字节无符号整数
https://docs.python.org/3/library/struct.html#format-characters

```py
# 把一个32位无符号整数变成字节，也就是4个长度的bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
bs  # b'\x00\x9c@c'

import struct
struct.pack('>I', 10240099)         # b'\x00\x9c@c'
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')   #  (4042322160, 32896)

# Windows位图文件（.bmp）
# 两个字节:'BM'表示Windows位图,'BA'表示OS/2位图;一个4字节整数:表示位图大小;一个4字节整数:保留位，始终为0; 一个4字节整数:实际图像的偏移量;一个4字节整数:Header的字节数;一个4字节整数:图像宽度;一个4字节整数:图像高度;一个2字节整数:始终为1;一个2字节整数:颜色数.
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
struct.unpack('<ccIIIIIIHH', s)
# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
## 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
```

```py
# 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
# -*- coding: utf-8 -*-
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):    
    t = struct.unpack('<ccIIIIIIHH',bmp_data[0:30])
    if t[0:2] == (b'B', b'M'):
        return {
            'width': t[-4],
            'height': t[-3],
            'color': t[-1]
        }

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
```

### `haslib`

摘要算法又称哈希算法、散列算法(MD5，SHA1等等);通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）

MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示
SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，越安全的算法不仅越慢，而且摘要长度更长
碰撞:两个不同的数据通过某个摘要算法得到了相同的摘要

```py
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())       # d26a53750bc40b38b65a520292f69306

# 分多次调用
md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print(md52.hexdigest())      # d26a53750bc40b38b65a520292f69306

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())      # 2c76b57293ce30acef38d98f6046927161b46a44
```

```py
# -*- coding: utf-8 -*-
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest() == db[user]

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```

由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

```py
def calc_md5(password):
    return get_md5(password + 'the-Salt')

# 用户无法修改登录名
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
```

```py
# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password+self.salt)

db = {
    'michael':User('michael','123456'),
    'bob':User('bob','abc999'),
    'alice':User('alice','alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```

### `hmac`

Hmac算法：Keyed-Hashing for Message Authentication;通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
采用Hmac替代salt算法，可使程序算法更标准化，也更安全
传入的`key`和`message`都是`bytes`类型，`str`类型需要编码为`bytes`

```py
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用 h.update(msg)
h.hexdigest()       # 'fa4ee7d173f2d97ee79022d1a7355bcf'
```

```py
# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```

### `itertools`

用于操作迭代对象的函数
`count()`创建一个无限迭代器
`cycle()`把传入的一个序列无限重复下去
`repeat()`把一个元素无限重复下去，第二个参数可限定重复次数
通过`takewhile()`等函数根据条件判断来截取出一个有限的序列

`chain()`把一组迭代对象串联起来，形成更大的迭代器
`groupby()`把迭代器中相邻的重复元素挑出来放在一起;挑选规则通过函数完成,作用于函数的两个元素返回的值相等,两个元素就被认为是在一组,函数返回值作为组的*key*

**`itertools`模块提供的全部是处理迭代的函数，返回值不是`list`，而是`Iterator`，用`for`循环迭代的时候才真正计算**

```py
# “无限”迭代器
import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)
# ...
# 1
# 2
# 3
# ...

cs = itertools.cycle('ABC')
for c in cs:
    print(c)
# ...
# 'A'
# 'B'
# 'C'
# 'A'
# 'B'
# 'C'
# ...

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
# A
# A
# A

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10, natuals)
list(ns)            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for c in itertools.chain('ABC','XYZ'):
    print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c : c.upper()):
    print(key, list(group))
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']
```

```py
# -*- coding: utf-8 -*-
import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    odds = (x for x in natuals if x % 2 == 1)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    oddN = itertools.takewhile(lambda x: x <= 2*N-1, odds)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    L = [4/((-1)**i*value) for i,value in enumerate(list(oddN))]    ##  sym = itertools.cycle([1,-1])    L = [4/(i*next(sym)) for i in list(ns)]
    # step 4: 求和:
    return sum(L) 

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

# 创意答案
def pi(n):
    odds = itertools.takewhile(lambda x: x < 2 * n, itertools.count(1, 2))    
    fac = itertools.cycle([1, -1])    
    sum = 0   
    for i in odds:
        sum += 4 * next(fac) / i
    return sum

def pi(N):
    odds = itertools.takewhile(lambda x: x < 2 * N, itertools.count(1, 2))
    fac = itertools.cycle([1, -1])
    L = [4/i*next(fac) for i in list(odds)]
    return sum(L)
```

### `contextlib`

任何对象，正确实现上下文管理，就可用`with`语句
上下文管理通过`__enter__`和`__exit__`两个方法实现

```py
# 关闭文件麻烦的写法
try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close

# 简化
with open('/path/to/file', 'r') as f:
    f.read()

class Query(object):
    def __init__(self, name):
        self.name = name    
    def __enter__(self):
        print('Begin')
        return self    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')    
    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

# Begin
# Query info about Bob...
# End
```

#### `@contextmanager`

`@contextmanager`这个decorator接受一个generator，用`yield`语句把`with ... as var`把变量输出，然后，`with`语句就可以正常工作
`@contextmanager`通过编写generator来简化上下文管理

```py
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# Begin
# Query info about Bob...
# End

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# <h1>
# hello
# world
# </h1>
```

1. `with`语句首先执行`yield`之前的语句，因此打印出`<h1>`；
2. `yield`调用会执行`with`语句内部的所有语句，因此打印出`hello`和`world`；
3. 最后执行`yield`之后的语句，打印出`</h1>`

#### `@closing`

把任意对象变为上下文对象，并支持`with`语句

```py
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

[other with blogs](http://www.cnblogs.com/nnnkkk/p/4309275.html)

### `urllib`

#### Get

```py
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# Status: 200 OK
# Server: nginx
# Date: Tue, 26 May 2015 10:02:27 GMT
# Content-Type: application/json; charset=utf-8
# Content-Length: 2049
# Connection: close
# Expires: Sun, 1 Jan 2006 01:00:00 GMT
# Pragma: no-cache
# Cache-Control: must-revalidate, no-cache, private
# X-DAE-Node: pidl1
# Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["编著"],"pubdate":"2007-6",...}

# 模拟 iphone 6 访问豆瓣
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
# ...
#     <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
#     <meta name="format-detection" content="telephone=no">
#     <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
# ...
```

#### Post

把参数`data`以`bytes`形式传入

```py
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

##### 成功记录
# Status: 200 OK
# Server: nginx/1.2.0
# ...
# Set-Cookie: SSOLoginState=1432620126; path=/; domain=weibo.cn
# ...
# Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}}

##### 失败
# ...
# Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"example@python.org","errline":536}}
```

```py
# -*- coding: utf-8 -*-
from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        jsonstr = f.read().decode('utf-8')   
    return json.loads(jsonstr)

# 测试
URL = 'https://echarts.apache.org/examples/data/asset/data/life-expectancy-table.json'
data = fetch_data(URL)
print(data[0])
```

#### Handler

需要更复杂的控制，比如通过一个Proxy去访问网站，利用`ProxyHandler`来处理

```py
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
```

### XML

操作XML有两种方法：DOM和SAX
DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
SAX是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件

优先考虑SAX

SAX解析XML非常简洁,关心的事件是`start_element`，`end_element`和`char_data`

当SAX解析器读到一个节点时`<a href="/">python</a>`会产生3个事件：

1. `start_element`事件，在读取`<a href="/">`时；
2. `char_data`事件，在读取`python`时；
3. `end_element`事件，在读取`</a`>时

```py
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self, name):
        print('sax:end_element: %s' % name)
    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# sax:start_element: ol, attrs: {}
# sax:char_data:
# 
# sax:char_data:
# sax:start_element: li, attrs: {}
# sax:start_element: a, attrs: {'href': '/python'}
# sax:char_data: Python
# sax:end_element: a
# sax:end_element: li
# sax:char_data:
# 
# sax:char_data:
# sax:start_element: li, attrs: {}
# sax:start_element: a, attrs: {'href': '/ruby'}
# sax:char_data: Ruby
# sax:end_element: a
# sax:end_element: li
# sax:char_data:
# 
# sax:end_element: ol
# 1

# 生成 XML ；复杂的XML建议改用 JSON
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
return ''.join(L)
```

读取一大段字符串时，`CharacterDataHandler`可能被多次调用，所以需要保存起来，在`EndElementHandler`里面再合并

```py
# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def __init__(self):
        self.name =''
        self.data = {}
    def start_element(self, name, attrs):
        self.name = name
        print('sax:start_element:%s, attrs:%s' %(name, str(attrs)))
    def end_element(self, name):
        print('sax:end_element:%s' % name)
    def char_data(self, text):
        self.data[self.name] = text
        print('sax:char_data: %s' % text)


def parseXml(xml_str):
    """
    :param xml_str: XML 格式天气预报
    :return: 当前城市实时天气预报结果
    """
    print(xml_str)
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    data = handler.data
    print(data)
    # {'status': '1', 'count': '1', 'info': 'OK', 'infocode': '10000', 'province': '北京', 'city': '北京市', 'adcode': '110000', 'weather': '多云', 'temperature': '21', 'winddirection': '东', 'windpower': '≤3', 'humidity': '72', 'reporttime': '2021-05-14 19:33:56'}
    return {
        'city': data['city'],
        'live': {
            'data': data['reporttime'],
            'weather': data['weather'],
            'temperature' : data["temperature"]
        }
    }

# 注意空格和换行会影响结果
data = r'''<response><status>1</status><count>1</count><info>OK</info><infocode>10000</infocode><lives type="list"><live>
<province>北京</province>
<city>北京市</city>
<adcode>110000</adcode>
<weather>多云</weather>
<temperature>21</temperature>
<winddirection>东</winddirection>
<windpower>≤3</windpower>
<humidity>72</humidity>
<reporttime>2021-05-14 19:33:56</reporttime>
</live>
</lives>
</response>
'''

result = parseXml(data.replace('\n','').replace('\r',''))
print(result)
assert result['city'] == '北京市'
```

### `HTMLParser`

HTML本质上是XML的子集，但HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML

`feed()`方法可多次调用，不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
两种特殊字符，一种英文表示的`&nbsp;`，一种数字表示的`&#1234;`，都可通过Parser解析

```py
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_data(self, data):
        print(data)
    def handle_comment(self, data):
        print('<!--', data, '-->')
    def handle_entityref(self, name):
        print('&%s;' % name)
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
```

```py
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from urllib import request
import re 

def get_data(url):
    with request.urlopen(url) as f:
        print("status:%s, resason:%s" % (f.status, f.reason))
        return f.read().decode('utf-8')

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata='' # 设置一个空的标志位
        self.info = []
       
    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'
    def handle_endtag(self, tag):
        self.__parsedata = ''# 在HTML 标签结束时，把标志位清空
    def handle_data(self, data):
        if self.__parsedata == 'name':
            # 通过标志位判断，输出打印标签内容
            self.info.append(f'会议名称:{data}')
        if self.__parsedata == 'time':
            self.info.append(f'会议时间:{data}')
        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                self.info.append(f'会议年份:{data.strip()}')
        if self.__parsedata == 'location':
            self.info.append(f'会议地点:{data} \n')

def main():
    parser = MyHTMLParser()
    data = get_data('https://www.python.org/events/python-events/')
    parser.feed(data)
    for s in parser.info:
        print(s)

if __name__ == '__main__':
   main()

## 2 
Name = r'<h3 class="event-title"><a href=".*">(.*)</a></h3>'    #匹配名称的正则
Location = r'<span class="event-location">(.*)</span>'          #匹配地点的正则
Time = r'<time datetime=".*">(.*)<span class="say-no-more">'    #匹配时间的正则
Year = r'<span class="say-no-more">(.*)</span></time>'          #匹配年份

#处理html内的信息并输出正则到的内容

def delInf(URL):
    datalist = []
    strInf = request.urlopen(URL).read().decode('utf-8')  #整个网页的信息采用utf-8的编码格式来
    name = re.findall(Name, strInf)       #正则匹配内容，返回所有匹配到的项，返回的是一个列表形式
    location = re.findall(Location, strInf)
    time = re.findall(Time, strInf)
    year = re.findall(Year, strInf)
    for index in range(0, len(name)):
        print('会议名称:'+name[index])
        print('会议地点:' + location[index])
        print('会议时间:' + time[index].replace('&ndash;','-'))  #由于特殊字符的存在，这里要替换一下
        print('会议年份:' + year[index]+'\n')

```

## 常用第三方模块

所有的第三方模块都会在[PyPI - the Python Package Index](https://pypi.org/)上注册

### Pillow

PIL：Python Imaging Library 图像处理标准库

安装`$ pip install pillow`

图像缩放、切片、旋转、滤镜、输出文字、调色板等

```py
from PIL import Image
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

######## 
from PIL import Image, ImageFilter
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
```

```py
# 绘图方法
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('arial.ttf', 36) # font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
```

https://pillow.readthedocs.io/en/stable/

### requests

处理URL资源特别方便比内置的urllib模块；`$ pip install requests`

```py
import requests
#### 简单请求
r = requests.get('https://www.douban.com/') # 豆瓣首页
r.status_code   # 200
r.text          # '<!DOCTYPE HTML>\n<html>\n<head>\n<meta name="description" content="提供图书、电影、音乐唱片的推荐、评论和...'

#### 带参数的URL
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r.url           # 'https://www.douban.com/search?q=python&cat=1001'
r.encoding      # 'utf-8'
r.content       ### 无论响应是文本还是二进制内容，都可用content获得bytes对象
# b'<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n...'

#### 特定类型响应
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json()
# {'query': {'count': 1, 'created': '2017-11-17T07:14:12Z', ...

#### dict作为headers参数
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r.text # '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n <title>豆瓣(手机版)</title>...'

#### POST请求
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON

# 上传文件需要更复杂的编码格式，requests把它简化成files参数
upload_files = {'file': open('report.xls', 'rb')}   # 务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
r = requests.post(url, files=upload_files)

#### 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

#### 获取响应头
r.headers
# {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
r.headers['Content-Type']
# 'text/html; charset=utf-8'
r.cookies['ts']  ### 获取指定的Cookie
# 'example_cookie_12345'

#### 请求中传入Cookie 
cs = {'token': '12345', 'status': 'working'}  # dict
r = requests.get(url, cookies=cs)

#### 指定超时
r = requests.get(url, timeout=2.5) # 2.5秒后超时
```

### chardet

检测编码，简单易用; `$ pip install chardet`
`chardet`支持检测的编码列表[Supported encodings](https://chardet.readthedocs.io/en/latest/supported-encodings.html)

```py
import chardet
chardet.detect(b'Hello World!')
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''} ### confidence:表示检测的概率是1.0（即100%）

data = '野火烧不尽，春风吹又生'.encode('gbk')
chardet.detect(data)
# {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'} 
# GBK是GB2312的超集,检测正确的概率是74%

data = '野火烧不尽，春风吹又生'.encode('utf-8')
chardet.detect(data)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

data = '最新の主要ニュース'.encode('euc-jp')
chardet.detect(data)
# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

# 获取到编码后，再转换为str
```

### psutil

用Python来编写脚本简化日常的运维工作是Python的一个重要用途
。在Linux下，有许多系统命令监控系统运行的状态，如`ps`，`top`，`free`等等。要获取这些系统信息，Python可以通过`subprocess`模块调用并获取结果。但这样做显得很麻烦，要写很多解析代码。

psutil = process and system utilities;支持Linux／UNIX／OSX／Windows等  `$ pip install psutil`

```py
import psutil
##### 获取CPU信息
psutil.cpu_count() # CPU逻辑数量
# 4
psutil.cpu_count(logical=False) # CPU物理核心
# 4  ## 2说明是双核超线程, 4则是4核非超线程
psutil.cpu_times()  # 统计CPU的用户／系统／空闲时间
# scputimes(user=54260.28125, system=37183.68750000006, idle=324648.74999999994, interrupt=1552.8125, dpc=566.28125)

# 类似top命令的CPU使用率，每秒刷新一次，累计10次
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))
# [7.7, 1.6, 1.6, 1.6]
# [13.6, 7.8, 7.8, 9.4]
# [20.0, 6.2, 4.7, 4.7]
# [17.6, 9.4, 6.2, 4.7]
# [13.6, 4.7, 7.8, 9.2]
# [10.9, 14.1, 25.0, 29.7]
# [9.2, 9.4, 20.3, 37.5]
# [12.3, 17.2, 16.9, 42.2]
# [15.2, 12.5, 29.7, 32.3]
# [21.9, 15.6, 18.8, 32.8]

##### 获取内存信息
psutil.virtual_memory()   # 获取物理内存信息
# svmem(total=17008623616, available=7462981632, percent=56.1, used=9545641984, free=7462981632)
psutil.swap_memory()      # 获取交换内存信息
# sswap(total=15032385536, used=10140028928, free=4892356608, percent=67.5, sin=0, sout=0)

##### 获取磁盘信息
psutil.disk_partitions()    # 磁盘分区信息
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]
### journaled表示支持日志
psutil.disk_usage('/')      # 磁盘使用情况
# sdiskusage(total=240439554048, used=177875111936, free=62564442112, percent=74.0)
psutil.disk_io_counters()   # 磁盘IO
# sdiskio(read_count=1392793, write_count=2740240, read_bytes=42224538624, write_bytes=47443334144, read_time=11516, write_time=7485)

##### 获取网络信息
psutil.net_io_counters()    # 获取网络读写字节／包的个数
# snetio(bytes_sent=205000569, bytes_recv=1481447872, packets_sent=1234474, packets_recv=2495996, errin=0, errout=0, dropin=0, dropout=8)

psutil.net_if_addrs()       # 获取网络接口信息
# {
#  '以太网': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='54-E1-AD-00-68-59', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.154.98', netmask='255.255.0.0', ...)], 
# 'WLAN': [...],
# '蓝牙网络连接': [...]
# }

psutil.net_if_stats()       # 获取网络接口状态
# {
#   '蓝牙网络连接': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=3, mtu=1500), 
#   '以太网': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),  
#   'WLAN': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=300, mtu=1500)
# }

psutil.net_connections()    # 获取当前网络连接信息
# [
#   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='0.0.0.0', port=3389), raddr=(), status='NONE', pid=1700), 
#   sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='::', port=2107), raddr=(), status='LISTEN', pid=5848),
#   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=1801), raddr=(), status='LISTEN', pid=5848), 
#   sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=<SocketKind.SOCK_STREAM: 1>, ..., pid=5848), 
#   sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=<SocketKind.SOCK_STREAM: 1>, ..., pid=2036), 
#   ...
#   sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=445), raddr=(), status='LISTEN', pid=4)
# ]

##### 获取进程信息
psutil.pids() # 所有进程ID
# [0, 4, 96, 420, 444, 588, ..., 24184, 25480, 25684, 26400, 26560]
p = psutil.Process(23284) # 获取指定进程ID=23284，其实就是当前Python交互环境
p.name() # 进程名称
# 'python.exe'
p.exe() # 进程exe路径
# 'D:\\Programs\\Python\\Python38\\python.exe'
p.cwd() # 进程工作目录
# 'C:\\Users\\Steven\\Downloads'
p.cmdline() # 进程启动的命令行
# ['python']
p.ppid() # 父进程ID
# 23416
p.parent() 
# psutil.Process(pid=23416, name='cmd.exe', status='running', started='2022-07-25 13:44:33')
p.children() # 子进程列表
# []
p.status() # 进程状态
# 'running'
p.username() # 进程用户名
# 'STEVEN\\Steven'
p.create_time()
# 1658822773.268577
p.terminal() # 进程终端
## '/dev/ttys002'  AttributeError: 'Process' object has no attribute 'terminal'
p.cpu_times() # 进程使用的CPU时间
# pcputimes(user=0.109375, system=0.078125, children_user=0.0, children_system=0.0)
p.memory_info() # 进程使用的内存
# pmem(rss=13484032, vms=8159232, num_page_faults=6685, peak_wset=14077952, wset=13484032, peak_paged_pool=179664, paged_pool=179264, peak_nonpaged_pool=17280, nonpaged_pool=13760, pagefile=8159232, peak_pagefile=8638464, private=8159232)
p.open_files() # 进程打开的文件
# [
#   popenfile(path='C:\\Program Files\\WindowsApps\\Microsoft.LanguageExperiencePacken-US_17134.66.103.0_neutral__8wekyb3d8bbwe\\Windows\\System32\\en-US\\KernelBase.dll.mui', fd=-1),
#   popenfile(path='C:\\Program Files\\WindowsApps\\Microsoft.LanguageExperiencePacken-US_17134.66.103.0_neutral__8wekyb3d8bbwe\\Windows\\System32\\en-US\\kernel32.dll.mui', fd=-1)]
p.connections() # 进程相关网络连接
# []
p.num_threads() # 进程的线程数量
# 3
p.threads() # 所有线程信息
# [pthread(id=212, user_time=0.109375, system_time=0.25), pthread(id=21100, user_time=0.0, system_time=0.0), pthread(id=3352, user_time=0.0, system_time=0.0)]
p.environ() # 进程环境变量
# {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Steven\\AppData\\Roaming', 'CLASSPATH': '.;D:\\Program Files\\Java\\jdk1.8.0_301\\lib;D:\\Program Files\\Java\\jdk1.8.0_301\\lib\\tools.jar', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', ...'C:\\windows'}
p.terminate() # 结束进程
# Terminated: 15 <-- 自己把自己结束了
```

`psutil`还提供了一个`test()`函数，可以模拟出`ps`命令的效果：

```bash
$ sudo python3
Password: ******
Python 3.6.3 ... on darwin
Type "help", ... for more information.
>>> import psutil
>>> psutil.test()
USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
root           0 24.0 74270628 2016380 ?             Nov18   40:51  kernel_task
root           1  0.1 2494140    9484 ?             Nov18   01:39  launchd
root          44  0.4 2519872   36404 ?             Nov18   02:02  UserEventAgent
root          45    ? 2474032    1516 ?             Nov18   00:14  syslogd
root          47  0.1 2504768    8912 ?             Nov18   00:03  kextd
root          48  0.1 2505544    4720 ?             Nov18   00:19  fseventsd
_appleeven    52  0.1 2499748    5024 ?             Nov18   00:00  appleeventsd
root          53  0.1 2500592    6132 ?             Nov18   00:02  configd
...
```

```py
import psutil
psutil.Process() # 获取当前运行的进程相关信息
# psutil.Process(pid=23904, name='python.exe', status='running', started='17:26:47')
psutil.cpu_freq()  # 返回CPU频率
# scpufreq(current=2496.0, min=0.0, max=2496.0)
psutil.cpu_percent()  # 返回当前系统CPU利用率(float类型)
# 20.0
psutil.cpu_stats()  # 返回CPU统计数据
# scpustats(ctx_switches=1838585427, interrupts=2765403574, soft_interrupts=0, syscalls=2517607330)
psutil.cpu_times_percent() # 对于每个特定的CPU时间提供利用率，由cpu_times()返回。
# scputimes(user=11.3, system=8.1, idle=79.4, interrupt=0.8, dpc=0.4)
psutil.boot_time()  # 返回从1970以来以秒表示的系统启动时间
# 1658718836.6645727
psutil.users()   # 返回当前连接在系统上的用户列表
# [suser(name='Steven', terminal=None, host=None, started=1658718855.899352, pid=None)]
```

[pstuil](https://github.com/giampaolo/psutil)

## `venv`

[`venv`](https://docs.python.org/zh-cn/3/tutorial/venv.html)用来为一个应用创建一套“隔离”的Python运行环境
`python3 -m venv <目录>`创建
Linux/Mac用`source activate`，Windows用`activate.bat`激活该venv环境
使用`deactivate`退出
删除:退出后把整个目录proj101env删掉就行

[virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html)
> 创建虚拟环境的时候 `virtualenv --no-site-packages venv`，如果virtualenv版本大于20，加上`--no-site-packages`时候会报错，默认版本大于20是不用加的

```bash
# 创建目录
~$ mkdir proj101env
~$ cd proj101env/
proj101env$
# 创建一个独立的Python运行环境
proj101env$ python3 -m venv .
proj101env$ ls
bin  include  lib  pyvenv.cfg
# 观察bin目录的内容，里面有python3、pip3等可执行文件，实际上是链接到Python系统目录的软链接
# 进入bin目录，激活venv环境
proj101env$ cd bin
bin$ source activate
(proj101env) bin$
(proj101env) bin$ pip3 install jinja2
...
Successfully installed jinja2-xxx
(proj101env) bin$ python3
>>> import jinja2
>>> exit()
# 用pip安装的包都被安装到proj101env这个环境下，具体目录是proj101env/lib/python3.x/site-packages
# 退出当前的proj101env环境，使用deactivate
(proj101env) bin$ deactivate
bin$
```

## 图形界面

支持多种图形界面的第三方库:Tk、xWidgets、Qt、GTK等

Tkinter: 自带库支持TK; Tkinter封装了访问Tk的接口;Tk是一个图形库，支持多个操作系统，使用Tcl语言开发;Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

在GUI中，每个Button、Label、输入框等，都是Widget。Frame可容纳其他Widget的Widget，所有Widget组合起来是一棵树。
`pack()`方法把Widget加入到父容器中，并实现布局。`pack()`是最简单的布局，`grid()`可以实现更复杂的布局。
在`createWidgets()`方法中，创建`Label`和`Button`，当`Button`被点击时，触发`self.quit()`使程序退出

```py
# 1.导入Tkinter包的所有内容
from tkinter import *

# 2. 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

# 3. 实例化Application，启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
```

GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理

```py
# 输入文本
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()    
```

```py
from tkinter import *
import time

LOG_LINE_NUM = 0

class Application(object):
    def __init__(self, window):
        self.mainWin = window
    def windowBox(self):
        #标题和标签
        self.mainWin.title("ASCLL码转换器")
        self.mainWin.geometry('605x590+550+150')  # width x height + x + y 宽和高 以及屏幕坐标
        self.LeftWindowLabel = Label(self.mainWin, text="待处理数据", padx=100)
        self.LeftWindowLabel.grid(column=0, row=0) 
        self.RightWindowLabel = Label(self.mainWin,text="数据转换结果")
        self.RightWindowLabel.grid(column=4,row=0)
        self.LeftLogLabel = Label(self.mainWin,text="数据日志")
        self.LeftLogLabel.grid(column=0,row=4)
        self.RightLogLabel = Label(self.mainWin,text="处理日志")
        self.RightLogLabel.grid(column=4,row=4)
        #文本框
        self.LeftText = Text(self.mainWin,width=35,height=30)
        self.LeftText.grid(column=0,row=1,rowspan=2,columnspan=2)
        self.RightText = Text(self.mainWin,width=35,height=30)
        self.RightText.grid(column=4,row=1,rowspan=2,columnspan=2)
        self.LeftLogText = Text(self.mainWin,width=35,height=10)
        self.LeftLogText.grid(column=0,row=7,rowspan=2,columnspan=2)
        self.RightLogText = Text(self.mainWin,width=35,height=10)
        self.RightLogText.grid(column=4,row=7,rowspan=2,columnspan=2)
        #按钮
        self.TransButton = Button(self.mainWin, text="开始转换", command=self.str_to_ascll, width=10)
        self.TransButton.grid(column=2, row=2)
    def str_to_ascll(self):
        src= self.LeftText.get(1.0, END)
        if src:
            try:
                Lsrc = [x.strip() for x in src if x.strip() != '']
                Osrc = [ord(x) for x in Lsrc ]
                Tsrc = "".join("%s" %x for x in Osrc)
                self.RightText.delete(1.0, END)
                self.RightText.insert(1.0, Tsrc)
                self.Log_Show("转换成功")
            except:
                self.RightText.delete(1.0,END)
                self.RightText.insert(1.0,"字符转换失败")
        else:
            self.Log_Show("转换失败")

    def get_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def Log_Show(self, log_message):
        global LOG_LINE_NUM
        current_time = self.get_time()
        logmessage_in = str(current_time) +" " + str(log_message) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.LeftLogText.insert(END, logmessage_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.LeftLogText.delete(1.0,2.0)
            self.LeftLogText.insert(END, logmessage_in)

def First_GUI():
    window = Tk()
    app = Application(window)
    app.windowBox()
    window.mainloop()

First_GUI()
```

![str_to_ascll_app](./images/base/strToAscll.png)

### 海龟绘图

1966,[LOGO语言](https://baike.baidu.com/item/logo/4689862)专门给儿童学习编程;通过编程指挥一个小海龟（turtle）在屏幕上绘图
[turtle库](https://docs.python.org/3.3/library/turtle.html#turtle-methods)
`width()`:设置笔刷宽度
`pencolor()`:设置颜色
`done()`:让窗口进入消息循环，等待被关闭
绘制出一个长方形

```py
# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(4)
# 前进:
forward(200)
# 右转90度:
right(90)
# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
```

```py
# 画五个五角星
from turtle import * 
def drawStar(x, y):
    pu()            # penup() Pull the pen up – no drawing when moving. 之后移动的时候就不会画
    goto(x, y)
    pd()            # pendown()     # 移动的时候就会画图
    seth(0)         # # set heading: 0 setheading
    for i in range(5):
        fd(40)      # forward
        rt(144)     # right

for x in range(0, 250, 50):  # range(0, 250, 50) ==> 0 50 100 150 200
    drawStar(x , 0)

done()
```

```py
# 使用递归绘制分型树
from turtle import *

# 设置色彩模式是RGB:
colormode(255)
lt(90)          # left 画笔方向 向上，默认向右的

lv = 14
l = 120
s = 45

width(lv)      # pensize() 笔刷大小

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)   # 笔刷颜色

penup()             # 笔刷抬起
bk(l)               # back 向后退 120
pendown()           # 笔刷放下
fd(l)               # 前进 120， 画完了树干

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)  # 画笔旋转 45
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s) # 右转 90
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)  # 左转 45 

    # restore the previous pen width
    width(w)

speed("fastest")  # 画图速度 
draw_tree(l, 4)
done()
```

## 网络编程

网络通信是两台计算机上的两个进程之间的通信;在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。

### TCP/IP简介

互联网协议簇（Internet Protocol Suite）通用协议标准;互联网上每个计算机的唯一标识就是IP地址;P地址对应的实际上是计算机的网络接口，通常是网卡
IP地址32位整数（称为IPv4）;IPv6地址128位整数
TCP协议则是建立在IP协议之上;建立可靠连接，保证数据包按顺序到达;浏览器的HTTP协议、发送邮件的SMTP协议都是建立在TCP协议基础上
TCP报文包含要传输的数据，源IP地址和目标IP地址，源端口和目标端口

### TCP编程

Socket表示“打开了一个网络链接”，打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可

客户端:创建TCP连接时,主动发起连接的叫客户端，被动响应连接的叫服务器
TCP连接创建的是双向通道,双方都可以同时给对方发数据,谁先发谁后发,根据具体的协议来决定;HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端

`AF_INET`指定使用IPv4协议，如果要用更先进的IPv6，就指定为`AF_INET6`;`SOCK_STREAM`指定使用面向流的TCP协议
`80`端口是Web服务的标准端口;SMTP服务`25`端口，FTP服务`21`;端口号小于1024的是Internet标准服务的端口，大于1024可以任意使用
`recv(max)`:一次最多接收指定的字节数

```py
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80)) # tuple，包含地址和端口号
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 60
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()

# 数据包括HTTP头和网页本身
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
```

```py
# 获取的HTML文件，把资源地址加上协议名，例如：//url..改成[https://url..](https://url..)就能直接打开了
import socket
import ssl

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn', 443))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
d = s.recv(1024)
while d:
    buffer.append(d)
    d = s.recv(1024)
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    f.write(html)
```

服务器:
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了
服务器要能够区分一个Socket连接是和哪个客户端绑定的.一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket

服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可用`0.0.0.0`绑定到所有的网络地址，还可用`127.0.0.1`绑定到本机地址。`127.0.0.1`是特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，外部的计算机无法连接进来。

```py
# echo_server.py
import threading
import time
import socket
# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址和端口号
s.bind(('127.0.0.1', 9999))
# 开始监听端口,参数指定等待连接的最大数量
s.listen(5)
print('Waitting for connection ...')
# 永久循环来接受来自客户端的连接;accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# 每个连接都必须创建新线程（或进程）来处理，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# echo_client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

## UDP编程

UDP面向无连接的协议；不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
传输数据不可靠；优点是比TCP速度快

`SOCK_DGRAM`指定Socket的类型是UDP。绑定端口和TCP一样，但不需要调用`listen()`，而是直接接收来自任何客户端的数据
`recvfrom()`返回数据和客户端的地址与端口，服务器收到数据后，直接调用`sendto()`就可以把数据用UDP发给客户端

```py
# udp_server.py
import socket
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999 ...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

# udp_client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(data, ('127.0.0.1', 9999))  # 不需要调用connect()，直接通过sendto()给服务器发数据
    print(s.recv(1024).decode('utf-8'))

s.close() 
```

## 电子邮件

电子邮件软件:MUA：Mail User Agent——邮件用户代理
**MTA**：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等
邮件的最终目的地**MDA**：Mail Delivery Agent——邮件投递代理
要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上
`发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人`
编写程序来发送和接收邮件:1 编写MUA把邮件发到MTA；2 编写MUA从MDA上收邮件

发邮件时，MUA和MTA使用SMTP协议：Simple Mail Transfer Protocol，MTA到另一个MTA也用SMTP协议。
收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。
**目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录**

### SMTP发送邮件

发送纯文本邮件、HTML邮件以及带附件的邮件
Python对SMTP支持有`smtplib`和`email`两个模块，`email`负责构造邮件，`smtplib`负责发送邮件

构造`MIMEText`对象，第一个参数就是邮件正文，第二个参数是MIME的subtype，`'plain'`表示纯文本，最终的MIME就是`'text/plain'`，最后一定要用`utf-8`编码保证多语言兼容性

```py
# 构造最简单的纯文本邮件
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python ...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)                # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendemail(from_addr, [to_addr], msg.as_string())  # 一次发给多个人，所以传入一个list
server.quit()
```

上述代码问题：

1. 邮件没有主题
2. 收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>
3. 明明收到了邮件，却提示不在收件人中

因为邮件主题、如何显示发件人、收件人等信息不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中，所以必须把`From`、`To`和`Subject`添加到`MIMEText`中，才是一封完整的邮件

```py
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# 文本邮件
msg = MIMEText('hello, send by Python ...', 'plain', 'utf-8') 
# html 邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本
# From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <xxxxxx@163.com>
# To: =?utf-8?b?566h55CG5ZGY?= <xxxxxx@qq.com>
# Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=
```

很多邮件服务商在显示邮件时，会把收件人名字自动替换为用户注册的名字，其他收件人名字不受影响

#### 发送附件

附件邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可构造一个`MIMEMultipart`对象代表邮件本身，然后往里面加上一个`MIMEText`作为邮件正文，再继续往里面加上表示附件的`MIMEBase`对象即可

```py
# ...
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/michael/Downloads/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
# ...
```

#### 发送图片

要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用`src="cid:0"`就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的`cid:x`即可。

```py
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
```

#### 同时支持HTML和Plain格式

发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，可自动降级查看纯文本邮件

```py
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...
```

#### 加密SMTP

Gmail，提供的SMTP服务必须要加密传输;Gmail的SMTP端口是587

```py
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()      # 创建了安全连接
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...
```

构造一个邮件对象就是一个`Messag`对象，如果构造一个`MIMEText`对象，表示一个文本邮件对象，如果构造一个`MIMEImage`对象，表示一个作为附件的图片，要把多个对象组合起来，就用`MIMEMultipart`对象，而`MIMEBase`可表示任何对象。继承关系如下：

```txt
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
```

[email.mime文档](https://docs.python.org/3/library/email.mime.html)

### POP3收取邮件

收取邮件编写**MUA**作为客户端，从**MDA**把邮件获取到用户的电脑或者手机上
需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象

收取邮件分两步：
1：用`poplib`把邮件的原始文本下载到本地；
2：用`email`解析原始文本，还原为邮件对象。

```py
##### 通过POP3下载邮件
import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3(pop3_server) #  poplib.POP3_SSL(pop3_server,port=995) 
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)  # 要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()

##### 解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

msg = Parser().parsestr(msg_content)
# 递归地打印出Message对象的层次结构
# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 邮件的Subject或Email中包含的名字都是经过编码后的str，要正常显示，就必须decode    
def decode_str(s):
    value, charset = decode_header(s)[0]  # decode_header()返回一个list，像Cc、Bcc这样的可能包含多个邮件地址，解析出来的会有多个元素
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

print_info(msg)
# +OK Welcome to coremail Mail Pop3 Server (163coms[...])
# Messages: 126. Size: 27228317
# 
# From: Test <xxxxxx@qq.com>
# To: Python爱好者 <xxxxxx@163.com>
# Subject: 用POP3收取邮件
# part 0
# --------------------
#   part 0
#   --------------------
#     Text: Python可以使用POP3收取邮件……...
#   part 1
#   --------------------
#     Text: Python可以<a href="...">使用POP3</a>收取邮件……...
# part 1
# --------------------
#   Attachment: application/octet-stream
```

## 访问数据库

数据库类别
付费商用数据库:Oracle，典型的高富帅；SQL Server，微软自家产品，Windows定制专款；DB2，IBM的产品，听起来挺高端；Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。
免费开源数据库:MySQL，大家都在用，一般错不了；PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；sqlite，嵌入式数据库，适合桌面和移动应用。

### 使用SQLite

SQLite是一种嵌入式数据库，数据库就是一个文件。SQLite本身是C写的，体积很小，经常被集成到各种应用程序中，在iOS和Android的App中可集成。
不能承受高并发访问，适合桌面和移动应用
Python内置SQLite3
数据库连接称为`Connection`;通过`Cursor`执行SQL语句,然后，获得执行结果
Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可

```py
# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# <sqlite3.Cursor object at 0x000001FA4504D9D0>
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# <sqlite3.Cursor object at 0x000001FA4504D9D0>
# 通过rowcount获得插入的行数:
cursor.rowcount         # 执行insert，update，delete语句, 由rowcount返回影响的行数
# 1
# 提交事务:
conn.commit()
# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()

##### 查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', ('1',))
# <sqlite3.Cursor object at 0x000001FA4504DDC0>
# 获得查询结果集:
values = cursor.fetchall()
values
# [('1', 'Michael')]
cursor.close()
conn.close()
```

使用`Cursor`对象执行`insert`，`update`，`delete`语句，由`rowcount`返回影响的行数。
使用`Cursor`对象执行`select`语句时，通过`fetchall()`可以拿到结果集。结果集是一个`list`，每个元素都是一个`tuple`，对应一行记录。
如果SQL语句带有参数，那么需要把参数按照位置传递给`execute()`方法，有几个`?`占位符就必须对应几个参数，例如：
`cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))`

```py
# -*- coding: utf-8 -*-
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name, score from user where score>=? and score<=? order by score', (low, high))
    data = cursor.fetchall()
    # print(data)   
    cursor.close()
    conn.close()
    L_user = [user[0] for user in data]         # 将数据格式化为判断所需的格式并返回
    return L_user

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
```

### 使用MySQL

MySQL是Web世界中使用最广泛的数据库服务器;最常用引擎是支持数据库事务的InnoDB

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。`/etc/my.cnf`或者`/etc/mysql/my.cnf`：

```conf
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
```

```bash
# 重启MySQL后，可以通过MySQL的客户端命令行检查编码
$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor...
...

mysql> show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | utf8                                                   |
| character_set_connection | utf8                                                   |
| character_set_database   | utf8                                                   |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8                                                   |
| character_set_server     | utf8                                                   |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/mysql-5.1.65-osx10.6-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+
8 rows in set (0.00 sec)

# 如果MySQL的版本≥5.5.3，可把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符
```

MySQL官方提供了mysql-connector-python驱动，安装的时候需要给pip命令加上参数`--allow-external`：
`$ pip install mysql-connector-python`
`$ pip install mysql-connector`

```py
# 导入MySQL驱动:
import mysql.connector
conn = mysql.connector.connect(host='192.168.31.10',user='root', password='123456', database='test')
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount     # 1
# 提交事务:
conn.commit()
cursor.close()      # True

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values              # [('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()      # True
conn.close()
```

1. 执行`INSERT`等操作后要调用`commit()`提交事务
2. MySQL的SQL占位符是`%s`

### 使用SQLAlchemy

ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
`$ pip install sqlalchemy`

`create_engine()`初始化数据库连接,`'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'`

```py
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine) # DBSession对象可视为当前数据库连接

### 向数据库表中添加一行记录
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

### 
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))      # type: <class '__main__.User'>
print('name:', user.name)       # name: Bob
# 关闭Session:
session.close()
```

关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能

```py
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list
```

https://www.cnblogs.com/minseo/p/15305003.html
hive python:https://www.cdata.com/kb/tech/hive-python-sqlalchemy.rst

## Web开发  ※

Web开发几个阶段

1. 静态Web页面：由文本编辑器直接编辑并生成静态的HTML页面，如果要修改Web页面的内容，就需要再次编辑HTML源文件，早期的互联网Web页面就是静态的；
2. CGI：由于静态Web页面无法与用户交互，比如用户填写了一个注册表单，静态Web页面就无法处理。要处理用户发送的动态数据，出现了Common Gateway Interface，简称CGI，用C/C++编写。
3. ASP/JSP/PHP：由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。
4. MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controller的模式，来简化Web开发。ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。

### HTTP协议简介

`Request Headers`
`GET / HTTP/1.1`；`GET`表示读取请求，将从服务器获得网页数据，`/`表示URL的路径，URL总是以`/`开头，`/`就表示首页，`HTTP/1.1`采用HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度
从第二行开始，每一行都类似于`Xxx: abcdefg`：
`Host: www.sina.com.cn`：请求的域名

`Response Headers`

HTTP请求:
一个HTTP请求只处理一个资源

HTTP格式:

HTTP GET请求的格式,每个Header一行一个，换行符是`\r\n`

```txt
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
```

HTTP POST请求的格式,当遇到连续两个`\r\n`时，Header部分结束，后面数据全部是Body;Body数据类型由`Content-Type`头来确定

```txt
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```

《HTTP: The Definitive Guide》 《HTTP权威指南》
http://www.w3schools.com/     http://www.w3school.com.cn/

### WSGI接口

接受HTTP请求、解析HTTP请求、发送HTTP响应；
WSGI：Web Server Gateway Interface
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求

```py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

上面的`application()`函数符合WSGI标准的一个HTTP处理函数，接收两个参数：

* `environ`：包含所有HTTP请求信息的`dict`对象
* `start_response`：发送HTTP响应的函数,只能调用一次;两个参数，一个HTTP响应码，一个是一组`list`表示的HTTP Header，每个Header用一个包含两个`str`的`tuple`表示

#### 运行WSGI服务

```py
# hello.py
# WSGIRequestHandler的get_environ中有如下代码
# env['PATH_INFO'] = urllib.parse.unquote_to_bytes(path).decode('iso-8859-1')
def application(environ, start_response):
    print(environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8'))
    start_response('200 OK',[('Content-Type','text/html; charset=utf-8')])
    body = '<h1>Hello,%s!</h1>' % ((environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8'))[1:] or 'web')
    # start_response('200 OK', [('Content-Type', 'text/html')])
    # body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# server.py 负责启动WSGI服务器
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
```

简化Web开发需要在WSGI之上再抽象出Web框架

### 使用Web框架

[Flask](https://flask.palletsprojects.com/)编写Web App比WSGI接口简单
常见的Python Web框架有：
[Django](https://www.djangoproject.com/)：全能型Web框架；
[web.py](https://webpy.org/)：一个小巧的Web框架；
[Bottle](http://bottlepy.org/docs/dev/)：和Flask类似的Web框架；
[Tornado](https://www.tornadoweb.org/en/stable/)：Facebook的开源异步Web框架。

`pip install flask`;写一个`app.py`，处理3个URL，分别是：

* `GET /`：首页，返回`Home`
* `GET /signin`：登录页，显示登录表单
* `POST /signin`：处理登录表单，显示登录结果

Flask通过Python的装饰器在内部自动地把URL和函数给关联起来

```py
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home<h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>username:<input name="username"></p>
              <p>password:<input name="password" type="password">
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=["POST"])
def signin():
    # 需要从request对象读取表单内容：
    if request.form["username"] == 'admin' and request.form["password"] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
```

### 使用模板

不懂前端的Python工程师不是好的产品经理

![template_html_py](./images/base/py_template_html.png)

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
包含变量`{{ name }}`的模板就是V:View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
MVC中的Model在哪？Model是用来传给View的，View在替换变量时，就可从Model中取出相应的数据
Model就是一个`dict`:`{ 'name': 'Michael' }`

Flask通过`render_template()`函数来实现模板渲染。Flask默认支持的模板是`jinja2`，`$ pip install jinja2`

在Jinja2模板中，用`{{ name }}`表示一个需要替换的变量。需要循环、条件判断等指令语句，用`{% ... %}`表示指令。
比如循环输出页码：

```html
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
```

常见的模板有：
[Mako](https://www.makotemplates.org/)：用`<% ... %>`和`${xxx}`的一个模板；
[Cheetah](https://cheetahtemplate.org/)：用`<% ... %>`和`${xxx}`的一个模板；
[Django](https://www.djangoproject.com/)：Django是一站式框架，内置一个用`{% ... %}`和`{{ xxx }}`的模板。

```py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=["POST"])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()  # app.run(debug=True)开启debug模式会自动更新
```

**一定要把模板放到正确的`templates`目录下，`templates`和`app.py`在同级目录下**

```html
<!-- home.html -->
<html>
<head>
  <title>Home</title>
</head>
<body>
  <h1 style="font-style:italic">Home</h1>
</body>
</html>

<!--form.html--->
<html>
<head>
    <title>Please Sign in</title>
</head>
<body>
    {% if message %}
    <p style="color:red">{{ message }}</p>
    {% endif %}
    <form action="/signin" method="post">
        <legend>Please Sign in:</legend>
        <p>username:<input name="username" placeholder="Username" value="{{ username }}"></p>
        <p>password:<input name="password" type="password" palceholder="Password"></p>
        <p><button type="submit">Sign In</button></p>
    </form>
</body>
</html>

<!-- signin-ok.html -->
<html>
<head>
    <title>Welcome, {{ username }}</title>
</head>
<body>
    <p>Welcome, {{ username }}!</p>
</body>
</html>
```

```py
# 小技巧
empty_info={user_address=="":"请输入住址",email=="":"请输入邮箱地址",telphone=="":"请输入手机号",phone_re.match(telphone)==False:"手机格式不正确",\
            email_re.match(email)==False:"邮箱格式不正确",confirm_password!=password:"两次密码不一样",\
            confirm_password=="":"请输入确认密码",password=="":"请输入密码",len(password)<8 or password.isalnum()==False:"密码不能小于8位，且必须是字母、数字组合",\
            len(username)<6 or username.isalnum()==False:"用户名不能小于6位，且必须是字母、数字组合",username=="":"请输入用户名"}.get(1, "correct")

# 写法简洁,get了.dict里以各种各样的错误判断为键,然后用对应的错误信息提示作为值. 只要能拿到一个key为1(True)的值,就说明密码判断错误,get()返回的就是对应的错误信息提示.没有拿到1,也就是里面所有的判断都通过,correct
```

## 异步IO

系统切换线程的开销也很大;解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配;
多线程和多进程只是一种方法,另一种解决IO问题的方法是异步IO(当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理)

在异步IO模型下，一个线程就可以同时处理多个IO请求

### 协程

协程，又称微线程，纤程。英文名Coroutine。在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断;一个线程执行
协程执行效率极高;不需要多线程的锁机制,在协程中控制共享资源不加锁，只需要判断状态就好
多核CPU(多进程+协程)

Python通过`generator`支持协程,`for`,`next()`,`yield`
Python的`yield`可返回一个值，还可接收调用者发出的参数

生产者生产消息后，直接通过`yield`跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产

```py
def consumer():
    r = ''      # 先行定义一个后来被引用的变量，防止无定义报错
    while True:
        # 要理解两个知识点，赋值语句先计算= 右边，由于右边是 yield 语句，所以yield语句执行完以后，进入暂停，而赋值语句在下一次启动生成器的时候首先被执行
        n = yield r         # 这里的yield既有接受send方法传参的作用，也有向produce传参的作用
        if not n:           # 用于第一次跳过空变量
            return
        print('[CONSUMER] consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)        # 用于启动生成器，程序规定如此，没有会报错
    n = 0
    while n < 5:
        n = n +1
        print('[PRODUCER] producing %s...' % n)
        r = c.send(n)   # 相当于带了参数的next(c)，同时也有接受consumer中yield传参的作用，可以用来打印消费者的状态
        print('[PRODUCER] Consumer return:%s' % r)
    c.close()

c = consumer()
produce(c)

# [PRODUCER] producing 1...
# [CONSUMER] consuming 1...
# [PRODUCER] Consumer return:200 OK
# [PRODUCER] producing 2...
# [CONSUMER] consuming 2...
# [PRODUCER] Consumer return:200 OK
# [PRODUCER] producing 3...
# [CONSUMER] consuming 3...
# [PRODUCER] Consumer return:200 OK
# [PRODUCER] producing 4...
# [CONSUMER] consuming 4...
# [PRODUCER] Consumer return:200 OK
# [PRODUCER] producing 5...
# [CONSUMER] consuming 5...
# [PRODUCER] Consumer return:200 OK
```

注意到`consumer`函数是一个`generator`，把一个`consumer`传入`produce`后：

1. 首先调用`c.send(None)`启动生成器；
2. 一旦生产了东西，通过`c.send(n)`切换到`consumer`执行；
3. `consumer`通过`yield`拿到消息，处理，又通过`yield`把结果传回；
4. `produce`拿到`consumer`处理的结果，继续生产下一条消息；
5. `produce`决定不生产了，通过`c.close()`关闭`consumer`，整个过程结束。

整个流程无锁，由一个线程执行，`produce`和`consumer`协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
Donald Knuth的一句话总结协程的特点:**“子程序就是协程的一种特例。”**

1、例子中的`c.send(None)`，其功能类似于`next(c)`，比如：

```py
def num():
    yield 1
    yield 2
    
c = num()
c.send(None)  # 1
c.send(None)  # 2
c.send(None) 
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     c.send(None)
# StopIteration
```

2、`n = yield r`，这条语句，要理解两个知识点，赋值语句先计算`=`右边，由于右边是`yield`语句，所以`yield`语句执行完以后，进入暂停，而赋值语句在下一次启动生成器的时候首先被执行；
3、`send`在接受`None`参数的情况下，等同于`next(generator)`的功能，但`send`同时也可接收其他参数，比如例子中的`c.send(n)`，要理解这种用法，看个例子：

```py
def num():
    a = yield 1
    while True:
        a = yield a
       
c = num()
c.send(None)    # 1
c.send(5)       # 5
c.send(100)     # 100
```

在上面的例子中，首先使用`c.send(None)`，返回生成器的第一个值，`a = yield 1` ，也就是`1`（但此时，并未执行赋值语句），
接着使用`c.send(5)`，再次启动生成器，并同时传入了一个参数`5`，再次启动生成的时候，从上次`yield`语句断掉的地方开始执行，即`a`的赋值语句，由于传入了一个参数`5`，所以`a`被赋值为`5`，接着程序进入`whlie`循环，当程序执行到`a = yield a`，同理，先返回生成器的值`5`，下次启动生成器的时候，再执行赋值语句，以此类推...
所以`c.send(n)`的用法就是"Python的`yield`不但可以返回一个值，它还可以接收调用者发出的参数"
**但注意，在一个生成器函数未启动之前，是不能传递值进去。在使用`c.send(n)`之前，必须先使用`c.send(None)`或者`next(c)`来返回生成器的第一个值。**
最后我们来看上文中的例子，梳理下执行过程：

```py
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```

1. 执行`c.send(None)`，启动生成器返回第一个值`n = yield r`，此时`r`为空，`n`还未赋值，然后生成器暂停，等待下一次启动。
2. 生成器返回空值后进入暂停，`produce(c)` 接着往下运行，进入`while`循环，此时`n`为`1`，所以打印:`[PRODUCER] Producing 1...`
3. `produce(c)`往下运行到`r = c.send(1)`，再次启动生成器，并传入了参数`1`，而生成器从上次`n`的赋值语句开始执行，`n`被赋值为`1`，`n`存在，`if`语句不执行，然后打印：`[CONSUMER] Consuming 1...` 接着`r`被赋值为`'200 OK'`，然后又进入循环，执行`n = yield r`，返回生成器的第二个值，`'200 OK'`，然后生成器进入暂停，等待下一次启动。
4. 生成器返回`'200 OK'`进入暂停后`，produce(c)`往下运行，进入`r`的赋值语句，`r`被赋值为`'200 OK'`，接着往下运行，打印：`[PRODUCER] Consumer return: 200 OK`
以此类推...

当`n`为`5`跳出循环后，使用`c.close()`结束生成器的生命周期，然后程序运行结束

### `asyncio`

`asyncio`是Python 3.4版本引入的标准库，内置对异步IO的支持
编程模型是一个消息循环;从`asyncio`模块中获取一个`EventLoop`的引用，把需要执行的协程扔到`EventLoop`中执行，就实现了异步IO

```py
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
```

`@asyncio.coroutine`把一个`generator`标记为`coroutine`类型，然后，把这个`coroutine`扔到`EventLoop`中执行
`hello()`会首先打印出`Hello world!`，然后，`yield from`语法可以方便地调用另一个`generator`。由于`asyncio.sleep()`也是一个`coroutine`，所以线程不会等待`asyncio.sleep()`，而是直接中断并执行下一个消息循环。当`asyncio.sleep()`返回时，线程就可以从`yield from`拿到返回值（此处是`None`），然后接着执行下一行语句。

把`asyncio.sleep(1)`看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行`EventLoop`中其他可以执行的`coroutine`了，因此可以实现并发执行。

```py
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# Hello world! (<_MainThread(MainThread, started 27692)>)
# Hello world! (<_MainThread(MainThread, started 27692)>)
# (暂停约1秒)
# Hello again! (<_MainThread(MainThread, started 27692)>)
# Hello again! (<_MainThread(MainThread, started 27692)>)
```

两个`coroutine`是由同一个线程并发执行的
把`asyncio.sleep()`换成真正的IO操作，则多个`coroutine`就可以由一个线程并发执行

```py
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 3个连接由一个线程通过coroutine并发完成
# wget www.sina.com.cn...
# wget www.sohu.com...
# wget www.163.com...
# (等待一段时间)
# (打印出sina的header)
# www.sina.com.cn header > HTTP/1.1 302 Found
# www.sina.com.cn header > Server: Tengine
# ...
# (打印出sohu的header)
# www.sohu.com header > HTTP/1.1 302 Found
# www.sohu.com header > Location: https://www.sohu.com/
# ...
# (打印出163的header)
# www.163.com header > HTTP/1.1 301 Moved Permanently
# www.163.com header > Date: Thu, 28 Jul 2022 07:57:55 GMT
# ...
```

小结：
`asyncio`提供了完善的异步IO支持
异步操作需要在`coroutine`中通过`yield from`完成
多个`coroutine`可以封装成一组Task然后并发执行

### `async/await`

新语法只能用在Python 3.5以及后续版本
新版本用`async`,`await` 关键词代替`@asyncio.coroutine`,`yield from`(https://realpython.com/async-io-python/)

```py
import threading
import asyncio

async def hello():
    print('hello world! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('hello again! (%s)' % threading.current_thread())

# loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

### `aiohttp`

`asyncio`实现了TCP、UDP、SSL等协议，`aiohttp`则是基于`asyncio`实现的HTTP框架
`pip install aiohttp`

注意`aiohttp`的初始化函数`init()`也是一个`coroutine`，`loop.create_server()`则利用`asyncio`创建TCP服务

```py
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!<h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/', index)
    app.router.add_route('GET','/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
```

```py
#  Django 风格
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

app = web.Application()
app.router.add_routes([web.get('/', index),
                       web.get('/hello/{name}', hello)])
web.run_app(app, host='localhost', port=8000)
```

```py
# Flask
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

@routes.get('/hello/{name}')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

app = web.Application()
app.add_routes(routes)
web.run_app(app, host='localhost', port=8000)
```

### 使用MicroPython

[MicroPython](https://micropython.org/),为了运行在单片机这样的性能有限的微控制器上，最小体积仅256K，运行时仅需16K内存
基于Python 3.4的语法标准,裁剪了大部分标准库，仅保留部分模块如`math`、`sys`的部分函数和类
此外，很多标准模块如`json`、`re`等在MicroPython中变成了以`u`开头的`ujson`、`ure`，表示针对MicroPython开发的标准库
运行在[pyboard](https://store.micropython.org/pyb-features)微控制器上
大量基于ARM的嵌入式系统，如[Arduino](https://www.arduino.cc/)
通过Python来非常方便地开发自动控制、机器人这样的应用

#### 搭建开发环境

硬件开发环境;树莓派+Arduino控制板;搭建机器人需要的零件比较复杂;乐高EV3机器人作为开发环境;乐高搭建非常容易且乐高的EV3控制器是一个完整的ARM系统

教育版建议买45544+45560套装，零售版就只有31313一种。没有MicroSD卡的可以顺手入一个MicroSD卡+读卡器，还可以再选购一个蓝牙游戏手柄

乐高官方提供了一个完整的EV3运行时镜像，该镜像内置了MicroPython，可以非常方便地运行Python程序,需要从乐高官网[下载镜像](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)到本地，然后写入到MicroSD卡.Windows和Mac系统可以使用[Etcher](https://www.balena.io/etcher/)写入镜像到MicroSD卡，也可以使用`dd`命令写入

插入SD卡后启动EV3控制器，等待1~2分钟，启动成功后，即可选择“Wireless and Networks”连接电脑：

![lego_EV3](./images/base/LGEV3_connections.jpg)

使用无线网连接需要额外的USB无线网卡，强烈推荐选择蓝牙连接，因为EV3内置了蓝牙模块。配对并连接成功后，可以在电脑上看到已连接的蓝牙设备EV3
可以直接使用SSH登录EV3，因为这个自带MicroPython的EV3镜像是一个裁剪后的Debian Linux系统。用命令`ssh robot@ev3dev.local`登录，密码`maker`：

```bash
$ ssh robot@ev3dev.local
Password: *****
Linux ev3dev 4.14.96-ev3dev-2.3.2-ev3 #1 PREEMPT Sun Jan 27 21:27:35 CST 2019 armv5tejl
             _____     _
   _____   _|___ /  __| | _____   __
  / _ \ \ / / |_ \ / _` |/ _ \ \ / /
 |  __/\ V / ___) | (_| |  __/\ V /
  \___| \_/ |____/ \__,_|\___| \_/

Debian stretch on LEGO MINDSTORMS EV3!
Last login: Mon Mar  4 18:05:04 2019 from f81e::a7:c54d:4e0b:3af7%bnep0
robot@ev3dev:~$ ls /usr/lib/micropython/
README           fcntl.mpy      mailbox.mpy          reprlib.mpy       trace.mpy
README.rst       ffilib.mpy     mailcap.mpy          runpy.mpy         traceback.mpy
__future__.mpy   fnmatch.mpy    mimetypes.mpy        sched.mpy         tty.mpy
_libc.mpy        formatter.mpy  multiprocessing.mpy  sdist_upip.mpy    types.mpy
_markupbase.mpy  fractions.mpy  nntplib.mpy          select.mpy        typing.mpy
abc.mpy          ftplib.mpy     numbers.mpy          selectors.mpy     uaiohttpclient.mpy
argparse.mpy     functools.mpy  operator.mpy         shelve.mpy        uasyncio
base64.mpy       getopt.mpy     optparse.mpy         shlex.mpy         uasyncio.mpy
binascii.mpy     getpass.mpy    os                   shutil.mpy        ucontextlib.mpy
binhex.mpy       gettext.mpy    pathlib.mpy          signal.mpy        ucurses
bisect.mpy       glob.mpy       pdb.mpy              smtplib.mpy       udnspkt.mpy
calendar.mpy     gzip.mpy       pickle.mpy           socket.mpy        umqtt
cgi.mpy          hashlib        pickletools.mpy      socketserver.mpy  unicodedata.mpy
cmd.mpy          heapq.mpy      pkg_resources.mpy    sqlite3.mpy       unittest.mpy
code.mpy         hmac.mpy       pkgutil.mpy          ssl.mpy           upip.mpy
codecs.mpy       html           platform.mpy         stat.mpy          upip_utarfile.mpy
codeop.mpy       http           poplib.mpy           statistics.mpy    upysh.mpy
collections      imaplib.mpy    posixpath.mpy        string.mpy        urequests.mpy
concurrent       imp.mpy        pprint.mpy           stringprep.mpy    urllib
contextlib.mpy   importlib.mpy  profile.mpy          struct.mpy        urllib.mpy
copy.mpy         inspect.mpy    pty.mpy              subprocess.mpy    utarfile.mpy
csv.mpy          io.mpy         pwd.mpy              sys.mpy           uu.mpy
curses           ipaddress.mpy  pyb.mpy              tarfile.mpy       uuid.mpy
datetime.mpy     itertools.mpy  pystone.mpy          telnetlib.mpy     venv.mpy
dbm.mpy          json           pystone_lowmem.mpy   tempfile.mpy      warnings.mpy
decimal.mpy      keyword.mpy    queue.mpy            test              weakref.mpy
difflib.mpy      linecache.mpy  quopri.mpy           textwrap.mpy      xmltok.mpy
email            locale.mpy     random.mpy           threading.mpy     zipfile.mpy
errno.mpy        logging.mpy    re.mpy               time.mpy          zlib.mpy
ev3dev2          machine        readline.mpy         timeit.mpy
```

在`/usr/lib/micropython/`目录下可看到系统自带Python库。MicroPython不直接运行`.py`文件，而是运行`.mpy`这个紧凑的二进制文件

开发EV3机器人程序,VSCode扩展,`lego`并安装`LEGO® MINDSTORMS® EV3 MicroPython`扩展

在VS Code左侧面板选择Lego图标，选择“Create a new project”：创建一个`hellorobot`的工程,EV3插件自动为我们创建了一个包含样板代码的`main.py`

```py
#!/usr/bin/env pybricks-micropython  ## 注释表示运行环境是MicroPython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()       # 控制EV3的扬声器发出一声“哔”的声音
```

可编写任意的Python源码文件，执行时注意程序入口永远是`main.py`

在VS Code 的`Exploer`中，找到`EV3DEV DEVICE BROWSER`，点击`ev3dev`，连接后图标显示为绿色

切换到Run面板，点击`RUN`运行，在`OUTPUT`面板中看到输出结果

VS Code是一个开发环境，电脑上并没有安装MicroPython，整个程序是通过蓝牙网络先传输到EV3主机，再执行，最后取回输出结果显示在VS Code中，因此，这是一个远程执行并允许调试的功能。`print()`函数可以输出到VS Code，主要作为调试使用，`brick.display.text()`则是输出到EV3的主机屏幕上

EV3的Python接口全部在`pybricks`包中，要查看完整的API，请在VS Code新建EV3工程时选择“Open user guide and examples”，即可在本地浏览器打开API文档。

### 控制小车

用EV3主机、大型伺服马达和超声波传感器搭建一个小车
![LGEV3_Car_components](./images/base/LGEV3_Car.jpg)
![LGEV3_car_instance](./images/base/LGEV3_car_instance.jpg)

```py
#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# 根据马达和传感器接入的位置初始化
motor = Motor(Port.B) # 接在B口
ultrasonic = UltrasonicSensor(Port.S4) # 接在4号口

brick.sound.beep()
brick.light(None)

# 设置初始速度0表示静止
speed = 0

# 通过传入1、-1和0分别表示加速、减速和停止：
def setSpeed(acc):
    global speed
    if acc < 0:
        speed = max(0, speed - 1)
    elif acc > 0:
        speed = min(3, speed + 1)
    else:
        speed = 0
    if speed > 0:
        motor.run(speed * 90) # 设置每秒转N个90度
    else:
        motor.stop()
    brick.light(colors[speed])

# 因为小车的初始速度为0，可设定响应右键加速，左键减速，中键停止，上键停止并退出，用一个无限循环实现功能
while True:
    if not any(brick.buttons()): # 没有按任何按键
        wait(10)
    else:
        if Button.LEFT in brick.buttons():
            setSpeed(-1)
        elif Button.RIGHT in brick.buttons():
            setSpeed(1)
        elif Button.CENTER in brick.buttons():
            setSpeed(0)
        elif Button.UP in brick.buttons():
            setSpeed(0)
            break
        wait(500)
    if ultrasonic.distance() < 200: # 检测到障碍物不足200毫米时 
        setSpeed(0)

brick.sound.beep()
```

因为EV3的控制API没有提供回调，只能通过无限循环主动轮询。使用无限循环时需要注意，务必在每次循环内部通过`wait()`暂停若干毫秒，否则很容易耗尽CPU。最后，我们通过超声波传感器返回的距离判断是否自动停车

### 遥控小车

乐高提供了一个红外线传感器和遥控器：红外遥控器需要很强的方向性，且遥控器太简陋，摇杆都没

使用蓝牙手柄;标准游戏手柄按键

```txt
   ┌──────┐                   ┌──────┐
  ┌┴─────┐│                  ┌┴─────┐│
┌─┴──────┴┴──────────────────┴──────┴┴─┐
│               ┌─┐ ┌─┐         ┌─┐    │
│   ┌─┐         └─┘ └─┘      ┌─┐│X│    │
│ ┌─┘ └─┐        -   +       │Y│└─┘┌─┐ │
│ └─┐ ┌─┘       ┌─┐ ┌─┐      └─┘┌─┐│A│ │
│   └─┘         └─┘ └─┘         │B│└─┘ │
│         ┌─┐    S   H    ┌─┐   └─┘    │
│       ┌─┘ └─┐         ┌─┘ └─┐        │
│       └─┐ ┌─┘         └─┐ ┌─┘        │
│         └─┘             └─┘          │
│       ────────────────────────       │
│      /                        \      │
│     /                          \     │
└────/                            \────┘
```

把游戏手柄和EV3主机用蓝牙连起来很简单，怎么用Python程序读取手柄的输入？

一般，从外部设备读取输入时，应用程序并不直接与外设打交道，而是由操作系统通过驱动程序连接外设，然后，通过操作系统提供的API读取输入。Windows程序可以通过DirectX访问外设，运行在网页的JavaScript程序可以通过浏览器提供的Gamepad API。

EV3主机运行的是Debian Linux，那么Python程序如何在Linux下读取手柄的输入？

在Linux中，系统把每个外设都映射为文件，每个设备的输入也被映射为文件。`/proc`目录挂载的就是Linux的虚拟文件系统，映射Linux的进程信息和设备信息。登录到EV3，查看`/proc/bus/input/devices`文件：

```bash
$ cat /proc/bus/input/devices 
I: Bus=0000 Vendor=0000 Product=0000 Version=0000
N: Name="LEGO MINDSTORMS EV3 Speaker"
P: Phys=
S: Sysfs=/devices/platform/sound/input/input0
U: Uniq=
H: Handlers=kbd event0 
B: PROP=0
B: EV=40001
B: SND=6

I: Bus=0019 Vendor=0001 Product=0001 Version=0100
N: Name="EV3 Brick Buttons"
P: Phys=gpio-keys/input0
S: Sysfs=/devices/platform/gpio_keys/input/input1
U: Uniq=
H: Handlers=kbd event1 
B: PROP=0
B: EV=3
B: KEY=1680 0 0 10004000
```

这个文件列出了目前系统可用的输入设备，上述两段分别代表扬声器和按钮设备。如果我们把蓝牙手柄连接到EV3，再查看文件，发现多了一段内容：

```bash
I: Bus=0005 Vendor=057e Product=2009 Version=0001
N: Name="Pro Controller"
P: Phys=00:17:ec:13:d8:1d
S: Sysfs=/devices/platform/soc@1c00000/serial8250.2/tty/ttyS2/hci0/hci0:2/0005:057E:2009.0003/input/input4
U: Uniq=00:90:e3:9b:ec:e9
H: Handlers=event2 
B: PROP=0
B: EV=10001b
B: KEY=ffff0000 0 0 0 0 0 0 0 0 0
B: ABS=3001b
B: MSC=10
```

通过`N: Name="xxx"`来搜索手柄设备，然后，通过`H: Handlers=xxx`获取设备的输入文件。例如，上述蓝牙手柄的名称是`Pro Controller`，输入是`event2`，对应到系统文件就是`/dev/input/event2`。Python代码实现如下：
定义`InputDevice`类表示输入设备
定义函数`listDevices()`通过读取`/proc/bus/input/devices`文件获取所有设备
定义函数`detectJoystick()`通过名字模糊查找手柄设备

```py
class InputDevice():
    def __init__(self):
        self.name = ''
        self.handler = ''
    def __str__(self):
        return '<Input Device: name=%s, handler=%s>' % (self.name, self.handler)
    def setName(self, name):
        if len(name) >= 2 and name.startswith('"') and name.endswith('"'):
            name = name[1:len(name)-1]
        self.name = name
    def setHandler(self, handlers):
        for handler in handlers.split(' '):
            if handler.startswith('event'):
                self.handler = handler

def listDevices():
    devices = []
    with open('/proc/bus/input/devices', 'r') as f:
        device = None
        while True:
            s = f.readline()
            if s == '':
                break
            s = s.strip()
            if s == '':
                devices.append(device)
                device = None
            else:
                if device is None:
                    device = InputDevice()
                if s.startswith('N: Name='):
                    device.setName(s[8:])
                elif s.startswith('H: Handlers='):
                    device.setHandler(s[12:])
    return devices

def detectJoystick(joystickNames):
    for device in listDevices():
        for joystickName in joystickNames:
            if joystickName in device.name:
                # 返回输入文件:
                return '/dev/input/%s' % device.handler
    # 未找到返回None:
    return None

# 搜索到手柄设备后打开文件读取输入
eventFile = detectJoystick(['Controller'])
if eventFile:
    with open(eventFile, 'rb') as infile:
        while True:
            # 读取输入
```

`eventX`文件应该以何种格式读取? 搜索一下Linux文档，在[input.txt](https://www.kernel.org/doc/Documentation/input/input.txt)中详细说明了`eventX`文件的输入格式;Linux系统把每一个输入事件都封装为一个C结构体

```c
struct input_event {
    struct timeval time; // 16字节时间戳
    unsigned short type; // 2字节事件类型
    unsigned short code; // 2字节事件代码
    unsigned int value;  // 4字节事件值
};
```

每次读取24字节并按照C的`struct`类型解码，可得到手柄输入的全部信息。在Python程序中，可以用`struct`读取：

```py
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
with open(eventFile, 'rb') as infile:
    while True:
        event = infile.read(EVENT_SIZE)
        _, _, t, c, v = struct.unpack(FORMAT, event)
        print('t = %s, c = %s, v = %s' % (t, c, v))
```

注意到`unpack()`方法的返回值，丢弃前两个8字节整数，保留`t`、`c`、`v`，分别是2字节无符号整数、2字节无符号整数和4字节无符号整数

根据Linux文档，再打印出每个事件的详细数据，把手柄的按键和摇杆都按一遍，就可以得到按键编码如下：

`t==1`时表示按键，此时`v==1`表示按下，`v==0`表示释放，`v==2`表示持续按下，对应的`c`表示按键编码。要检测`A`、`B`按钮按下

```py
if t == 1 and v == 1:
    if c == 305:
        # Button A pressed
        pass
    if c == 304:
        # Button B pressed
        pass
```

摇杆数据比较复杂，类型`t==3`表示摇杆，`c==0`，表示左摇杆的左右移动，`c==1`，表示左摇杆的上下移动，`v`介于`0~65535`，`32768`表示中心值，越往两侧偏移越多则越接近最大和最小值：

```txt
      0
      ▲
      │
0 <───┼───> 65535
      │
      ▼
    65535
```

通过一个读取手柄的无限循环来控制小车

```py
def joystickLoop(robot, eventFile):
    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)
    with open(eventFile, 'rb') as infile:
        while True:
            event = infile.read(EVENT_SIZE)
            _, _, t, c, v = struct.unpack(FORMAT, event)
            if t == 1 and v == 1:
                if c == 305:
                    # A键加速:
                    robot.setSpeed(1)
                elif c == 304:
                    # B键减速:
                    robot.setSpeed(-1)
                elif c == 307:
                    # X键退出:
                    return robot.inactive()
            elif t == 3:
                if c == 1:
                    # 左摇杆上下移动:
                    speed = 0
                    if v < 32768:
                        # 加速:
                        speed = 1
                    elif v > 32768:
                        # 减速:
                        speed = -1
                    robot.setSpeed(speed)
```

主线程通过死循环读取手柄输入，怎么读取超声波传感器的数据
利用Python的`threading`启动多线程，在另一个线程中不断检测超声波传感器，并在条件达到的时候自动停车

```py
def autoStopLoop(robot):
    while robot.active:
        if robot.speed > 0 and robot.ultrasonic.distance() < 200:
            robot.setSpeed(0)
        wait(100)

joystickEvent = detectJoystick(['Controller'])
robot = Robot()
t = threading.Thread(target=autoStopLoop, args=(robot,))
t.start()
joystickLoop(robot, joystickEvent)
```

```py
# devices.py
# list input devices
class InputDevice():
    def __init__(self):
        self.name = ''
        self.handler = ''
    def __str__(self):
        return '<Input Device: name=%s, handler=%s>' % (self.name, self.handler)
    def setName(self, name):
        if len(name) >= 2 and name.startswith('"') and name.endswith('"'):
            name = name[1:len(name)-1]
        self.name = name
    def setHandler(self, handlers):
        for handler in handlers.split(' '):
            if handler.startswith('event'):
                self.handler = handler

def listDevices():
    devices = []
    with open('/proc/bus/input/devices', 'r') as f:
        device = None
        while True:
            s = f.readline()
            if s == '':
                break
            s = s.strip()
            if s == '':
                devices.append(device)
                device = None
            else:
                if device is None:
                    device = InputDevice()
                if s.startswith('N: Name='):
                    device.setName(s[8:])
                elif s.startswith('H: Handlers='):
                    device.setHandler(s[12:])
    return devices

def detectJoystick(joystickNames):
    for device in listDevices():
        for joystickName in joystickNames:
            if joystickName in device.name:
                return '/dev/input/%s' % device.handler
    return None

# main.py 
#!/usr/bin/env pybricks-micropython
import struct, threading
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from devices import detectJoystick

class Robot():
    def __init__(self):
        self.motor = Motor(Port.B)
        self.ultrasonic = UltrasonicSensor(Port.S4)
        self.active = True
        self.speed = 0
        self.colors = [None, Color.GREEN, Color.YELLOW, Color.RED]
    def setSpeed(self, acc):
        if acc < 0:
            self.speed = max(-3, self.speed - 1)
        elif acc > 0:
            self.speed = min(3, self.speed + 1)
        else:
            self.speed = 0
        if self.speed != 0:
            self.motor.run(self.speed * 90)
        else:
            self.motor.stop()
        brick.light(self.colors[abs(self.speed)])
    def inactive(self):
        self.active = False
        self.setSpeed(0)
        brick.sound.beep()
def autoStopLoop(robot):
    while robot.active:
        if robot.speed > 0 and robot.ultrasonic.distance() < 200:
            robot.setSpeed(0)
        wait(100)
def joystickLoop(robot, eventFile):
    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)
    with open(eventFile, 'rb') as infile:
        while True:
            event = infile.read(EVENT_SIZE)
            _, _, t, c, v = struct.unpack(FORMAT, event)
            # button A, B:
            if t == 1 and v == 1:
                if c == 305:   # press A:
                    robot.setSpeed(1)
                elif c == 304: # press B:
                    robot.setSpeed(-1)
                elif c == 307: # press X:
                    return robot.inactive()
            elif t == 3:
                if c == 1: # Left stick & vertical:
                    speed = 0
                    if v < 32768:   # up:
                        speed = 1
                    elif v > 32768: # down:
                        speed = -1
                    robot.setSpeed(speed)
def buttonLoop(robot):
    while True:
        if not any(brick.buttons()):
            wait(10)
        else:
            if Button.LEFT in brick.buttons():
                robot.setSpeed(-1)
            elif Button.RIGHT in brick.buttons():
                robot.setSpeed(1)
            elif Button.CENTER in brick.buttons():
                robot.setSpeed(0)
            elif Button.UP in brick.buttons():
                return robot.inactive()
            wait(500)
def main():
    brick.sound.beep()
    joystickEvent = detectJoystick(['Controller'])
    robot = Robot()
    t = threading.Thread(target=autoStopLoop, args=(robot,))
    t.start()
    if joystickEvent:
        joystickLoop(robot, joystickEvent)
    else:
        buttonLoop(robot)
main()
```

### 遥控转向

拐弯,需要控制前轮转向或者控制两个轮子的转速,转速差实现转向

用两个马达升级一下小车
![Lego_EV3_Tank](./images/base/LGEV3Tank.jpg)

根据轮子的直径、轮距，就可以计算出在给定速度和转向角度时两个马达的转速;EV3提供`DriveBase`类自动计算并设定两个马达的转速

```py
class Driver():
    def __init__(self, leftMotor, rightMotor, diameter, axle):
        self.driver = DriveBase(leftMotor, rightMotor, diameter, axle)
        self.x = 0
        self.y = 0
        self.speed = 0
        self.steering = 0

    def drive(self, speed, steering):
        self.speed = speed
        self.steering = steering
        if self.speed == 0:
            self.driver.stop()
        else:
            self.driver.drive(self.speed, self.steering)
```

`Robot`类中，需要传入必要的参数以构造`Driver`

```py
class Robot():
    def __init__(self, leftMotor, rightMotor, diameter, axle, maxSpeed=300, maxSteering=180):
        self.driver = Driver(leftMotor, rightMotor, diameter, axle)
        self.speedStep = 32767 // maxSpeed
        self.steeringStep = 32767 // maxSteering
        ...

    def drive(self, x, y):
        speed = -y // self.speedStep
        steering = x // self.steeringStep
        self.driver.drive(speed, steering)
```

当从摇杆接收到`x`、`y`坐标后，先转换成速度和转向角度，再调用`DriveBase.drive(speed, steering)`方法，即可按指定速度和角度转向。注意到`x`、`y`坐标先处理成以`(0, 0)`为原点的坐标，以便于计算。

```py
# devices.py
# list input devices
class InputDevice():
    def __init__(self):
        self.name = ''
        self.handler = ''
    def __str__(self):
        return '<Input Device: name=%s, handler=%s>' % (self.name, self.handler)
    def setName(self, name):
        if len(name) >= 2 and name.startswith('"') and name.endswith('"'):
            name = name[1:len(name)-1]
        self.name = name
    def setHandler(self, handlers):
        for handler in handlers.split(' '):
            if handler.startswith('event'):
                self.handler = handler

def listDevices():
    devices = []
    with open('/proc/bus/input/devices', 'r') as f:
        device = None
        while True:
            s = f.readline()
            if s == '':
                break
            s = s.strip()
            if s == '':
                devices.append(device)
                device = None
            else:
                if device is None:
                    device = InputDevice()
                if s.startswith('N: Name='):
                    device.setName(s[8:])
                elif s.startswith('H: Handlers='):
                    device.setHandler(s[12:])
    return devices

def detectJoystick(joystickNames):
    for device in listDevices():
        for joystickName in joystickNames:
            if joystickName in device.name:
                return '/dev/input/%s' % device.handler
    return None

# joystick.py
# joystick control:
import struct
# define button code:

BUTTON_A = 305
BUTTON_B = 304
BUTTON_X = 307
BUTTON_Y = 306
BUTTON_PLUS = 313
BUTTON_MINUS = 312
BUTTON_START = 317
BUTTON_HOME = 316 

class JoyStick():
    def __init__(self, eventFile):
        self.eventFile = eventFile
        self.buttonHandler = None
        self.joyLeftHandler = None
        self.joyRightHandler = None
    def setButtonHandler(self, buttonHandler):
        self.buttonHandler = buttonHandler
    def setJoyLeftHandler(self, joyLeftHandler):
        self.joyLeftHandler = joyLeftHandler
    def setJoyRightHandler(self, joyRightHandler):
        self.joyRightHandler = joyRightHandler
    def startLoop(self):
        FORMAT = 'llHHI'
        EVENT_SIZE = struct.calcsize(FORMAT)
        with open(self.eventFile, 'rb') as infile:
            lx, ly, rx, ry = 0, 0, 0, 0
            while True:
                event = infile.read(EVENT_SIZE)
                _, _, t, c, v = struct.unpack(FORMAT, event)
                if t == 1 and v == 1:
                    # button pressed:
                    if self.buttonHandler:
                        if not self.buttonHandler(c):
                            return
                if t == 3:
                    if c == 0 and self.joyLeftHandler:
                        # left stick & horizontal:
                        lx = v - 32768
                        self.joyLeftHandler(lx, ly)
                    elif c == 1 and self.joyLeftHandler:
                        # left stick & vertical:
                        ly = v - 32768
                        self.joyLeftHandler(lx, ly)
                    elif c == 3 and self.joyRightHandler:
                        # right stick & horizontal:
                        rx = v - 32768
                        self.joyRightHandler(rx, ry)
                    elif c == 4 and self.joyRightHandler:
                        # right stick & vertical:
                        ry = v - 32768
                        self.joyRightHandler(rx, ry)

# main.py
#!/usr/bin/env pybricks-micropython
import struct, threading
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from devices import detectJoystick
from joystick import JoyStick, BUTTON_A, BUTTON_X

SPEED = 100
STEERING = 90
STATUS_STOPPED = 0
STATUS_FORWARD = 1
STATUS_BACKWARD = 2
STATUS_STEERING = 3
COLORS = (None, Color.GREEN, Color.RED, Color.YELLOW)

class Driver():
    def __init__(self, leftMotor, rightMotor, diameter, axle):
        self.driver = DriveBase(leftMotor, rightMotor, diameter, axle)
        self.x = 0
        self.y = 0
        self.speed = 0
        self.steering = 0
    def drive(self, speed, steering):
        self.speed = speed
        self.steering = steering
        if self.speed == 0:
            self.driver.stop()
        else:
            self.driver.drive(self.speed, self.steering)
class Robot():
    def __init__(self, leftMotor, rightMotor, topMotor, diameter, axle, maxSpeed=300, maxSteering=180, port=Port.S4):
        self.driver = Driver(leftMotor, rightMotor, diameter, axle)
        self.cannon = topMotor
        self.ultrasonic = UltrasonicSensor(port)
        self.speedStep = 32767 // maxSpeed
        self.steeringStep = 32767 // maxSteering
        self.active = True
    def drive(self, x, y):
        # map y (-32768 ~ +32767) to speed (+maxSpeed ~ -maxSpeed):
        speed = -y // self.speedStep
        # map x (-32768 ~ +32767) to steering (-maxSteering ~ +maxSteering):
        steering = x // self.steeringStep
        self.driver.drive(speed, steering)
    def target(self, x):
        self.cannon.run(-x // 327)
    def fire(self):
        brick.sound.file('cannon.wav')
    def inactive(self):
        self.active = False
        self.drive(0, 0)
        brick.sound.beep()
def autoStopLoop(robot):
    while robot.active:
        if robot.ultrasonic.distance() < 200:
            robot.drive(0, 0)
        wait(100)
def main():
    brick.sound.beep()
    joystickEvent = detectJoystick(['Controller'])
    if joystickEvent:
        robot = Robot(Motor(Port.D), Motor(Port.A), Motor(Port.B), 55, 200)
        t = threading.Thread(target=autoStopLoop, args=(robot,))
        t.start()
        def onButtonPressed(code):
            if code == BUTTON_X:
                robot.inactive()
                return False
            if code == BUTTON_A:
                robot.fire()
            return True
        def onLeftJoyChanged(x, y):
            robot.drive(x, y)
        def onRightJoyChanged(x, y):
            robot.target(x)
        joystick = JoyStick(joystickEvent)
        joystick.setButtonHandler(onButtonPressed)
        joystick.setJoyLeftHandler(onLeftJoyChanged)
        joystick.setJoyRightHandler(onRightJoyChanged)
        joystick.startLoop()
    else:
        brick.sound.beep()
main()
```

## 实战

目标是一个Blog网站，包含日志、用户和评论3大部分；项目名称`awesome-webapp`

https://wangwangyz.site/
https://aodabo.tech/

### Day 1 - 搭建开发环境

```bash
$ python --version 
Python 3.8.10
$ pip install aiohttp # 异步框架aiohttp
$ pip install jinja2  # 前端模板引擎
$ docker run -itd --name mysql -v /d/dockerData/mysql:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:latest ## docker mysql 数据库
$ pip install aiomysql # MySQL aiomysql
```

项目结构

```txt
awesome-webapp/          <-- 根目录
|
+- backup/               <-- 备份目录
|
+- conf/                 <-- 配置文件
|
+- dist/                 <-- 打包目录
|
+- www/                  <-- Web目录，存放.py文件
|  |
|  +- static/            <-- 存放静态文件
|  |
|  +- templates/         <-- 存放模板文件
|
+- ios/                  <-- 存放iOS App工程
|
+- LICENSE               <-- 代码LICENSE
```

### Day 2 - 编写Web App骨架

```py
# app.py
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
```

### Day 3 - 编写ORM

访问数据库需要创建数据库连接、游标对象，然后执行SQL语句，最后处理异常，清理资源
把常用的`SELECT`、`INSERT`、`UPDATE`和`DELETE`操作用函数封装起来
Web框架使用基于`asyncio`的`aiohttp`，基于协程的异步模型,才能处理大量用户的请求(耗时的IO操作)
异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”
`aiomysql`为MySQL数据库提供了异步IO的驱动

#### 创建连接池

创建一个全局的**连接池**,每个HTTP请求都可以从连接池中直接获取数据库连接;好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。

连接池由全局变量`__pool`存储，缺省情况下将编码设置为`utf8`，自动提交事务：

```py
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    _ppol = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop = loop
    )

##### Select
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
            await cur.close()
            logging.info('rows returned: %s' % len(rs))
            return rs
# SQL语句的占位符是?，MySQL的占位符是%s
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn: # yield from将调用一个子协程（也就是在一个协程中调用另一个协程）并直接获得子协程的返回结果
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ()) # 自动替换占位符
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

##### Insert, Update, Delete
# 执行都需要相同的参数，返回一个整数表示影响的行数,定义通用函数
async def execute(sql, args):
    log(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.repalce('?','%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected
```

#### ORM

设计ORM需要从上层调用者角度来设计;先考虑如何定义一个`User`对象，然后把数据库表`users`和它关联起来

```py
from orm import Model, StringField, IntegerField

# User类中的__table__、id和name是类的属性,不是实例的属性
# 在类级别上定义的属性用来描述User对象和表的映射关系
# 实例属性必须通过__init__()方法去初始化，所以两者互不干扰
class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()

# 创建实例:
user = User(id=123, name='Michael')
# 存入数据库:
user.insert()
# 查询所有User对象:
users = User.findAll()
```

定义有ORM映射的基类`Model`

```py
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def getValue(self, key):
        return getattr(self, key, None)
    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value
# Model从dict继承,具备所有dict功能
# 实现了特殊方法__getattr__()和__setattr__()

# user['id']  # 123
# user.id     # 123

#### Field和各种Field子类
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

##### 映射varchar的StringField：
class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

##### 如何将具体的子类如User的映射信息读取出来？通过metaclass：ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 排除Model类本身:
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        # 获取table名称:
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        # 获取所有的Field和主键名:
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键:
                    if primaryKey:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)

## 任何继承自Model的类（比如User）;会自动通过ModelMetaclass扫描映射关系，并存储到自身的类属性如__table__、__mappings__中
## 往Model类添加class方法，就可以让所有子类调用class方法
class Model(dict, metaclass=ModelMetaclass):
    ...
    @classmethod
    async def find(cls, pk):
        ' find object by primary key. '
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    @classmethod
    @asyncio.coroutine
    def find(cls, pk):
        ' find object by primary key. '
        rs = yield from select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    @asyncio.coroutine
    def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = yield from execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

#### User类现在就可以通过类方法实现主键查找：
user = await User.find('123')
user = yield from User.find('123')
#### 把一个User实例存入数据库
user = User(id=123, name='Michael')
yield from user.save()      # user.save() 创建一个携程， yield from user.save() 创建携程并执行
await user.save()
```

完善ORM，对于查找;`findAll()`:根据WHERE条件查找;`findNumber()`:根据WHERE条件查找，但返回的是整数，适用于`select count(*)`类型的SQL
`update()`,`remove()`

### Day 4 - 编写Model

```py
import time, uuid
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
```

在编写ORM时，给一个Field增加`default`参数可让ORM自己填入缺省值。缺省值可作为函数对象传入，在调用`save()`时自动计算
例如，主键`id`的缺省值是函数`next_id`，创建时间`created_at`的缺省值是函数`time.time`，可以自动设置当前日期和时间

日期和时间用`float`类型存储，而不是`datetime`类型，好处是不必关心数据库的时区以及时区转换问题，排序非常简单，显示时，做一个`float`到`str`的转换

#### 初始化数据库表

```sql
-- schema.sql
drop database if exists awesome;
create database awesome;
use awesome;
-- grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';
create user 'www-data'@'localhost' identified by 'www-data';
grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' with grant option;

--create user 'www-data'@'%' identified by 'www-data';
--grant select, insert, update, delete on awesome.* to 'www-data'@'%' with grant option;

-- GRANT ALL ON *.* to 'www-data'@'localhost' with grant option;

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
```

初始化命令：`$ mysql -u root -p < schema.sql`

```py
# 编写数据访问代码
import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, host='192.168.31.10',user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    # 添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
```

### Day 5 - 编写Web框架

编写一个Web框架,`aiohttp`相对比较底层

```py
# aiohttp 处理流程
# 第一步，编写一个用@asyncio.coroutine装饰的函数：
@asyncio.coroutine
def handle_url_xxx(request):
    # 第二步，传入的参数需要自己从request中获取：
    url_param = request.match_info['key']
    query_params = parse_qs(request.query_string)
    # ...
    # 最后，需要自己构造Response对象
    text = render('template', data)
    return web.Response(text.encode('utf-8'))

# 以上的重复的工作可以由框架完成
# 处理带参数的URL/blog/{id}
@get('/blog/{id}')
def get_blog(id):
    pass
# 处理query_string参数可以通过关键字参数**kw或者命名关键字参数接收
@get('/api/comments')
def api_comments(*, page='1'):
    pass

# 函数的返回值，不一定是web.Response对象，可以是str、bytes或dict
# 渲染模板，可以这么返回一个dict
return {
    '__template__': 'index.html',
    'data': '...'
}
```

Web框架的设计是完全从使用者出发，目的是让使用者编写尽可能少的代码。

编写简单的函数而非引入`request`和`web.Response`有额外的好处，就是可以单独测试，否则，需要模拟一个`request`才能测试

```py
# @get和@post
def get(path):
    '''
    Define decorator @get('path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator
```

```py
# 定义RequestHandler 封装一个URL处理函数
# 从URL函数中分析其需要接收的参数，从request中获取必要的参数，调用URL函数，然后把结果转换为web.Response对象
class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        ...

    @asyncio.coroutine
    def __call__(self, request):
        kw = ... 获取参数
        r = yield from self._func(**kw)
        return r

    def add_route(app, fn):
        method = getattr(fn, '__method__', None)
        path = getattr(fn, '__route__', None)
        if path is None or method is None:
            raise ValueError('@get or @post not defined in %s.' % str(fn))
        if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
            fn = asyncio.coroutine(fn)
        logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
        app.router.add_route(method, path, RequestHandler(app, fn))

# 把很多次add_route()注册的调用
add_route(app, handles.index)
add_route(app, handles.blog)
add_route(app, handles.create_comment)
# ...
# 变成自动扫描
# 自动把handler模块的所有符合条件的函数注册了:
add_routes(app, 'handlers')

def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                add_route(app, fn)

# 在app.py中加入middleware、jinja2模板和自注册的支持
app = web.Application(loop=loop, middlewares=[
    logger_factory, response_factory
])
init_jinja2(app, filters=dict(datetime=datetime_filter))
add_routes(app, 'handlers')
add_static(app)
```

#### middleware

`middleware`是一种拦截器，一个URL在被某个函数处理前，可以经过一系列的`middleware`的处理

一个`middleware`可以改变URL的输入、输出，甚至可以决定不继续处理而直接返回。`middleware`的用处在于把通用的功能从每个URL处理函数中拿出来，集中放到一个地方。例如，一个记录URL日志的`logger`可以简单定义如下：

```py
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        # 记录日志:
        logging.info('Request: %s %s' % (request.method, request.path))
        # 继续处理请求:
        return (yield from handler(request))
    return logger

# response middleware把返回值转换为web.Response对象再返回

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        # 结果:
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            ...
# 有了这些基础设施，就可专注地往handlers模块不断添加URL处理函数，可以极大地提高开发效率
```

### Day 6 - 编写配置文件

```py
# config_default.py

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}

# 如果要部署到服务器时，通常需要修改数据库的host等信息，直接修改config_default.py不是好办法，
# 更好的方法是编写一个config_override.py，用来覆盖某些默认设置
# config_override.py
configs = {
    'db':{
        'host':'192.168.31.10'
    }
}
# 把config_default.py作为开发环境的标准配置，
# 把config_override.py作为生产环境的标准配置，
# 既方便地在本地开发，又可以随时把应用部署到服务器上

# config.py
configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass
```

### Day 7 - 编写MVC

```py
# 编写处理首页URL的函数
@get('/')
async def index(request):
    users = await User.findALl()
    return {
        '__template__': 'test.html',
        'users': users
    }
```

模板文件

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Test users - Awesome Python Webapp</title>
</head>
<body>
    <h1>All users</h1>
    {% for u in users %}
    <p> {{ u.name }} / {{ u.email }} </p>
    {% endfor %}
</body>
</html>
```

### Day 8 - 构建前端

选择[uikit](https://getuikit.com/)CSS框架,可从[uikit首页](https://getuikit.com/)下载打包的资源文件[uikit2.6](https://www.cdnpkg.com/uikit/2.6.0)

```bash
static/
+- css/
|  +- addons/
|  |  +- uikit.addons.min.css
|  |  +- uikit.almost-flat.addons.min.css
|  |  +- uikit.gradient.addons.min.css
|  +- awesome.css
|  +- uikit.almost-flat.addons.min.css
|  +- uikit.gradient.addons.min.css
|  +- uikit.min.css
+- fonts/
|  +- fontawesome-webfont.eot
|  +- fontawesome-webfont.ttf
|  +- fontawesome-webfont.woff
|  +- FontAwesome.otf
+- js/
   +- awesome.js
   +- html5.js
   +- jquery.min.js
   +- uikit.min.js
```

模板引擎考虑到页面上重复的HTML部分的复用问题, 相同部分`inc_header.html`和`inc_footer.html`可共享;
include方法不利于页面整体结构的维护

```html
<html>
    <% include file="inc_header.html" %>
    <% include file="index_body.html" %>
    <% include file="inc_footer.html" %>
</html>
```

jinjia2 模板有种“继承”方式，实现模板的复用更简单.
“继承”模板的方式是通过编写一个“父模板”，在父模板中定义一些可替换的block（块）。然后，编写多个“子模板”，每个子模板都可以只替换父模板定义的block

```html
<!-- base.html -->
<html>
    <head>
        <title>{% block title%} 这里定义了一个名为title的block {% endblock %}</title>
    </head>
    <body>
        {% block content %} 这里定义了一个名为content的block {% endblock %}
    </body>
</html>

<!-- a.html -->
{% extends 'base.html' %}

{% block title %} A {% endblock %}

{% block content %}
    <h1>Chapter A</h1>
    <p>blablabla...</p>
{% endblock%}

<!-- b.html -->
{% extends 'base.html' %}

{% block title %} B {% endblock %}

{% block content %} 
    <h1>Chapter</h1>
    <ul>
        <li>list 1</li>
        <li>list 2</li>
    </ul>
{% endblock %}
```

定义好父模板的整体布局和CSS样式，编写子模板就会非常容易

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    {% block meta %}<!-- block meta 子页面定义一些meta，例如rss feed -->{% endblock %}
    <title>{% block title %} ? {% endblock %} - Awesome Python Webapp</title><!--覆盖页面的标题-->
    <link rel="stylesheet" href="/static/css/uikit.min.css">
    <link rel="stylesheet" href="/static/css/uikit.gradient.min.css">
    <link rel="stylesheet" href="/static/css/awesome.css" />
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/md5.js"></script>
    <script src="/static/js/uikit.min.js"></script>
    <script src="/static/js/awesome.js"></script>
    {% block beforehead %}<!-- before head  在<head>标签关闭前插入JavaScript代码-->{% endblock %}
</head>
<body>
    <nav class="uk-navbar uk-navbar-attached uk-margin-bottom">
        <div class="uk-container uk-container-center">
            <a href="/" class="uk-navbar-brand">Awesome</a>
            <ul class="uk-navbar-nav">
                <li data-url="blogs"><a href="/"><i class="uk-icon-home"></i> 日志</a></li>
                <li><a target="_blank" href="#"><i class="uk-icon-book"></i> 教程</a></li>
                <li><a target="_blank" href="#"><i class="uk-icon-code"></i> 源码</a></li>
            </ul>
            <div class="uk-navbar-flip">
                <ul class="uk-navbar-nav">
                {% if user %}
                    <li class="uk-parent" data-uk-dropdown>
                        <a href="#0"><i class="uk-icon-user"></i> {{ user.name }}</a>
                        <div class="uk-dropdown uk-dropdown-navbar">
                            <ul class="uk-nav uk-nav-navbar">
                                <li><a href="/signout"><i class="uk-icon-sign-out"></i> 登出</a></li>
                            </ul>
                        </div>
                    </li>
                {% else %}
                    <li><a href="/signin"><i class="uk-icon-sign-in"></i> 登陆</a></li>
                    <li><a href="/register"><i class="uk-icon-edit"></i> 注册</a></li>
                {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="uk-container uk-container-center">
        <div class="uk-grid">
            <!-- content -->
            {% block content %}
            {% endblock %}
            <!-- // content -->
        </div>
    </div>

    <div class="uk-margin-large-top" style="background-color:#eee; border-top:1px solid #ccc;">
        <div class="uk-container uk-container-center uk-text-center">
            <div class="uk-panel uk-margin-top uk-margin-bottom">
                <p>
                    <a target="_blank" href="#" class="uk-icon-button uk-icon-weibo"></a>
                    <a target="_blank" href="#" class="uk-icon-button uk-icon-github"></a>
                    <a target="_blank" href="#" class="uk-icon-button uk-icon-linkedin-square"></a>
                    <a target="_blank" href="#" class="uk-icon-button uk-icon-twitter"></a>
                </p>
                <p>Powered by <a href="#">Awesome Python Webapp</a>. Copyright &copy; 2014. [<a href="/manage/" target="_blank">Manage</a>]</p>
                <p><a href="http://www.liaoxuefeng.com/" target="_blank">www.liaoxuefeng.com</a>. All rights reserved.</p>
                <a target="_blank" href="#"><i class="uk-icon-html5" style="font-size:64px; color: #444;"></i></a>
            </div>
        </div>
    </div>
</body>
</html>
```

首页改造，从`__base__.html`继承一个`blogs.html`

```py
{% extends '__base__.html' %}

{% block title %}日志{% endblock %}

{% block content %}

    <div class="uk-width-medium-3-4">
        {% for blog in blogs %}
            <article class="uk-article">
                <h2><a href="/blog/{{ blog.id }}">{{ blog.name }}</a></h2>
                <p class="uk-article-meta">发表于{{ blog.created_at}}</p>
                <p>{{ blog.summary }}</p>
                <p><a href="/blog/{{ blog.id }}">继续阅读 <i class="uk-icon-angle-double-right"></i></a></p>
            </article>
            <hr class="uk-article-divider">
        {% endfor %}
    </div>

    <div class="uk-width-medium-1-4">
        <div class="uk-panel uk-panel-header">
            <h3 class="uk-panel-title">友情链接</h3>
            <ul class="uk-list uk-list-line">
                <li><i class="uk-icon-thumbs-o-up"></i> <a target="_blank" href="#">编程</a></li>
                <li><i class="uk-icon-thumbs-o-up"></i> <a target="_blank" href="#">读书</a></li>
                <li><i class="uk-icon-thumbs-o-up"></i> <a target="_blank" href="#">Python教程</a></li>
                <li><i class="uk-icon-thumbs-o-up"></i> <a target="_blank" href="#">Git教程</a></li>
            </ul>
        </div>
    </div>

{% endblock %}
```

```py
@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
```

Blog的创建日期显示的是一个浮点数，因为它是由这段模板渲染出来的：`<p class="uk-article-meta">发表于{{ blog.created_at }}</p>`
解决方法是通过jinja2的filter（过滤器），把一个浮点数转换成日期字符串。编写一个`datetime`的filter，`<p class="uk-article-meta">发表于{{ blog.created_at|datetime }}</p>`, `|`之后的是filter;filter需要在初始化jinja2时设置

```py
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return '1分钟前'
    if delta < 3600:
        return '%s分钟前' % (delta // 60)
    if delta < 86400:
        return '%s小时前' % (delta // 3600)
    if delta < 604800:
        return '%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return '%s年%s月%s日' % (dt.year, dt.month, dt.day)

...
init_jinja2(app, filters=dict(datetime=datetime_filter))
...
```

### Day 9 - 编写API

Roy Fielding博士在2000年,提出[REST](https://zh.wikipedia.org/wiki/REST)（Representational State Transfer）取代了复杂而笨重的SOAP，成为Web API的标准了
REST就是一种设计API的模式。最常用的数据格式是JSON;以JSON格式编写的REST风格的API具有简单、易读、易用的特点。

```py
@get('/api/users')
def api_get_users(*, page='1'):
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = yield from User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p, users=users)
```

只要返回一个`dict`，后续的`response`这个`middleware`就可以把结果序列化为JSON并返回。定义一个`APIError`,API调用时发生了逻辑错误（比如用户不存在），其他的Error视为Bug，返回的错误代码为`internalerror`。

### Day 10 - 用户注册和登录

通过API实现用户注册

```py
_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@post('/api/users')
def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):    # 用户口令是客户端传递的经过SHA1计算后的40位Hash字符串，所以服务器端并不知道用户的原始口令
        raise APIValueError('passwd')
    users = yield from User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    yield from user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r
```

创建注册页面

```html
{% extends '__base__.html' %}

{% block title %}注册{% endblock %}

{% block beforehead %}

<script>
function validateEmail(email) {
    var re = /^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$/;
    return re.test(email.toLowerCase());
}
$(function () {
    var vm = new Vue({
        el: '#vm',
        data: {
            name: '',
            email: '',
            password1: '',
            password2: ''
        },
        methods: {
            submit: function (event) {
                event.preventDefault();
                var $form = $('#vm');
                if (! this.name.trim()) {
                    return $form.showFormError('请输入名字');
                }
                if (! validateEmail(this.email.trim().toLowerCase())) {
                    return $form.showFormError('请输入正确的Email地址');
                }
                if (this.password1.length < 6) {
                    return $form.showFormError('口令长度至少为6个字符');
                }
                if (this.password1 !== this.password2) {
                    return $form.showFormError('两次输入的口令不一致');
                }
                var email = this.email.trim().toLowerCase();
                $form.postJSON('/api/users', {
                    name: this.name.trim(),
                    email: email,
                    passwd: CryptoJS.SHA1(email + ':' + this.password1).toString()
                }, function (err, r) {
                    if (err) {
                        return $form.showFormError(err);
                    }
                    return location.assign('/');
                });
            }
        }
    });
    $('#vm').show();
});
</script>

{% endblock %}

{% block content %}

    <div class="uk-width-2-3">
        <h1>欢迎注册！</h1>
        <form id="vm" v-on="submit: submit" class="uk-form uk-form-stacked">
            <div class="uk-alert uk-alert-danger uk-hidden"></div>
            <div class="uk-form-row">
                <label class="uk-form-label">名字:</label>
                <div class="uk-form-controls">
                    <input v-model="name" type="text" maxlength="50" placeholder="名字" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">电子邮件:</label>
                <div class="uk-form-controls">
                    <input v-model="email" type="text" maxlength="50" placeholder="your-name@example.com" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">输入口令:</label>
                <div class="uk-form-controls">
                    <input v-model="password1" type="password" maxlength="50" placeholder="输入口令" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">重复口令:</label>
                <div class="uk-form-controls">
                    <input v-model="password2" type="password" maxlength="50" placeholder="重复口令" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <button type="submit" class="uk-button uk-button-primary"><i class="uk-icon-user"></i> 注册</button>
            </div>
        </form>
    </div>

{% endblock %}
```

用户登录比用户注册复杂。由于HTTP协议是无状态协议，服务器要跟踪用户状态，只能通过cookie实现。大多数Web框架提供Session功能来封装保存用户状态的cookie

Session优点是简单易用，可以直接从Session中取出用户登录信息；
Session缺点是服务器需要在内存中维护一个映射表来存储用户登录信息，如果有两台以上服务器，就需要对Session做集群，因此，使用Session的Web App很难扩展。

采用直接读取cookie的方式来验证用户登录，每次用户访问任意URL，都会对cookie进行验证，这种方式的好处是保证服务器处理任意的URL都是无状态的，可扩展到多台服务器

由于登录成功后是由服务器生成一个cookie发送给浏览器，所以，要保证这个cookie不会被客户端伪造出来。

实现防伪造cookie的关键是通过一个单向算法（例如SHA1），举例如下：

当用户输入了正确的口令登录成功后，服务器可以从数据库取到用户的id，并按照如下方式计算出一个字符串：`"用户id" + "过期时间" + SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")`

当浏览器发送cookie到服务器端后，服务器可以拿到的信息包括：用户id,过期时间,SHA1值

如果未到过期时间，服务器就根据用户id查找用户口令，并计算：`SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")`

并与浏览器cookie中的哈希进行比较，如相等，则用户已登录，否则，cookie是伪造的

这个算法的关键在于SHA1是一种单向算法，即可通过原始字符串计算出SHA1结果，但无法通过SHA1结果反推出原始字符串。

```py
# 实现登录API
@post('/api/authenticate')
def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = yield from User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r
    
# 计算加密cookie:
def user2cookie(user, max_age):
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)
```

对于每个URL处理函数，都去写解析cookie的代码，会导致代码多次重复

利用middle在处理URL之前，解析cookie，并将登录用户绑定到request对象上,后续的URL处理函数就可以直接拿到登录用户

```py
@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        return (yield from handler(request))
    return auth
    
# 解密cookie:
@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = yield from User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None
```

### Day 11 - 编写日志创建页

编写REST API，用于创建一个Blog;非常容易测试

```py
@post('/api/blogs')
def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip())
    yield from blog.save()
    return blog
```

生成前端页面最早的方式是拼接字符串,完全不具备可维护性;后模板方式. 在页面上大量使用JavaScript,模板方式仍会导致JavaScript代码与后端代码绑得非常紧密,以至于难以维护;根本原因在于负责显示的HTML DOM模型与负责数据和交互的JavaScript代码没有分割清楚。

[MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)Model View ViewModel模式应运而生

MVVM最早由微软提出来，它借鉴了桌面应用程序的MVC思想，在前端页面中，把Model用纯JavaScript对象表示：

```html
<!-- Model -->
<script>
    var blog = {
        name: 'hello',
        summary: 'this is summary',
        content: 'this is content...'
    };
</script>

<!-- View -->
<form action="/api/blogs" method="post">
    <input name="name">
    <input name="summary">
    <textarea name="content"></textarea>
    <button type="submit">OK</button>
</form>
```

把Model和View关联起来的就是ViewModel。ViewModel负责把Model的数据同步到View显示出来，还负责把View的修改同步回Model

许多成熟的MVVM框架，例如AngularJS，KnockoutJS等. 选择[Vue](https://vuejs.org/)这个简单易用的MVVM框架来实现创建Blog的页面`templates/manage_blog_edit.html`

```html
{% extends '__base__.html' %}

{% block title %}编辑日志{% endblock %}

{% block beforehead %}
<script>
    var ID = '{{ id }}', action = '{{ action }}'

    function initVM(blog){
        var vm = new Vue({
            el: '#vm',
            data: blog,
            methods:{
                submit:function(event){
                    event.preventDefault();
                    var $form = $('#vm').find('form');
                    $form.postJSON(action, this.$data , function(err, r){
                        if(err){
                            $form.showFormError(err);
                        } else {
                            return location.assign('/api/blogs/' + r.id);
                        }
                    });
                }
            }
        });
        $('#vm').show();
    }

    $(function(){
        if(ID){
            getJSON('/api/blogs/' + ID, function(err, blog){
                if(err){
                    return fatal(err);
                }
                $('#loading').hide();
                initVM(blog);
            });
        } else {
            $('#loading').hide();
            initVM({name:'', summary:'', content:''});
        }
    })
</script>
{% endblock %}

{% block content %}
<div class="uk-width-1-1 uk-margin-bottom">
    <div class="uk-panel uk-panel-box">
        <ul class="uk-breadcrumb">
            <li><a href="/manage/comments">评论</a></li>
            <li><a href="/manage/blogs">日志</a></li>
            <li><a href="/manage/users">用户</a></li>
        </ul>
    </div>
</div>
<div id="error" class="uk-width-1-1"></div>
<div id="loading" class="uk-width-1-1 uk-text-center">
    <span><i class="uk-icon-spinner uk-icon-medium uk-icon-spin"></i> 正在加载...</span>
</div>
<div id="vm" class="uk-width-2-3">
    <form v-on="submit: submit" class="uk-form uk-form-stacked">
        <div class="uk-alert uk-alert-danger uk-hidden"></div>
        <div class="uk-form-row">
            <label class="uk-form-label">标题:</label>
            <div class="uk-form-controls">
                <input v-model="name" name="name" type="text" placeholder="标题" class="uk-width-1-1">
            </div>
        </div>
        <div class="uk-form-row">
            <label class="uk-form-label">摘要:</label>
            <div class="uk-form-controls">
                <textarea v-model="summary" rows="4" name="summary" placeholder="摘要" class="uk-width-1-1" style="resize:none;"></textarea>
            </div>
        </div>
        <div class="uk-form-row">
            <label class="uk-form-label">内容:</label>
            <div class="uk-form-controls">
                <textarea v-model="content" rows="16" name="content" placeholder="内容" class="uk-width-1-1" style="resize:none;"></textarea>
            </div>
        </div>
        <div class="uk-form-row">
            <button type="submit" class="uk-button uk-button-primary"><i class="uk-icon-save"></i> 保存</button>
            <a href="/manage/blogs" class="uk-button"><i class="uk-icon-times"></i> 取消</a>
        </div>
    </form>
</div>
{% endblock %}
```

初始化Vue时，指定3个参数：

* `el`：根据选择器查找绑定的View，这里是`#vm`，就是id为`vm`的DOM，对应一个`<div>`标签
* `data`：JavaScript对象表示的Model，初始化为`{ name: '', summary: '', content: ''}`
* `methods`：View可以触发的JavaScript函数，`submit`就是提交表单时触发的函数

接下来，在`<form>`标签中，用几个`v-model`，就可以让Vue把Model和View关联起来：`<!-- input的value和Model的name关联起来了 --><input v-model="name" class="uk-width-1-1">`;Form表单通过`<form v-on="submit: submit">`把提交表单的事件关联到`submit`方法

在MVVM中，Model和View是双向绑定的.在Chrome控制台，可通过`vm.name`访问单个属性，或通过`vm.$data`访问整个Model

### Day 12 - 编写日志列表页

```py
#apis.py 定义Page类用于存储分页信息
class Page(object):
    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index - 1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1
    def __str__(self):
        return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)
    __repr__ = __str__

# handlers.py
@get('/api/blogs')
def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)

@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }
```

```json
// 模板页面首先通过API：GET /api/blogs?page=?拿到Model
// http://localhost:9000/api/blogs?page=?
{
  "page": {
    "item_count": 13,
    "page_size": 10,
    "page_count": 2,
    "page_index": 1,
    "offset": 0,
    "limit": 10,
    "has_next": true,
    "has_previous": false
  },
  "blogs": [...]
}
```

```html
<!--通过Vue初始化MVVM -->
<script>
function initVM(data) {
    var vm = new Vue({
        el: '#vm',
        data: {
            blogs: data.blogs,
            page: data.page
        },
        methods: {
            edit_blog: function (blog) {
                location.assign('/manage/blogs/edit?id=' + blog.id);
            },
            delete_blog: function (blog) {
                if (confirm('确认要删除“' + blog.name + '”？删除后不可恢复！')) {
                    postJSON('/api/blogs/' + blog.id + '/delete', function (err, r) {
                        if (err) {
                            return alert(err.message || err.error || err);
                        }
                        refresh();
                    });
                }
            }
        }
    });
    $('#vm').show();
}
$(function() {
    getJSON('/api/blogs', {
        page: {{ page_index }}
    }, function (err, results) {
        if (err) {
            return fatal(err);
        }
        $('#loading').hide();
        initVM(results);
    });
});
</script>

<!--View的容器是#vm，包含一个table，用v-repeat可把Model的数组blogs直接变成多行<tr>： -->
<div id="vm" class="uk-width-1-1">
    <a href="/manage/blogs/create" class="uk-button uk-button-primary"><i class="uk-icon-plus"></i> 新日志</a>
    <table class="uk-table uk-table-hover">
        <thead>
            <tr>
                <th class="uk-width-5-10">标题 / 摘要</th>
                <th class="uk-width-2-10">作者</th>
                <th class="uk-width-2-10">创建时间</th>
                <th class="uk-width-1-10">操作</th>
            </tr>
        </thead>
        <tbody>
            <tr v-repeat="blog: blogs" >
                <td>
                    <a target="_blank" v-attr="href: '/blog/'+blog.id" v-text="blog.name"></a>
                </td>
                <td>
                    <a target="_blank" v-attr="href: '/user/'+blog.user_id" v-text="blog.user_name"></a>
                </td>
                <td>
                    <span v-text="blog.created_at.toDateTime()"></span>
                </td>
                <td>
                    <a href="#0" v-on="click: edit_blog(blog)"><i class="uk-icon-edit"></i>
                    <a href="#0" v-on="click: delete_blog(blog)"><i class="uk-icon-trash-o"></i>
                </td>
            </tr>
        </tbody>
    </table>
    <div v-component="pagination" v-with="page"></div>
</div>    
```

往Model的`blogs`中增加一个Blog元素，table增加一行；`blogs`的某个元素删除，table减少一行。所有复杂的Model-View的映射逻辑全部由MVVM框架完成，只需要在HTML中写上`v-repeat`指令，就什么都不用管了。

可把`v-repeat="blog: blogs"`看成循环代码，所以，可在一个`<tr>`内部引用循环变量`blog`。`v-text`和`v-attr`指令分别用于生成文本和DOM节点属性

### Day 13 - 提升开发效率

一个Web App的框架完全搭建完成，从后端的API到前端的MVVM，流程已经跑通。让服务器检测到代码修改后自动重新加载。

Django的开发环境在Debug模式下可做到自动重新加载，如果编写的服务器也能实现这个功能，就能大大提升开发效率

Python的第三方库`watchdog`可以利用操作系统的API来监控目录文件的变化，并发送通知:`$ pip3 install watchdog`;利用`watchdog`接收文件变化的通知，如果是`.py`文件，就自动重启`wsgiapp.py`进程;利用Python自带的`subprocess`实现进程的启动和终止，并把输入输出重定向到当前进程的输入输出中

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = ''
import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def log(s):
    print('[Monitor] %s' % s)

class MyFileSystemEventHander(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()

command = ['echo', 'ok']
process = None

def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None

def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

def restart_process():
    kill_process()
    start_process()

def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonitor your-script.py')
        exit(0)
    if argv[0] != 'python3':
        argv.insert(0, 'python3')
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)
```

`$ python3 pymonitor.py wsgiapp.py`;给`pymonitor.py`加上可执行权限`$ ./pymonitor.py app.py` win(`pymonitor.py app.py`)

```log
python pymonitor.py app.py
[Monitor] Watching directory F:\GitHub\Learning\6_Python\awesome-webapp\www...
[Monitor] Start process python app.py...
...
INFO:root:server started at http://127.0.0.1:9000...
[Monitor] Python source file changed: F:\GitHub\Learning\6_Python\awesome-webapp\www\handlers.py
[Monitor] Kill process [4160]...
[Monitor] Process ended with code 1.
[Monitor] Start process python app.py...
[Monitor] Python source file changed: F:\GitHub\Learning\6_Python\awesome-webapp\www\handlers.py
[Monitor] Kill process [12980]...
[Monitor] Process ended with code 1.
[Monitor] Start process python app.py...
...
INFO:root:server started at http://127.0.0.1:9000...
```

### Day 14 - 完成Web App

把当前用户绑定到`request`上，并对URL`/manage/`进行拦截，检查当前用户是否是管理员身份

```py
# app.py
@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth
```

后端API：

* 获取日志：`GET /api/blogs`
* 创建日志：`POST /api/blogs`
* 修改日志：`POST /api/blogs/:blog_id`
* 删除日志：`POST /api/blogs/:blog_id/delete`
* 获取评论：`GET /api/comments`
* 创建评论：`POST /api/blogs/:blog_id/comments`
* 删除评论：`POST /api/comments/:comment_id/delete`
* 创建新用户：`POST /api/users`
* 获取用户：`GET /api/users`

管理页面：

* 评论列表页：`GET /manage/comments`
* 日志列表页：`GET /manage/blogs`
* 创建日志页：`GET /manage/blogs/create`
* 修改日志页：`GET /manage/blogs/`
* 用户列表页：`GET /manage/users`

用户浏览页面

* 注册页：`GET /register`
* 登录页：`GET /signin`
* 注销页：`GET /signout`
* 首页：`GET /`
* 日志详情页：`GET /blog/:blog_id`

### Day 15 - 部署Web App

[DevOps](https://zh.wikipedia.org/wiki/DevOps):开发和运维要变成一个整体,理念把运维、监控等功能融入到开发中

#### 部署到Linux服务器

[Ubuntu Server 14.04 LTS](https://ubuntu.com/download/server), 确保ssh服务正在运行`$ sudo apt-get install openssh-server`;公钥复制到服务器端用户的`.ssh/authorized_keys`中,可通过证书实现无密码连接

高性能的Web服务器:Nginx;处理静态资源，同时作为反向代理把动态请求交给Python代码处理

```ascii
┌───────────────────────────────────────┐
│ ┌───────┐     ┌─────────┐     ┌─────┐ │
│ │ Nginx │◄───►│ awesome │◄───►│MySQL│ │
│ └───────┘     └─────────┘     └─────┘ │
│                  Linux                │
└───────────────────────────────────────┘
```

Nginx负责分发请求

```ascii

   ┌─────────┐
   │ Browser │
   └─────────┘
        ▲
┌───────│─────────────────────────────────────────────┐
│       ▼                                             │
│  ┌─────────┐  url=/static/                          │
│  │  Nginx  │◄─────────────► /srv/awesome/www/static │
│  └─────────┘                                        │
│       ▲                                             │
│       │ url=/                                       │
│       ▼                                             │
│  ┌─────────┐                                        │
│  │ awesome │◄─────────────► /srv/awesome/www        │
│  └─────────┘                                        │
│                                                     │
│                       Linux                         │
└─────────────────────────────────────────────────────┘
```

定义好部署的目录结构

```txt
/
+- srv/
   +- awesome/       <-- Web App根目录
      +- www/        <-- 存放Python源码
      |  +- static/  <-- 存放静态资源文件
      +- log/        <-- 存放log
```

在服务器上部署，要考虑到新版本如果运行不正常，需要回退到旧版本时怎么办。每次用新的代码覆盖掉旧的文件是不行的，需要一个类似版本控制的机制。由于Linux系统提供了软链接功能，所以，把www作为一个软链接，它指向哪个目录，哪个目录就是当前运行的版本：

Nginx和python代码的配置文件只需要指向www目录即可

Nginx可以作为服务进程直接启动，但`app.py`还不行，[Supervisor](http://supervisord.org/)登场:管理进程的工具，可以随系统启动而启动服务,它还时刻监控服务进程，如果服务进程意外退出，Supervisor可以自动重启服务。

需要用到的服务:

* Nginx：高性能Web服务器+负责反向代理
* Supervisor：监控服务进程的工具
* MySQL：数据库服务

安装上述服务：`$ sudo apt-get install nginx supervisor python3 mysql-server`；安装Python库`$ sudo pip3 install jinja2 aiomysql aiohttp`；
初始化数据库：`$ mysql -u root -p < schema.sql`

#### 部署

用FTP还是SCP还是rsync复制文件？如果动复制，用一两次还行，一天如果部署50次不但慢、效率低，而且容易出错

正确的部署方式是使用工具配合脚本完成自动化部署。[Fabric](https://www.fabfile.org/)是一个自动化部署工具。由于Fabric是用Python 2.x开发的，所以，部署脚本要用Python 2.7来编写，本机还必须安装Python 2.7版本

本机（开发机器）安装Fabric `$ easy_install fabric`:`pip install fabric`(2.7`pip install fabric==1.14.0`);Linux服务器上不需要安装Fabric，Fabric使用SSH直接登录服务器并执行部署命令

编写部署脚本`fabfile.py`

```cmd
awesome-python-webapp/
+- fabfile.py
+- www/
+- ...
```

```py
# fabfile.py
# 设置部署时的变量
import os, re
from datetime import datetime

# 导入Fabric API:
from fabric.api import *

# 服务器登录用户名:
env.user = 'michael'
# sudo用户为root:
env.sudo_user = 'root'
# 服务器地址，可以有多个，依次部署:
env.hosts = ['192.168.0.3']

# 服务器MySQL用户名和口令:
db_user = 'www-data'
db_password = 'www-data'

###  编写打包的任务
_TAR_FILE = 'dist-awesome.tar.gz'
def build():
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))
### 

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/srv/awesome'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    # 解压到新目录:
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 重置软链接:
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s' % newdir)
    # 重启Python服务和nginx服务器:
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')
```

Fabric提供`local('...')`来运行本地命令，`with lcd(path)`可把当前命令的目录设定为`lcd()`指定的目录，注意Fabric只能运行命令行命令，Windows下可能需要[Cgywin](https://cygwin.com/)环境

打包:在`awesome-webapp`目录下运行：`$ fab build`;在`dist`目录下创建了`dist-awesome.tar.gz`

注意`run()`函数执行的命令是在服务器上运行，`with cd(path)`和`with lcd(path)`类似，把当前目录在服务器端设置为`cd()`指定的目录。如果一个命令需要sudo权限，就不能用`run()`，而是用`sudo()`来执行

#### 配置Supervisor

Supervisor只负责运行`app.py`,编写一个Supervisor的配置文件`awesome.conf`，存放到/`etc/supervisor/conf.d/`目录下：

```config
[program:awesome]

command     = /srv/awesome/www/app.py
directory   = /srv/awesome/www
user        = www-data
startsecs   = 3

redirect_stderr         = true
stdout_logfile_maxbytes = 50MB
stdout_logfile_backups  = 10
stdout_logfile          = /srv/awesome/log/app.log
```

配置文件通过`[program:awesome]`指定服务名为`awesome`，`command`指定启动`app.py`

```bash
$ sudo supervisorctl reload
$ sudo supervisorctl start awesome
$ sudo supervisorctl status
awesome                RUNNING    pid 1401, uptime 5:01:34
```

other :启动supervisord:`$ /usr/bin/python2 /usr/bin/supervisord -c /etc/supervisord.conf`
修改 `vi /etc/supervisord.conf`

```conf
[include]
files = supervisord.d/*.ini
files = supervisor/conf.d/*.conf # 增加的内容
```

#### 配置Nginx

把配置文件`awesome`放到`/etc/nginx/sites-available/`目录下

```config
server {
    listen      80; # 监听80端口

    root       /srv/awesome/www;
    access_log /srv/awesome/log/access_log;
    error_log  /srv/awesome/log/error_log;

    # server_name awesome.steven.com; # 配置域名

    # 处理静态文件/favicon.ico:
    location /favicon.ico {
        root /srv/awesome/www;
    }

    # 处理静态资源:
    location ~ ^\/static\/.*$ {
        root /srv/awesome/www;
    }

    # 动态请求转发到9000端口:
    location / {
        proxy_pass       http://127.0.0.1:9000;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

在`/etc/nginx/sites-enabled/`目录下创建软链接

```bash
$ pwd
/etc/nginx/sites-enabled
$ sudo ln -s /etc/nginx/sites-available/awesome .
# Nginx重新加载配置文件
$ sudo /etc/init.d/nginx reload
# udo service nginx {start|stop|restart|reload|force-reload|status|configtest|rotate|upgrade}
# sudo /usr/sbin/nginx -s  reload
```

如果有任何错误，都可在`/srv/awesome/log`查找Nginx和App的log。如果Supervisor启动时报错，可在`/var/log/supervisor`查看Supervisor的log
