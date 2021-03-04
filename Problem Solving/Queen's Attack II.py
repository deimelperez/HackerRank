import math
import os
import random
import re
import sys

# Complete the queensAttack function below.


def queensAttack(n, k, r_q, c_q, obstacles):
    steps = 0
    obst_row_p = [item for item in obstacles if r_q ==
                  item[0] and c_q < item[1]]
    obst_row_n = [item for item in obstacles if r_q ==
                  item[0] and c_q > item[1]]
    obst_col_p = [item for item in obstacles if c_q ==
                  item[1] and r_q < item[0]]
    obst_col_n = [item for item in obstacles if c_q ==
                  item[1] and r_q > item[0]]
    obst_l_r_p = [item for item in obstacles if r_q - item[0] ==
                  -1 * (c_q - item[1]) and r_q < item[0]]
    obst_l_r_n = [item for item in obstacles if r_q - item[0] ==
                  -1 * (c_q - item[1]) and r_q > item[0]]
    obst_r_l_p = [item for item in obstacles if r_q - item[0] ==
                  c_q - item[1] and r_q < item[0]]
    obst_r_l_n = [item for item in obstacles if r_q - item[0] ==
                  c_q - item[1] and r_q > item[0]]

    obst_row_p.sort(key=lambda item: item[1])
    obst_row_n.sort(key=lambda item: item[1], reverse=True)
    obst_col_p.sort(key=lambda item: item[0])
    obst_col_n.sort(key=lambda item: item[0], reverse=True)
    obst_l_r_p.sort(key=lambda item: item[0])
    obst_l_r_n.sort(key=lambda item: item[0], reverse=True)
    obst_r_l_p.sort(key=lambda item: item[0])
    obst_r_l_n.sort(key=lambda item: item[0], reverse=True)

    if obst_row_p:
        steps += obst_row_p[0][1] - c_q - 1
    else:
        steps += n - c_q

    if obst_row_n:
        steps += c_q - obst_row_n[0][1] - 1
    else:
        steps += c_q - 1

    if obst_col_p:
        steps += obst_col_p[0][0] - r_q - 1
    else:
        steps += n - r_q

    if obst_col_n:
        steps += r_q - obst_col_n[0][0] - 1
    else:
        steps += r_q - 1

    if obst_l_r_p:
        steps += obst_l_r_p[0][0] - r_q - 1
    else:
        steps += n - r_q if n - r_q < c_q - 1 else c_q - 1

    if obst_l_r_n:
        steps += r_q - obst_l_r_n[0][0] - 1
    else:
        steps += r_q - 1 if r_q - 1 < n - c_q else n - c_q

    if obst_r_l_p:
        steps += obst_r_l_p[0][0] - r_q - 1
    else:
        steps += n - r_q if n - r_q < n - c_q else n - c_q

    if obst_r_l_n:
        steps += r_q - obst_r_l_n[0][0] - 1
    else:
        steps += r_q - 1 if r_q - 1 < c_q - 1 else c_q - 1

    return steps


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
