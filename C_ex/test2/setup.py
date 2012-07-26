#!/usr/bin/python
#-*- coding:utf8-*-
from distutils.core import setup,Extension
module = Extension("wrap",sources = ['src/wrap.c'])
setup (
	name = "wrap",
	version = "1.0",
	ext_modules = [module]
	)