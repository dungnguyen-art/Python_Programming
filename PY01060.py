T = int(input())
while T > 0:
    T -= 1
    s = input()
    l = []
    for i in range(0, len(s)):
        l.append(int(s[i]))
    sm, mul = 0, 1
    flag = 1
    # print(s)
    for i in range(0, len(s)):
        if i % 2 == 1:
            sm += int(l[i])
        else:
            if l[i] > 0:
                mul = mul * l[i]
                flag = 0

    if flag:
        print(0)
    else:
        print(mul, end=" ")
    print(sm,end="\n")
