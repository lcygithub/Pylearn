#!/usr/bin/python
#-*- coding:utf8-*-
print set([0,1,2,3,4,4,56,78,4])
print set(['abc','sdf','fgdg','fggfgfg'])

a = set([1,2,3])
b = set([2,3,4])
print a.union(b)

c = a&b
d = a | b
print c
print d
print c.issuperset(a)
print a.issuperset(c)
print d.issuperset(a)

print a,b
print a.intersection(b)
print a.difference(b)
print b.difference(a)

print "a - b:",
print a - b

print a.symmetric_difference(b)
print a ^ b

print a.copy()
print a is a
print a.copy() is a