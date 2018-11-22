"""finalmapper.py"""
import re
import sys

anagrams = {}
document = open("norvig.txt", "r")

for line in document:
    line = line.lower().strip()
    words = line.split()

    for word in words:
        word = re.sub('[^A-Za-z]', '', word)
        holder = sorted(list(word))
        holder = ''.join(holder)

        print('%s\t%s' % (holder, word))
