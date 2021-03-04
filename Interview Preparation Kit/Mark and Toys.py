import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    for p in prices:
        if k > p:
            count += 1
            k -= p
        else:
            break
    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')
