import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.


def activityNotifications(expenditure, d):
    count = 0
    x = sorted(expenditure[:d - 1])
    for i in range(d, len(expenditure)):
        bisect.insort_right(x, expenditure[i - 1])
        if not d % 2:
            if expenditure[i] >= (x[d // 2 - 1] + x[d // 2]):
                count += 1
        else:
            if expenditure[i] >= 2 * x[d // 2]:
                count += 1
        x.pop(bisect.bisect_left(x, expenditure[i - d]))
    return count


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
