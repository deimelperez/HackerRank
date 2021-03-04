import math
import os
import random
import re
import sys

# Complete the larrysArray function below.


def larrysArray(A):
    total = 0
    for i in range(1, len(A) + 1):
        total += A.index(i)
        A.pop(A.index(i))
    if total % 2 == 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(result + '\n')
