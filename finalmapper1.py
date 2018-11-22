#!/usr/bin/env python
"""finalmapper.py"""
import re
import sys
document = open("norvig.txt", "r")
anagrams = {}
for line in document:
    line = re.sub("[,.]", " ", line)
    line = line.lower().strip()
    words = line.split()

    for word in words:
        word = re.sub('[^A-Za-z]', '', word)
        holder = sorted(list(word))
        holder = ''.join(holder)
        print('%s\t%s' % (holder, word))
