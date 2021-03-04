#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minFolders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER cssFiles
#  2. INTEGER jsFiles
#  3. INTEGER readMeFiles
#  4. INTEGER capacity
#

def minFolders(cssFiles, jsFiles, readMeFiles, capacity):
    # Write your code here
    folders = 0
    if readMeFiles == cssFiles + jsFiles:
        folders = readMeFiles
    elif capacity >= 3 and cssFiles > 0 and jsFiles > 0:
        folders = cssFiles + jsFiles - readMeFiles
    else:
        folders = cssFiles + jsFiles

    return folders


if __name__ == '__main__':
