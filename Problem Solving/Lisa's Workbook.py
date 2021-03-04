import math
import os
import random
import re
import sys

# Complete the workbook function below.


def workbook(n, k, arr):
    problem = 1
    page = []
    count = 0
    for i in range(n):
        while arr[i] > k:
            page.append([i for i in range(problem, problem + k)])
            problem += k
            arr[i] -= k
        page.append([i for i in range(problem, problem + arr[i])])
        problem = 1
    for i in range(len(page)):
        if i + 1 in page[i]:
            count += 1
    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(str(result) + '\n')
