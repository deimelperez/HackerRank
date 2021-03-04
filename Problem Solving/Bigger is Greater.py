import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.


def biggerIsGreater(w):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_weight = []
    for letter in w:
        my_weight.append(alph.index(letter))
    my_weight.reverse()
    for i in range(0, len(my_weight) - 1):
        if my_weight[i] > my_weight[i + 1]:
            tmp = my_weight[0:i + 1]
            for j, w in enumerate(tmp):
                if my_weight[i + 1] < w:
                    my_weight[i + 1], tmp[j] = tmp[j], my_weight[i + 1]
                    break
            tmp.sort()
            for k in range(len(tmp)):
                my_weight[i - k] = tmp[k]
            break
    else:
        return 'no answer'
    my_weight.reverse()
    result = []
    for weight in my_weight:
        result.append(alph[weight])
    result = ''.join(result)
    return result


if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result + '\n')
