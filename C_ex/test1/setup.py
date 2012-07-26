#!/usr/bin/python
#-*- coding:utf8-*-
from distutils.core import setup,Extension

module = Extension('compare',sources = ['src/comp.c'])
setup (name = "compare",
	version = "1.0",
	description = "this is a compare func",
	ext_modules = [module])