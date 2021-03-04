import math
import os
import random
import re
import sys

# Complete the maxMin function below.


def maxMin(k, arr):
    arr.sort()
    unf = arr[-1] - arr[0]
    for i in range(len(arr) - k + 1):
        tmp = [arr[i], arr[i + k - 1]]
        if tmp[1] - tmp[0] < unf:
            unf = tmp[1] - tmp[0]
    return unf


if __name__ == '__main__':
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result) + '\n')
