import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    cont = 0
    d = {}
    for ind, x in enumerate(arr):
        d[x] = ind
    for i in range(len(arr), 0, -1):
        index = d[i]
        if i - 1 != index:
            arr[index], arr[i - 1] = arr[i - 1], arr[index]
            d[i] = i - 1
            d[arr[index]] = index
            cont += 1
    return cont


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')
