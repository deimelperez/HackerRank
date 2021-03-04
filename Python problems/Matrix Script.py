import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

sentence_l = []

for i in range(len(matrix[0])):
    for el in matrix:
        sentence_l.append(el[i])


char = ''.join(sentence_l)
translation = char.maketrans('!@#$%&', '      ')
s = char.translate(translation).split()
try:
    last_word = s[-1]
    final = char[char.rfind(last_word) + len(last_word):]
except:
    final = ''

try:
    first_word = s[0]
    beg = char[:char.find(first_word)]
except:
    beg = ''
sentence = beg + ' '.join(s) + final
try:
    sentence[1]
except:
    sentence = char
print(sentence)
