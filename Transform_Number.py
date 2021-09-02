k = 10
while k > 0:
    ar = [int(x) for x in input().split()]
    n = len(ar)
    ch = True
    for i in range(n):
        if ar[i] != 0:
            ch = False
    if ch == True:
        break
    cnt = 0
    t = 5
    check = 0
    while t>0:
        x = ar[0]
        for i in range(n-1):
            ar[i] = abs(ar[i] - ar[i+1])

        ar[n-1] = abs(ar[n-1] - x)
        cnt += 1
        ok = True
        for i in range(n):
            if ar[i] != 0:
                ok = False
                break
        if ok == True:
            t = 0
    # print(cnt)
    print(cnt-1)

# //1 3 5 9
# //2 2 4 8
# //0 2 4 6
# //2 2 2 6
# //0 0 4 4
# //0 4 0 4
# //4 4 4 4
# //0 0 0 0