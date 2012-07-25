#!/usr/bin/python
#-*- coding:utf8-*-
list1 = [x*x for x in range(10)]
print list1
list2 = [x*x for x in range(10) if x % 3 == 0]
print list2
list3 = [(x,y) for x in range(10) for y in range(10)]
print list3
girls = ['alic','banbana','cedlenda']
boys = ['ard','bbss','ckjl']
list4 = [b+"+"+g for b in boys for g in girls if b[0] == g[0]]
print list4

letterGirls = {}
for girl in girls:
	letterGirls.setdefault(girl[0],[]).append(girl)
list4 = [b+"+"+g for b in boys for g in letterGirls[b[0]]]
print list4