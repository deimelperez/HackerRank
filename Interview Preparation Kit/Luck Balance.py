import math
import os
import random
import re
import sys

# Complete the luckBalance function below.


def luckBalance(k, contests):
    important = []
    others = []
    for c in contests:
        if c[1]:
            important.append(c[0])
        else:
            others.append(c[0])
    important.sort()
    if k < len(important):
        important_win = important[0:len(important) - k]
        important_lose = important[len(important) - k:]
    else:
        important_lose = important
        important_win = [0, ]
    luck = sum(others) + sum(important_lose) - sum(important_win)
    return luck


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')
