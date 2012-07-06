#-*- coding:utf8-*-
class MyClass():
	count = 0
	def __init__(self):
		print "this is init"
		self.count = 0
	def p1():
		print "this is p1()"

	def p2(self):
		self.count += 1
		print "self count:%d"%self.count

	@classmethod
	def p3(cls):
		cls.count += 1
		print "csl count:%d"%cls.count

	@staticmethod
	def p4():
		print "staticmethod"

	# def p5(self):
	# 	print "this is p5()"

	# @ p5
	# def p6(self):
	# 	print "this is p6()"