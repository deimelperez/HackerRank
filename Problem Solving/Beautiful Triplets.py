import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.


def beautifulTriplets(d, arr):
    cont = 0
    tmp_j = 0
    tmp_k = 0
    for i in range(len(arr) - 2):
        if i < len(arr) + 2:
            if (arr[i] + d) in arr[i + 1:]:
                tmp_j = arr[i + 1:].count(arr[i] + d)
                if (arr[i] + 2 * d) in arr[i + 2:]:
                    tmp_k = arr[i + 2:].count(arr[i] + 2 * d)
                    cont += tmp_j * tmp_k
    return cont


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')
