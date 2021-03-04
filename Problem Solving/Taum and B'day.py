def birthdayPresent(b, w, bc, wc, z):
    if bc == wc:
        return (b + w) * bc
    if bc > wc:
        if wc + z < bc:
            return (wc * w) + ((wc + z) * b)
        else:
            return (wc * w) + (bc * b)
    if wc > bc:
        if bc + z < wc:
            return ((bc + z) * w) + (bc * b)
        else:
            return (wc * w) + (bc * b)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        bwz = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bc = int(bwz[0])

        wc = int(bwz[1])

        z = int(bwz[2])

        result = birthdayPresent(b, w, bc, wc, z)

        print(str(result))
