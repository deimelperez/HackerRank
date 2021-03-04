import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    deletions = 0
    tmp = 'A' if s[0] == 'B' else 'B'
    for letter in s:
        if tmp == letter:
            deletions += 1
        else:
            tmp = letter
    return deletions


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')
