#!/usr/bin/python
#-*- coding:utf8-*-
from distutils.core import setup,Extension

module = Extension("jie",sources = ['src/jiecheng.c'])
setup (
	name = "jiecheng",
	version = "1.0",
	description = "this is jiecheng py",
	ext_modules = [module]
	)