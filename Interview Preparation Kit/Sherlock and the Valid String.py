import math
import os
import random
import re
import sys

# Complete the isValid function below.


def isValid(s):
    s_dict = {}
    for letter in s:
        s_dict[letter] = s_dict.get(letter, 0) + 1
    count = {}
    for letter in s_dict:
        count[s_dict[letter]] = count.get(s_dict[letter], 0) + 1
    if len(count) > 2:
        return 'NO'
    elif len(count) == 2:
        x, y = count.values()
        if x != 1 and y != 1:
            return 'NO'
        else:
            k1, k2 = count.keys()
            if abs(k1 - k2) != 1 and not ((k1 == 1 and x == 1) or (k2 == 1 and y == 1)):
                return 'NO'
            else:
                return 'YES'
    else:
        return 'YES'


if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result + '\n')
