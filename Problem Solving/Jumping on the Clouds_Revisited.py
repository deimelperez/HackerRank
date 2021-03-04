import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    e = 100
    cond = True
    i = 0
    if k > len(c):
        k = k % len(c)

    while cond:
        i += k
        if i >= len(c):
            i -= len(c)
        if c[i] == 0:
            e -= 1
        else:
            e -= 3
        if i == 0:
            cond = False
    return e


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result) + '\n')
