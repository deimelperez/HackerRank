import math
import os
import random
import re
import sys

# Complete the howManyGames function below.


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    cont = 0
    if s > p:
        while s > p:
            s -= p
            cont += 1
            if p > m:
                p -= d
            if p <= m:
                cont += s // m
                # if not s % m:
                #     cont -= 1
                break
    return cont


if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(str(answer) + '\n')
