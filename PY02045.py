s = input()
while len(s) > 1:
    k = int(len(s) / 2)
    sm_1, sm_2 = "", ""
    for i in range(len(s)):
        if i < k:
            sm_1 = sm_1 + s[i]
        else:
            sm_2 = sm_2 + s[i]
    s = str(int(sm_1) + int(sm_2))
    print(s)
