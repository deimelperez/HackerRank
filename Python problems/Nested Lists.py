if __name__ == '__main__':
    d = {}
    lowest = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if d.get(score, 0):
            l = d[score]
            l.append(name)
            d[score] = l
        else:
            d[score] = [name]

        lowest.append(score)
    lowest = sorted(list(set(lowest)))
    for name in sorted(d[lowest[1]]):
        print(name)
