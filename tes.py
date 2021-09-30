# a = [int(x) for x in input().split()]
# n = len(a)
# for i in range(n):
#     print(i)
import math
T = int(input())
while T > 0:
    n = int(input())
    cnt = 0
    # đếm các số nguyên tố từ 2 đến n
    for i in range(2, n, 1):
        ok = True
        for j in range(2, int(math.sqrt(i)+1), 1):
            if i % j == 0:
                ok = False
                break
        if ok:
            cnt += 1
# Kiểm tra số cnt có phải là số nguyên tố hay không
    check = True
    # print(cnt)
    if cnt < 2:
        check = False
    for i in range(2, int(math.sqrt(cnt)+1), 1):
        if cnt % i == 0:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
    T -= 1