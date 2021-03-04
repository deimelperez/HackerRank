import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.


def kaprekarNumbers(p, q):
    cont = 0
    for i in range(p, q + 1):
        if i < 10:
            if i == 1 or i == 9:
                print(1 if i == 1 else 9, end=' ')
        else:
            numb = str(i ** 2)
            l = numb[0:len(numb) // 2]
            a = math.ceil(len(numb) / 2)
            r = numb[len(numb) - a:]
            x = int(l) + int(r)
            if x == i:
                cont += 1
                print(i, end=' ')
    if cont == 0:
        print('INVALID RANGE')
    return


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
