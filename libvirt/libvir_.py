#!/usr/bin/python
#-*- coding:utf8-*-
import libvirt
import sys

conn = libvirt.openReadOnly(None)
if conn == None:
    print "fail to open connection"
    sys.exit(1)

try:
    dom0 = conn.lookupByName("Domain-0")
except:
    print "fail to find the main domain"
    sys.exit(1)

print "Domain 0:id %d running %s" % (dom0.ID(), dom0.OSType())
print dom0.info()
