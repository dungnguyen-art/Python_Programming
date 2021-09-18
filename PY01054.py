T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    sm = 1
    for i in range(k):
        if int(s[i]) != 0:
            sm *= int(s[i])
    print(sm)