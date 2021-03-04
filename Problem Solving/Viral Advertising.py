import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    p = 2
    cumulative = 2
    for _ in range(n-1):
        p = 3 * p // 2
        cumulative += p
    return cumulative


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')
