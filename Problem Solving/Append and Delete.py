import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.


def appendAndDelete(s, t, k):
    size_s = len(s)
    size_t = len(t)
    steps = 0
    x = size_s if size_s > size_t else size_t
    if (s == t and (not k % 2 or k >= size_s)) or k >= (2 * x):
        return 'Yes'
    for i in range(0, size_s if size_s < size_t else size_t):
        if s[i] != t[i]:
            break
    else:
        if k % 2:
            return 'Yes'
    steps = size_s - i + size_t - i
    if k >= steps and not (k - steps) % 2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')
