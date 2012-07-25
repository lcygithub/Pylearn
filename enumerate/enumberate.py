#!/usr/bin/python
#-*- coding:utf8-*-
strings = ["xxxx",'adf','asdfasdf']
for string in strings:
	if "xxxx" in string:
		index = strings.index(string)
		strings[index] = '[censored]'
print strings
print index
testlist = [1,12,23,32,3,4]
index = testlist.index(12)
print index
strings = ["xxxx",'adf','asdfasdf']
for index,string in enumerate(strings):
	if "xxxx" in string:
		strings[index] = '[centored]'
print index
print strings
print enumerate(strings)

'''
    enumerate(iterable[, start]) -> iterator for index, value of iterable
    
    Return an enumerate object.  iterable must be another object that supports
    iteration.  The enumerate object yields pairs containing a count (from
    start, which defaults to zero) and a value yielded by the iterable argument.
    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

'''