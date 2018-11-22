#!/usr/bin/env python
"""reducer.py"""
import sys
import re
from operator import itemgetter

reduced_anas = {}
for line in sys.stdin:
    wordList = re.sub("[^\w]", " ",  line.strip()).split()
    key, value = line.split('\t')
    if key not in reduced_anas:
        reduced_anas[key] = []
    if value not in reduced_anas[key]:
        reduced_anas[key].append(value)
for item in reduced_anas:
    if len(reduced_anas[item])>1:
        print('%s\t%s' % (item, ', '.join(reduced_anas[item])))
