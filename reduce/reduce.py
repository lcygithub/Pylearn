#!/usr/bin/python
#-*- coding:utf8-*-
print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
'''
Type:		builtin_function_or_method
Base Class:	<type 'builtin_function_or_method'>
String Form:	<built-in function reduce>
Namespace:	Python builtin
Docstring:
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
'''