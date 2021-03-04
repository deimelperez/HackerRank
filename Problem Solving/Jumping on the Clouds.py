import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    cont = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 >= len(c):
            cont += 1
            break
        if c[i + 2] == 0:
            cont += 1
            i += 2
        else:
            cont += 2
            i += 3
    return cont


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
