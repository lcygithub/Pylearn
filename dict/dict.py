#!/usr/bin/python
#-*- coding:utf8-*-
'''
字典

一.创建字典

方法①:
>>> dict1 = {}
>>> dict2 = {'name': 'earth', 'port': 80}
>>> dict1, dict2
({}, {'port': 80, 'name': 'earth'})

方法②:从Python 2.2 版本起
>>> fdict = dict((['x', 1], ['y', 2]))
>>> fdict
{'y': 2, 'x': 1}

方法③:

从Python 2.3 版本起, 可以用一个很方便的内建方法fromkeys() 来创建一个"默认"字典, 字
典中元素具有相同的值 (如果没有给出， 默认为None):
>>> ddict = {}.fromkeys(('x', 'y'), -1)
>>> ddict
{'y': -1, 'x': -1}
>>>
>>> edict = {}.fromkeys(('foo', 'bar'))
>>> edict
{'foo': None, 'bar': None}

二.如何访问字典中的值

①要想遍历一个字典(一般用键), 你只需要循环查看它的键, 像这样：
>>> dict2 = {'name': 'earth', 'port': 80}
>>>
>>>> for key in dict2.keys():
... print 'key=%s, value=%s' % (key, dict2[key])
...
key=name, value=earth
key=port, value=80

②从Python 2.2 开始
在 for 循环里遍历字典。
>>> dict2 = {'name': 'earth', 'port': 80}
>>>
>>>> for key in dict2:
... print 'key=%s, value=%s' % (key, dict2[key])
...
key=name, value=earth
key=port, value=80


要得到字典中某个元素的值， 可以用你所熟悉的字典键加上中括号来得到：
>>> dict2['name']
'earth'
>>>
>>> print 'host %s is running on port %d' % \
... (dict2['name'], dict2['port'])
host earth is running on port 80


③字典所有的方法。方法has_key()和 in 以及 not in 操作符都是布尔类型的
>>> 'server' in dict2 # 或 dict2.has_key('server')
False
>>> 'name' in dict # 或 dict2.has_key('name')
True
>>> dict2['name']
'earth'
一个字典中混用数字和字符串的例子：
>>> dict3 = {}
>>> dict3[1] = 'abc'
>>> dict3['1'] = 3.14159
>>> dict3[3.2] = 'xyz'
>>> dict3
{3.2: 'xyz', 1: 'abc', '1': 3.14159}


三.更新字典

采取覆盖更新
上例中 dict2['name']='earth';
更新 dict2['name']='abc';

四.删除字典元素和字典
del dict2['name'] # 删除键为“name”的条目
dict2.clear() # 删除dict2 中所有的条目
del dict2 # 删除整个dict2 字典
dict2.pop('name') # 删除并返回键为“name”的条目

dict2 = {'name': 'earth', 'port': 80}
>>> dict2.keys()
['port', 'name']
>>>
>>> dict2.values()
[80, 'earth']
>>>
>>> dict2.items()
[('port', 80), ('name', 'earth')]
>>>
>>> for eachKey in dict2.keys():
... print 'dict2 key', eachKey, 'has value', dict2[eachKey]
...
dict2 key port has value 80
dict2 key name has value earth


update()方法可以用来将一个字典的内容添加到另外一个字典中

{'server': 'http', 'port': 80, 'host': 'venus'}
>>> dict3.clear()
>>> dict3
>>> dict3


五.映射类型相关的函数

>>> dict(x=1, y=2)
{'y': 2, 'x': 1}
>>> dict8 = dict(x=1, y=2)
>>> dict8
{'y': 2, 'x': 1}
>>> dict9 = dict(**dict8)
>>> dict9
{'y': 2, 'x': 1}

dict9 = dict8.copy()

字典内建方法:

字典key值:dict9.keys()

字典值: dict9.values()

字典所有项:dict9.items()

返回字典值：dict9.get('y')

表 7.2 字典类型方法

方法名字        操作

dict.cleara() 删除字典中所有元素

dict.copya() 返回字典(浅复制)的一个副本

dict.fromkeysc(seq,val=None) c 创建并返回一个新字典，以seq 中的元素做该字典的键，val 做该字典中所有键对应的初始值(如果不提供此值，则默认为None)

dict.get(key,default=None)a 对字典dict 中的键key,返回它对应的值value，如果字典中不存在此键，则返回default 的值(注意，参数default 的默认值为None)

dict.has_key(key) 如果键(key)在字典中存在，返回True，否则返回False. 在Python2.2版本引入in 和not in 后，此方法几乎已废弃不用了，但仍提供一个
可工作的接口。

dict.items() 返回一个包含字典中(键, 值)对元组的列表

dict.keys() 返回一个包含字典中键的列表

dict.iter()d 方法iteritems(), iterkeys(), itervalues()与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表。

dict.popc(key[, default]) c 和方法get()相似，如果字典中key 键存在，删除并返回dict[key]，如果key 键不存在，且没有给出default 的值，引发KeyError 异常。

dict.setdefault(key,default=None)e 和方法set()相似，如果字典中不存在key 键，由dict[key]=default 为它赋值。

dict.update(dict2)a 将字典dict2 的键-值对添加到字典dict

dict.values() 返回一个包含字典中所有值的列表

①②③④⑤⑥⑦⑧⑨⑩
六.集合类型
①用集合的工厂方法 set()和 frozenset():
>>> s = set('cheeseshop')
>>> s
set(['c', 'e', 'h', 'o', 'p', 's'])
>>> t = frozenset('bookshop')
>>> t
frozenset(['b', 'h', 'k', 'o', 'p', 's'])
>>> type(s)
<type 'set'>
>>> type(t)
<type 'frozenset'>

②如何更新集合
用各种集合内建的方法和操作符添加和删除集合的成员:
>>> s.add('z')
>>> s
set(['c', 'e', 'h', 'o', 'p', 's', 'z'])
>>> s.update('pypi')
>>> s
set(['c', 'e', 'i', 'h', 'o', 'p', 's', 'y', 'z'])
>>> s.remove('z')
>>> s
set(['c', 'e', 'i', 'h', 'o', 'p', 's', 'y'])
>>> s -= set('pypi')
>>> s
set(['c', 'e', 'h', 'o', 's'])

③删除集合
del s

④成员关系 (in, not in)
>>> s = set('cheeseshop')
>>> t = frozenset('bookshop')
>>> 'k' in s
False
>>> 'k' in t
True
>>> 'c' not in t
True

⑤集合等价/不等价
>>> s == t
False
>>> s != t
True
>>> u = frozenset(s)
>>> s == u
True
>>> set('posh') == set('shop')
True

⑥差补/相对补集( – )
两个集合(s 和t)的差补或相对补集是指一个集合C，该集合中的元素，只属于集合s，而不属
于集合t。差符号有一个等价的方法，difference().
>>> s - t
set(['c', 'e'])

对称差分( ^ ):对称差分是集合的XOR


'''