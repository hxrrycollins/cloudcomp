#!/usr/bin/env python 
"""finalmapper.py"""
import re
import sys

anagrams = {}
for line in sys.stdin:
    line = line.lower().strip()
    words = line.split()
    for word in words:
        word = re.sub('[^A-Za-z]', '', word)
        holder = sorted(list(word))
        holder = ''.join(holder)
        print('%s\t%s' % (holder, word))
