import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    a = s.count('a')
    count = a * (n // len(s)) + s[0:n % len(s)].count('a')
    return count


if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
