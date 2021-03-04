import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.


def minimumDistances(a):
    dist = []
    for i, x in enumerate(a):
        if x in a[i + 1:]:
            dist.append(a[i + 1:].index(x) + 1)
    if dist:
        return min(dist)
    return -1


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
