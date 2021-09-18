T = int(input())
while T > 0:
    T -= 1
    s = input()
    sm = 0
    ok = True
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                ok = False
                break
            sm += int(s[i])
        else:
            if int(s[i]) % 2 != 1:
                ok = False
                sm += int(s[i])
                break
            sm += int(s[i])
    if sm < 2:
        ok = False
    for i in range(2, int(sm//2)+1):
        if sm % i == 0:
            ok = False
            break
    # print(sm)
    if ok:
        print("YES")
    else:
        print("NO")