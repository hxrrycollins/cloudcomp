"""mapper.py"""
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
        if (holder not in anagrams):
            anagrams[holder]=[word]
        else:
            if word not in anagrams[holder]:
                anagrams[holder].append(word)

for item in anagrams:
    if len(anagrams[item][0])>0:
        print('%s\t%s' % (item, ', '.join(anagrams[item])))
