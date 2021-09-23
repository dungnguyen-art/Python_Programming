T = int(input())

def Prime(k):
    if k < 2:
        return False
    for i in range(2,int(k//2)+1):
        if k % i == 0:
            return False
    return True


while T > 0:
    T -= 1
    s = input()
    l = []
    for i in range(0, len(s)):
        l.append(int(s[i]))
    k = len(s)
    flag = 1
    if Prime(k):
        flag = 0
    cnt = 0
    for i in range(0,k):
        if Prime(l[i]):
            cnt += 1

    flag_1 = 1
    if cnt > k - cnt:
        flag_1 = 0
    if flag_1 == 0 and flag == 0:
        print("YES")
    else:
        print("NO")