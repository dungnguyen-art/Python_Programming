T = int(input())


def Prime(k):
    if k < 2:
        return False
    for i in range(2, int(k // 2) + 1):
        if k % 2 == 0:
            return False
    return True


while T > 0:
    T -= 1
    s = input()
    ok = True
    for i in range(len(s)):
        print(i, " ", int(s[i]))
        if (Prime(i) == True and Prime(int(s[i])) == True) or (Prime(i) == False and Prime(int(s[i])) == False):
            continue
        else:
            ok = False
            break
        # print(i + " " + s[i])
    if ok:
        print("YES")
    else:
        print("NO")
