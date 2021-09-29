import math

T = int(input())
while T > 0:
    T -= 1
    s = input().split()
    n, p = int(s[0]), int(s[1])
    tmp = math.factorial(n)
    # print(tmp)
    i, res, x = 0, 0, 0
    while res < n:
        res = p ** i
        if tmp % res == 0:
            x = i
        i += 1
    print(x)
