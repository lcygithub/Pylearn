#-*- coding:utf8-*-
# class FooParent:
# 	def bar(self,message):
# 		print message

# class FooChild(FooParent):
# 	def bar(self,message):
# 		# FooParent.bar(self,message)
# 		s = super(FooChild,self)
# 		s.bar(message)
# _metaclass = type
class A(object):
	def __init__(self):
		print "enter A"
		print "leave A"
class B(A):
	def __init__(self):
		print "enter B"
		# A.__init__(self)
		super(B,self).__init__()
		print "leave B"
class C(A):
	def __init__(self):
		print "enter C"
		# A.__init__(self)
		super(C,self).__init__()
		print "leave C"
class D(A):
	def __init__(self):
		print "enter D"
		# A.__init__(self)
		super(D,self).__init__()
		print "leave D"
class E(B,C,D):
	def __init__(self):
		print "enter E"
		# B.__init__(self)
		# C.__init__(self)
		# D.__init__(self)
		super(E,self).__init__()
		print "leave E"
# enter E
# enter B
# enter C
# enter D
# enter A
# leave A
# leave D
# leave C
# leave B
# leave E
