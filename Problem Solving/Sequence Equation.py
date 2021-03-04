import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.


def permutationEquation(p):
    r = []
    for i in range(1, len(p) + 1):
        r.append(p.index(p.index(i) + 1) + 1)
    return r


if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))
