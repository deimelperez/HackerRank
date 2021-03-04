import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    a.sort()
    r = []
    for i in range(0, len(a)):
        cont = 0
        tmp = a[i]
        for x in a:
            if 0 <= (tmp - x) <= 1:
                cont += 1
        r.append(cont)
    return max(r)


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
