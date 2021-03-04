import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.


def equalizeArray(arr):
    x = list(set(arr))
    d = []
    for number in x:
        d.append([number, arr.count(number)])
    d.sort(key=lambda item: item[1], reverse=True)
    return len(arr) - d[0][1]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result) + '\n')
