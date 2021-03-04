import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(s):
    b = True
    level = 0
    count = 0
    for letter in s:
        if letter == 'U':
            level += 1
        else:
            level -= 1
        if level < 0:
            if b:
                count += 1
                b = False
        else:
            b = True
    return count


if __name__ == '__main__':
    s = input()

    result = countingValleys(s)

    print(str(result) + '\n')
