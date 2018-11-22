"""reducer.py"""
import sys
import re
from operator import itemgetter

reduced_anas = {}
unique_anagrams = []

for line in sys.stdin:
    wordList = re.sub("[^\w]", " ",  line.strip()).split()
    print (wordList)
    key = wordList[0]
    if key not in reduced_anas:
        reduced_anas[key] = []

    for i in range(1, len(wordList)):
        if wordList[i] not in reduced_anas[key]:
            reduced_anas[key].append(wordList[i])

for item in reduced_anas:
    print('%s\t%s' % (item, ', '.join(reduced_anas[item])))
