import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.


def organizingContainers(container, n):
    cuant = []
    suma = []
    for _ in range(n):
        cuant.append(0)
    for c in container:
        suma.append(sum(c))
        for i, x in enumerate(c):
            cuant[i] += x
    cuant.sort()
    suma.sort()
    div = []
    for i in range(0, n):
        div.append(suma[i] % cuant[i])
    if sum(div):
        return 'Impossible'
    else:
        return 'Possible'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container, n)

        print(result + '\n')
