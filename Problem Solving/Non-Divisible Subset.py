import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    rest = []
    cont = 0
    for x in s:
        rest.append(x % k)
    r = []
    for i in range(0, k):
        r.append(rest.count(i))
    if not k % 2:
        if r[k // 2]:
            cont += 1
    if r[0]:
        cont += 1
    for i in range(1, math.ceil(k / 2)):
        cont += r[i] if r[i] > r[k-i] else r[k-i]
    return cont


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')
