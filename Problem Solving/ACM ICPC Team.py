import math
import os
import random
import re
import sys

# Complete the acmTeam function below.


def acmTeam(topic):
    teams = []

    for i, x in enumerate(topic):
        for j in range(i + 1, len(topic)):
            cont = 0
            for index, letter in enumerate(x):
                if letter == '1' or topic[j][index] == '1':
                    cont += 1
            teams.append(cont)
    teams.sort(reverse=True)
    result = [teams[0], teams.count(teams[0])]
    return result


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
