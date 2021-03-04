'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


def beautiful(s):
    count = 0
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            s[i + 1] = s[i] + 1
            count += 1

    return(count)


# Write your code here
for _ in range(int(input())):
    _ = input()
    secuence = map(int, input().split())
    print(beautiful(secuence))
