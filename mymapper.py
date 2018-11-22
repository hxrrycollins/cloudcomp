#!/usr/bin/env python
"""mapper.py"""
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
        if (holder not in anagrams):
            anagrams[holder]=[word]
        else:
            if word not in anagrams[holder]:
                anagrams[holder].append(word)

for item in anagrams:
    print('%s, %s' % (item, ', '.join(anagrams[item])))