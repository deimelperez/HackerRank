import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):
    minn = abs(arr[0] - arr[1])
    arr.sort()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < minn:
            minn = abs(arr[i] - arr[i + 1])
    return minn


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
