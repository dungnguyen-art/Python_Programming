T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    s_1 = s[k-4:k]
    # print(s_1)
    n = int(s_1)
    ok = True
    if n < 2:
        ok = False
    for i in range(2,int(n//2)+1):
        if n%i == 0:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")