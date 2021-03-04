import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    m_dict = {}
    n_dict = {}
    for i in range(len(s1) if len(s1) > len(s2) else len(s2)):
        if i < len(s1):
            m_dict[s1[i]] = 1
        if i < len(s2):
            n_dict[s2[i]] = 1

    for w in s1:
        try:
            if n_dict[w] == m_dict[w]:
                return 'YES'
        except:
            pass
    else:
        return 'NO'
    return


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result + '\n')
