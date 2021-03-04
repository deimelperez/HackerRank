#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def setPassword(x):
    hsh = 0
    for i, letter in enumerate(x):
        hsh += ord(letter) * 131 ** (len(x) - i - 1)
    hsh %= 1000000007
    return hsh


def authorize(x, psw, hsh):
    x = int(x)
    if x == hsh:
        return 1
    else:
        for letter in letters:
            hsh = setPassword(psw + letter)
            if x == hsh:
                return 1
        else:
            return 0


def authEvents(events):
    # Write your code here
    l = []
    for event in events:
        if event[0] == 'setPassword':
            hsh = setPassword(event[1])
            psw = event[1]
        else:
            l.append(authorize(event[1], psw, hsh))
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
