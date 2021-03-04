import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = list(itertools.product(range(x+1), range(y+1), range(z+1)))

    solution = [list(el) for el in coordinates if sum(el) != n]
    print(solution)
