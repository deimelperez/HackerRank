import math
import os
import random
import re
import sys

# Complete the serviceLane function below.


def serviceLane(width, cases):
    result = []
    for c in cases:
        result.append(min(width[c[0]:c[1] + 1]))
    return result


if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    print('\n'.join(map(str, result)))
