import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.


def beautifulDays(i, j, k):
    days = range(i, j + 1)
    cont = 0
    for d in days:
        if not (d - int(str(d)[::-1])) % k:
            cont += 1
    return cont


if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')
