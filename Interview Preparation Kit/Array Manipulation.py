import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    max_sum = 0
    sums = []
    x = 0
    for _ in range(n):
        sums.append(0)

    for q in queries:
        a, b, k = q[0], q[1], q[2]
        sums[a - 1] += k
        if b < n:
            sums[b] -= k

    for i in range(n):
        x += sums[i]
        max_sum = x if x > max_sum else max_sum
    return max_sum


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
