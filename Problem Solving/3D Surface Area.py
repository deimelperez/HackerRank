import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.


def surfaceArea(A):
    area = 2 * (len(A) * len(A[0]))
    front_area = 0
    side_area = 0
    for i in range(len(A)):
        front_area += A[i][0]
        for j in range(len(A[0]) - 1):
            front_area += (A[i][j + 1] - A[i][j]
                           ) if A[i][j + 1] - A[i][j] > 0 else 0
    for i in range(len(A[0])):
        side_area += A[0][i]
        for j in range(len(A) - 1):
            side_area += (A[j + 1][i] - A[j][i]) if A[j +
                                                      1][i] - A[j][i] > 0 else 0

    area += 2 * front_area + 2 * side_area
    return area


if __name__ == '__main__':
    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(str(result) + '\n')
