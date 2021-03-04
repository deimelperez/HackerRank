import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    half_money = money // 2
    l = 0
    sorted_cost = sorted(cost)
    r = len(cost) - 1
    while l < r:
        m = (l + r) // 2
        if sorted_cost[m] < half_money:
            l = m + 1
        else:
            r = m
    cost_unique = sorted(list(set(cost)))
    value = sorted_cost[l]
    index_unique = sorted_cost.index(value) if sorted_cost.index(
        value) < len(cost_unique) - 1 else len(cost_unique) - 1

    if value + cost_unique[index_unique + 1] <= money:
        if cost.index(sorted_cost[l]) + 1 > cost.index(cost_unique[index_unique + 1]) + 1:
            x = cost.index(cost_unique[index_unique + 1]) + 1
            y = cost.index(sorted_cost[l]) + 1
        else:
            x = cost.index(sorted_cost[l]) + 1
            y = cost.index(cost_unique[index_unique + 1]) + 1
        print(x, y)
        return
    else:
        if value + sorted_cost[l + 1] <= money:
            if cost.index(sorted_cost[l]) + 1 > cost.index(sorted_cost[l + 1]) + 1:
                x = cost.index(sorted_cost[l + 1]) + 1
                cost.pop(x)
                y = cost.index(sorted_cost[l]) + 2
            else:
                x = cost.index(sorted_cost[l]) + 1
                cost.pop(x)
                y = cost.index(sorted_cost[l + 1]) + 2
            print(x, y)
            return
        elif cost_unique[index_unique + 1] + cost_unique[index_unique - 1] <= money:
            if cost.index(cost_unique[index_unique - 1]) + 1 > cost.index(cost_unique[index_unique + 1]) + 1:
                x = cost.index(cost_unique[index_unique + 1]) + 1
                y = cost.index(cost_unique[index_unique - 1]) + 1
            else:
                x = cost.index(cost_unique[index_unique - 1]) + 1
                y = cost.index(cost_unique[index_unique + 1]) + 1
            print(x, y)
        else:
            if cost.index(cost_unique[index_unique - 1]) + 1 > cost.index(sorted_cost[l]) + 1:
                x = cost.index(sorted_cost[l]) + 1
                y = cost.index(cost_unique[index_unique - 1]) + 1
            else:
                x = cost.index(cost_unique[index_unique - 1]) + 1
                y = cost.index(sorted_cost[l]) + 1
            print(x, y)
            return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
