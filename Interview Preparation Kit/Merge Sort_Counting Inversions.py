import math
import os
import random
import re
import sys

# Complete the countInversions function below.
# Only works on Pypy3


def mergeSort(arr):
    cont = 0
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]

        cont += mergeSort(L)
        cont += mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] <= M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
                cont += len(L) - i
            k += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(M):
            arr[k] = M[j]
            k += 1
            j += 1
        return cont
    else:
        return 0


def countInversions(arr):
    cont = mergeSort(arr)
    return cont


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')
