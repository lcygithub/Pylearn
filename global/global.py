#!/usr/bin/python
#-*- coding:utf8-*-
# global _rank
CONSTANT = 0

def modifyConstant(test):
	# print test
	global CONSTANT
	CONSTANT += 1
	print CONSTANT
	return CONSTANT
if __name__ == "__main__":
	ts = map(modifyConstant,range(10))
	print ts