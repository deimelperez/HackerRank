import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sherlockAndAnagrams(s):
    cont = 0
    d = {}

    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            d[s[j:j + i]] = d.get(s[j:j + i], 0) + 1
    an = {}
    for x in d:
        h = ''
        y = list(x)
        y.sort()
        for l in y:
            h = h + l
        an[h] = an.get(h, 0) + d[x]
    for l in an:
        if an[l] > 1:
            cont += factorial(an[l]) // (factorial(an[l] - 2) * 2)

    return cont


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')
