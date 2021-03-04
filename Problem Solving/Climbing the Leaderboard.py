import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    r = []
    s = [[x, y]
         for x, y in zip(sorted(list(set(scores))), range(len(list(set(scores))), 0, -1))]
    tmp = 0
    for a in alice:
        for i in range(tmp, len(s)):
            if a < s[i][0]:
                r.append(s[i][1]+1)
                if i > 0:
                    tmp = i - 1
                break
        else:
            r.append(1)
    return r


if __name__ == '__main__':
    scores = list(map(int, input().rstrip().split()))

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
