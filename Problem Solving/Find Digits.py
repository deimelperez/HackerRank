import math
import os
import random
import re
import sys

# Complete the findDigits function below.


def findDigits(n):
    x = str(n)
    cont = 0
    for num in x:
        if int(num) != 0:
            if not n % int(num):
                cont += 1
    return cont


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')
