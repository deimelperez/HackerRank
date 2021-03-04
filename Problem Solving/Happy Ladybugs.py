import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.


def happyLadybugs(b):
    d = {}
    for letter in b:
        d[letter] = d.get(letter, 0) + 1
    if not d.get('_', 0):
        for i in range(len(b) - 1):
            if b[i] != b[i + 1]:
                if i + 2 < len(b):
                    if b[i + 2] != b[i + 1]:
                        return 'NO'
                else:
                    return 'NO'
    for letter in d:
        if d[letter] == 1 and letter != '_':
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result + '\n')
