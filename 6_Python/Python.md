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
```