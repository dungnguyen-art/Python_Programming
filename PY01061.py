T = int(input())
while T > 0:
    T -= 1
    s = input()
    k = len(s)
    #dung chi so index de dua 3 phan cuoi vao s_1 sau do ep kiem ve int -==> check prime
    s_1 = s[k-3:k]
    # print(s_1)
    n = int(s_1)
    ok = True
    if n < 2:
        ok = False
    for i in range(2,int(n//2)+1):
        if n%i == 0:
            ok = False
            break
    # dung chi so index de dua 3 phan dau vao s_2 sau do ep kiem ve int -==> che
    s_2 = s[0:3]
    # print(s_2)
    ok_1 = True
    n_2 = int(s_2)
    if n_2 < 2:
        ok_1 = False
    for i in range(2,int(n_2//2)+1):
        if n_2 % i == 0:
            ok_1 = False
            break
    if ok == True and ok_1 == True:
        print("YES")
    else:
        print("NO")