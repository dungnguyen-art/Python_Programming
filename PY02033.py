import math
T = int(input())
while T > 0:
    T -= 1
    s = input().split()
    n, p = int(s[0]), int(s[1])
    res, tmp =0, 0
    i = 0
    while tmp < n:
        tmp = p**i
        if math.factorial(n) % tmp == 0:
            res = i
        i += 1

    print(res)