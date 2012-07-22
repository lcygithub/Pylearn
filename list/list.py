#!/usr/bin/python
#-*- coding:utf8-*-

# 产生一个数值递增列表
num_inc_list = range(30)
print num_inc_list

# 用某个固定值初始化列表
initial_value = 0
list_lenght = 5
sample_list = [ initial_value for i in range(10)]
sample_list = sample_list*list_lenght
print sample_list