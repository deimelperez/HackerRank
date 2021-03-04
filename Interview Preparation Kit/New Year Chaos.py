import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    cont = 0
    for i in range(len(q), 0, -1):
        if i > 0 and i == q[i - 1]:
            pass
        elif i > 1 and i == q[i - 2]:
            q[i - 1], q[i - 2] = q[i - 2], q[i - 1]
            cont += 1
        elif i > 2 and i == q[i - 3]:
            q[i - 3], q[i - 2], q[i - 1] = q[i - 2], q[i - 1], q[i - 3]
            cont += 2
        else:
            print('Too chaotic')
            return
    print(cont)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
