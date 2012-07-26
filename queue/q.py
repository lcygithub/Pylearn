#-*- coding:utf8-*-
from collections import deque
q = deque(range(10))
q.append(11)
q.appendleft(12)
print q
q.pop()
print q

q.popleft()
print q
q.rotate(3)
print q
q.rotate(-1)
print q