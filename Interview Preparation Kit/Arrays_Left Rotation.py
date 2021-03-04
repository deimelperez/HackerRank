import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    if d > len(a):
        d = d % len(a)
    for _ in range(d):
        x = a.pop(0)
        a.append(x)
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
