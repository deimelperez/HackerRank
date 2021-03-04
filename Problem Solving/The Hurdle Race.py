import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.


def hurdleRace(k, height):
    x = max(height) - k
    if x > 0:
        return x
    else:
        return 0


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result) + '\n')
