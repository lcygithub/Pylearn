#!/usr/bin/python
#-*- coding:utf8-*-
from distutils.core import setup,Extension 
 
module1 = Extension('spam',sources=['src/spammodule.c']) 
 
setup ( name = 'spam',
	version = '1.0',
	description = 'Tthis is a demo package',
	ext_modules = [module1])