T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    #dung list st de chua cac chu so trong n sau do dung ham sum de tinh tong cua chung.
    lt = []
    for i in range(k):
        lt.append(int(s[i]))
    sm = sum(lt)
    ok = True
    #kiem tra snt
    if sm < 2:
        ok = False
    for i in range(2, int(sm//2)+1):
        if sm % i == 0:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")

