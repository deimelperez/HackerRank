import math
import os
import random
import re
import sys
import bisect

# Complete the flatlandSpaceStations function below.


def flatlandSpaceStations(n, c):
    distance = 0
    c.sort()
    for i in range(n):
        space_station = bisect.bisect_left(c, i)
        space_station = space_station if space_station < len(c) else 0
        if min(abs(i - c[space_station]), abs(i - c[space_station - 1])) > distance:
            distance = min(abs(i - c[space_station]),
                           abs(i - c[space_station - 1]))
    return distance


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result) + '\n')
