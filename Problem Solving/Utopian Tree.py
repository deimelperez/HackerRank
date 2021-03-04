import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):
    h = 1
    spring = True
    for _ in range(0, n):
        if spring:
            h *= 2
            spring = False
        else:
            h += 1
            spring = True
    return h


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result) + '\n')
