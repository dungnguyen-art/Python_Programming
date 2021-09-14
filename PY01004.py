import math

t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    check = True
    if cnt < 2:
        check = False
    else:
        for i in range(2, int(cnt // 2) + 1):
            if cnt % i == 0:
                check = False
                break
    if check == True:
        print("YES")
    else:
        print("NO")
    t -= 1
