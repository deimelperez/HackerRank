import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.


def absolutePermutation(n, k):


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))
