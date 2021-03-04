import math
import os
import random
import re
import sys

# Complete the stones function below.


def stones(n, a, b):
    result = []
    j = 0
    for i in range(n-1, 0, -1):
        result.append(a*i + b*j)
        j = j + 1
    j = 0
    for i in range(n-1, 0, -1):
        result.append(b*i + a*j)
        j = j + 1
    result = sorted(list(set(result)))
    return result


if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
