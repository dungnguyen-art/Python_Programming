T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    lt = []
    for i in range(k):
        lt.append(int(s[i]))
    sm = sum(lt)
    sm = str(sm)
    k = len(sm)
    ok = True
    if k <= 1:
        ok = False
    for i in range(int(k//2)+1):
        if sm[i] != sm[k - i - 1]:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")
# print(type(sm))
