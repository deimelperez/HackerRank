import os
import sys

#
# Complete the pageCount function below.
#


def pageCount(n, p):
    #
    # Write your code here.
    #
    if p == 1 or p == n or (p == n - 1 and n % 2):
        return 0
    result1 = 1
    for i in range(2, n, 2):
        if p in [i, i + 1]:
            break
        result1 += 1
    result2 = 0
    if not n % 2:
        n -= 1
        result2 = 1
    for i in range(n, 0, -2):
        if p in [i, i - 1]:
            break
        result2 += 1
    if result1 > result2:
        return result2
    else:
        return result1


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
