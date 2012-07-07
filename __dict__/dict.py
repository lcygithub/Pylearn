#-*- coding:utf8-*-
class A(object):
	a = 10

o1 = A()
o2 = A()
print o1.a,o2.a,A.a
print o1.__dict__,o2.__dict__,A.__dict__

o1.a += 2
o1.b = 0
print o1.a,o2.a,A.a,o1.b
print o1.__dict__,o2.__dict__,A.__dict__

A.a += 3
o1.b += 1
print o1.a,o2.a,A.a,o1.b
print o1.__dict__,o2.__dict__,A.__dict__