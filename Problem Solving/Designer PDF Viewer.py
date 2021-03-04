import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_h = []
    for letter in word:
        my_h.append(h[alph.index(letter)])
    return max(my_h) * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
