#-*- coding:utf8-*-
import os
list = os.listdir(os.getcwd())
for file in list:
	now = os.getcwd() + "/" + file
	print now
	if not os.path.isdir(now):
		os.system("enca -L zh_CN -x GB2312 " + file)