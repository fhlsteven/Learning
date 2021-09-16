# Python Grammar

## 输入输出

* 输入 `inpput()`

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

* 


