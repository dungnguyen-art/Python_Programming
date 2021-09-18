T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    ok = True
    for i in range(0, k, 2):
        if s[i] != s[0]:
            ok = False
            break
    if ok == True and k % 2 == 1 and s[0] != s[1]:
        print("YES")
    else:
        print("NO")
