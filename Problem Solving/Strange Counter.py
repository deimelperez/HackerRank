import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.


def strangeCounter(t):
    if t <= 3:
        if t == 1:
            return 3
        if t == 2:
            return 2
        if t == 3:
            return 1
    tmp = 1
    for i in range(t):
        tmp += 3 * (2 ** i)
        if tmp <= t < tmp + 3 * (2 ** (i + 1)):
            result = 3 * (2 ** (i + 1)) - (t - tmp)
            return result


if __name__ == '__main__':
    t = int(input())

    result = strangeCounter(t)

    print(str(result) + '\n')
