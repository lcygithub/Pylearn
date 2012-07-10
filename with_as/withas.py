#-*- coding:utf8-*-
import sys
class test:
	def __enter__(self):
		print("enter")
	def __exit__(self,*args):
		print ("exit")

with test() as a:
	print "in with"
	
print "yes"