import math
import os
import random
import re
import sys

# Complete the encryption function below.


def encryption(s):
    s = s.replace(' ', '')
    l = len(s)
    c = math.ceil(math.sqrt(l))
    m_letters = []
    for i in range(0, l, c):
        if i + c > l:
            m_letters.append(s[i:])
        else:
            m_letters.append(s[i:i+c])
    result = []
    for i in range(c):
        result.append([])

    for s in m_letters:
        for i, l in enumerate(s):
            result[i].append(l)
    for i in range(c):
        result[i] = ''.join(result[i])
    result = ' '.join(result)
    return result


if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result + '\n')
