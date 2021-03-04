import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.


def circularArrayRotation(a, k, queries):
    if k > len(a):
        k = k % len(a)
    for _ in range(k):
        x = a.pop()
        a.insert(0, x)
    r = []
    for q in queries:
        r.append(a[q])
    return r


if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))
