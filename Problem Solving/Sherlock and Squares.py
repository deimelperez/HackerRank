import math
import os
import random
import re
import sys

# Complete the squares function below.


def squares(a, b):
    cont = 0
    r = range(a, b + 1)
    for i in r:
        x = math.sqrt(i)
        if x.is_integer():
            cont += 1
            break
    cond = True
    while cond:
        x += 1
        if x ** 2 <= b:
            cont += 1
        else:
            cond = False
    return cont


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(str(result) + '\n')
