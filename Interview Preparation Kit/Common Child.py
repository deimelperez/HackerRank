import math
import os
import random
import re
import sys

# Complete the commonChild function below.


def commonChild(s1, s2):
    L = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                L[i + 1][j + 1] = 1 + L[i][j]
            else:
                L[i + 1][j + 1] = L[i + 1][j] if L[i +
                                                   1][j] > L[i][j + 1] else L[i][j + 1]
    return L[-1][-1]


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(str(result) + '\n')
