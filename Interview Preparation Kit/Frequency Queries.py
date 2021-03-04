import math
import os
import random
import re
import sys

# Complete the freqQuery function below.


def freqQuery(queries):
    count = {}
    my_d = {}
    r = []
    for q in queries:
        if q[0] == 1:
            my_d[q[1]] = my_d.get(q[1], 0) + 1
            count[my_d[q[1]]] = count.get(my_d[q[1]], 0) + 1
            count[my_d[q[1]] - 1] = (count.get(my_d[q[1]] - 1, 0) -
                                     1) if (count.get(my_d[q[1]] - 1, 0) - 1) > 0 else 0
        elif q[0] == 2:
            if my_d.get(q[1], 0):
                my_d[q[1]] -= 1
                count[my_d[q[1]]] = count.get(my_d[q[1]], 0) + 1
                count[my_d[q[1]] + 1] = (count.get(my_d[q[1]] + 1, 0) - 1) if (
                    count.get(my_d[q[1]] + 1, 0) - 1) > 0 else 0
            else:
                my_d[q[1]] = 0
        elif q[0] == 3:
            if count.get(q[1], 0) > 0:
                r.append(1)
            else:
                r.append(0)
    return r


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
