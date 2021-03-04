import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    m_dict = {}
    n_dict = {}
    for i in range(len(magazine) if len(magazine) > len(note) else len(note)):
        if i < len(magazine):
            m_dict[magazine[i]] = 0
        if i < len(note):
            n_dict[note[i]] = 0
    for i in range(len(magazine) if len(magazine) > len(note) else len(note)):
        if i < len(magazine):
            m_dict[magazine[i]] += 1
        if i < len(note):
            n_dict[note[i]] += 1
    try:
        for w in note:
            if n_dict[w] <= m_dict[w]:
                pass
            else:
                print('No')
                break
        else:
            print('Yes')
    except:
        print('No')
    return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
