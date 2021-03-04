import math
import os
import random
import re
import sys

# Complete the fairRations function below.


def fairRations(B):
    count = 0
    check = False
    imp = 0
    for b in B:
        if b % 2:
            check = not check
            imp += 1
        if check:
            count += 1
    if imp % 2 == 0:
        return count * 2
    else:
        return 'NO'


if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(str(result) + '\n')
