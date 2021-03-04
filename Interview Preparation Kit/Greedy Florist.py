import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k, c):
    price = 0
    tmp = 0
    c.sort(reverse=True)
    for i in range(len(c) // k + 1):
        for j in range(k):
            if tmp + j < len(c):
                price += ((i + 1) * c[tmp + j])
            else:
                break
        tmp = tmp + k
    return price


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(str(minimumCost) + '\n')
