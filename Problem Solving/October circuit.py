# n = input()
# s = input()
# x = set(s)
# count = []
# for c in x:
#     count.append(s.count(c))
# print(max(count))

import numpy as np
zeros = np.zeros(1000001, dtype=int)
n = int(input())

for _ in range(n):
    l = list(map(int, input().rstrip().split()))
    if l[0] >= 1:
        r, ranges = l[0], l[1:]
        for i in range(0, r * 2 - 1, 2):
            zeros[ranges[i]] += 1
            zeros[ranges[i + 1] + 1] -= 1

for i in range(1000000):
    zeros[i + 1] += zeros[i]
    if zeros[i + 1] == 0:
        print(i + 1)
        break
else:
    print(-1)
