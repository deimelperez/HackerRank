import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    a_dict = {}
    b_dict = {}
    cont = 0
    for i in range(len(a) if len(a) > len(b) else len(b)):
        if i < len(a):
            a_dict[a[i]] = a_dict.get(a[i], 0) + 1
        if i < len(b):
            b_dict[b[i]] = b_dict.get(b[i], 0) + 1
    for letter in a_dict:
        cont += abs(a_dict.get(letter, 0) - b_dict.get(letter, 0))
        a_dict[letter] = 0
        b_dict[letter] = 0
    for letter in b_dict:
        cont += b_dict[letter]
    return cont


if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')
