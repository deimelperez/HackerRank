import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(ar):
    colors = list(set(ar))
    count = 0
    for i in range(0, len(colors)):
        count += ar.count(colors[i]) // 2
        print(ar.count(colors[i]) // 2)
    return count


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    print(result)
