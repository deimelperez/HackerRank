import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.


def angryProfessor(k, a):
    a.sort()
    early = 0
    for x in a:
        if x > 0:
            break
        else:
            early += 1
    if early < k:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result + '\n')
