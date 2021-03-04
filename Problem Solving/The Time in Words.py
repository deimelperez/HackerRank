import math
import os
import random
import re
import sys

# Complete the timeInWords function below.


def timeInWords(h, m):
    num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                  6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                  11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                  15: 'Quarter', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                  20: 'Twenty'}
    minutes = ' minutes'
    if m == 0:
        return num2words1[h].lower() + ' o\' clock'
    if m == 30:
        return 'half past ' + num2words1[h].lower()
    if m > 30:
        if 60 - m > 20:
            _, remainder = divmod(60 - m, 10)
            return num2words1[20].lower() + ' ' + num2words1[remainder].lower() + ' minutes to ' + num2words1[h + 1].lower() if h + 1 < 13 else num2words1[1].lower()
        else:
            if 60 - m == 15:
                minutes = ''
            if 60 - m == 1:
                minutes = ' minute'
            return num2words1[(60 - m)].lower() + minutes + ' to ' + num2words1[h + 1].lower() if h + 1 < 13 else num2words1[1].lower()
    else:
        if m > 20:
            _, remainder = divmod(m, 10)
            return num2words1[20].lower() + ' ' + num2words1[remainder].lower() + ' minutes past ' + num2words1[h].lower() if h + 1 < 13 else num2words1[1].lower()
        else:
            if m == 15:
                minutes = ''
            if m == 1:
                minutes = ' minute'
            return num2words1[m].lower() + minutes + ' past ' + num2words1[h].lower() if h + 1 < 13 else num2words1[1].lower()


if __name__ == '__main__':
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result + '\n')
