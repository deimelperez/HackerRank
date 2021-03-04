import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    tmp_arr = sorted(list(set(arr)))
    result = []
    i = 0
    x = len(arr)
    for i in range(0, len(tmp_arr)):
        result.append(x)
        x -= arr.count(tmp_arr[i])
    return result


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
