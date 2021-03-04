import math
import os
import random
import re
import sys

# Complete the gridSearch function below.


def gridSearch(G, P):
    for i in range(len(G) - len(P) + 1):
        if P[0] in G[i]:
            for j in range(len(G[0]) - len(P[0]) + 1):
                for k in range(len(P)):
                    if G[i + k][j:j + len(P[0])] == P[k]:
                        pass
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result + '\n')
