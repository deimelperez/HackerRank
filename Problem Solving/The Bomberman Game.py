import math
import os
import random
import re
import sys

# Complete the bomberMan function below.


def bomberMan(n, grid):
    result = []
    if n == 0 or n == 1:
        return grid
    if n % 2 == 0:
        for _ in grid:
            result.append(''.join(['O' for _ in range(len(grid[0]))]))
        return result
    third = []
    for _ in grid:
        third.append(['O' for _ in range(len(grid[0]))])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                if i - 1 >= 0:
                    third[i - 1][j] = '.'
                if j - 1 >= 0:
                    third[i][j - 1] = '.'
                if i + 1 < len(grid):
                    third[i + 1][j] = '.'
                if j + 1 < len(grid[0]):
                    third[i][j + 1] = '.'
                third[i][j] = '.'
    fifth = []
    for _ in grid:
        fifth.append(['O' for _ in range(len(grid[0]))])
    for i in range(len(grid)):
        for j in range(len(third[0])):
            if third[i][j] == 'O':
                if i - 1 >= 0:
                    fifth[i - 1][j] = '.'
                if j - 1 >= 0:
                    fifth[i][j - 1] = '.'
                if i + 1 < len(grid):
                    fifth[i + 1][j] = '.'
                if j + 1 < len(grid[0]):
                    fifth[i][j + 1] = '.'
                fifth[i][j] = '.'
    if (n - 3) % 4 == 0:
        for i, row in enumerate(third):
            third[i] = ''.join(row)
        return third
    if (n - 5) % 4 == 0:
        for i, row in enumerate(fifth):
            fifth[i] = ''.join(row)
        return fifth


if __name__ == '__main__':
    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print('\n'.join(result))
