#!/usr/bin/python
#-*- coding:utf8-*-
from heapq import *
from random import shuffle
data = range(10)
print data
print shuffle(data)
test = range(10)
heap = []
for n in data:
	heappush(heap,n)
print data
print heap
def pp(heap):
	print heappop(heap)
	print heap
for i in range(len(heap)):
	pp(heap)

heap = range(10)
print heap
print type(heap)
print heapify(heap)
print heap
print type(heap)

print heapreplace(heap,90)
print heap
