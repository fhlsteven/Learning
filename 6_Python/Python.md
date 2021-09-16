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

* 浮点数： 
