import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    hg_sums = []
    for i in range(len(arr)):
        if i + 2 < len(arr):
            for j in range(len(arr)):
                if j + 2 < len(arr):
                    hg_sums.append(
                        sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]))
                else:
                    break
        else:
            break
    return max(hg_sums)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')
