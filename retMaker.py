#!/usr/bin/python
import string
import sys

addr = sys.argv[1]

addr = str(addr)

fb = addr[0:2]
sb = addr[2:4]
tb = addr[4:6]
fob = addr[6:8]

if len(addr) == 8:
    print "\\x" + fob + "\\x" + tb + "\\x" + sb + "\\x" + fb
else:
    print "Nope, that was bad input."
