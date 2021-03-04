import sys
import re
import random
import os
import math


# Complete the chocolateFeast function below.

def chocolateFeast(n, c, m):
    w = n // c
    count = w
    while w >= m:
        count += w // m
        rest = w % m
        w = rest + w // m
    return count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        print(str(result) + '\n')
