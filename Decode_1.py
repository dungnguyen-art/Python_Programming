T = int(input())
while T > 0:
    s = ""
    st = str(input())
    cnt = 1
    k = len(st)
    for i in range(0,k-1,1):
        if st[i] == st[i+1]:
            cnt = cnt+1
        else:
            sTmp = str(cnt) + st[i]
            s = s+sTmp
            cnt = 1
    if st[k-1] != st[k-2]:
        sTmp = '1' + st[k-1]
        s = s+sTmp
    else:
        sTmp = str(cnt) + st[k-1]
        s= s+sTmp
    print(s)
    T = T - 1