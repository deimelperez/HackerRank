import math
import os
import random
import re
import sys

# Complete the twoPluses function below.\


def plus(grid):
    bigger = 1
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == 'G':
                up = 0
                down = 0
                right = 0
                left = 0
                for k in range(i - 1, -1, -1):
                    if grid[k][j] == 'G':
                        up += 1
                    else:
                        break

                for k in range(i + 1, len(grid)):
                    if grid[k][j] == 'G':
                        down += 1
                    else:
                        break

                for k in range(j - 1, -1, -1):
                    if grid[i][k] == 'G':
                        left += 1
                    else:
                        break

                for k in range(j + 1, len(grid[0])):
                    if grid[i][k] == 'G':
                        right += 1
                    else:
                        break
                area = 1 + 4 * min(up, down, left, right)
                if area > bigger:
                    bigger = area
    return bigger


def twoPluses(grid):
    result = 1

    for i, row in enumerate(grid):
        grid[i] = list(row)
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == 'G':
                up = 0
                down = 0
                right = 0
                left = 0
                for k in range(i - 1, -1, -1):
                    if grid[k][j] == 'G':
                        up += 1
                    else:
                        break

                for k in range(i + 1, len(grid)):
                    if grid[k][j] == 'G':
                        down += 1
                    else:
                        break

                for k in range(j - 1, -1, -1):
                    if grid[i][k] == 'G':
                        left += 1
                    else:
                        break

                for k in range(j + 1, len(grid[0])):
                    if grid[i][k] == 'G':
                        right += 1
                    else:
                        break

                lon = min(up, down, left, right)
                while lon > 0:
                    h = []
                    for row in grid:
                        h.append(list(row))
                    for k in range(lon + 1):
                        h[i - k][j] = 'X'
                        h[i + k][j] = 'X'
                        h[i][j - k] = 'X'
                        h[i][j + k] = 'X'
                        h[i][j] = 'X'
                    smaller = plus(h)
                    area = smaller * (1 + 4 * lon)
                    if area > result:
                        result = area
                    lon -= 1

    return result


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(str(result) + '\n')
