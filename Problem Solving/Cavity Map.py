import math
import os
import random
import re
import sys

# Complete the cavityMap function below.


def cavityMap(grid):
    matrix = []
    deep = []
    for i, g in enumerate(grid):
        matrix.append([])
        for number in g:
            matrix[i].append(int(number))
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix) - 1):
            if matrix[i][j] > max(matrix[i - 1][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i][j - 1]):
                deep.append([i, j])
    for i, j in deep:
        matrix[i][j] = 'X'
    result = []
    tmp = ''
    for row in matrix:
        for r in row:
            tmp += str(r)
        result.append(tmp)
        tmp = ''
    return result


if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
