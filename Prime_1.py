import math

def Sieve(h):
    prime = [True for x in range(h + 1)]
    p = 2
    while p * p <= h:
        if prime[p]:
            for j in range(p * p, h + 1, p):
                prime[j] = False
        p += 1
    prime[0] = False
    prime[1] = False
    cnt = 0
    for j in range(2, h + 1):
        if prime[j]:
            cnt += 1
    return cnt
#hello bebe
T = int(input())
while T > 0:
    n = int(input())
    k = Sieve(n)
    flag = True
    if k < 2:
        flag = False
    for i in range(2, int(math.sqrt(k)) + 1, 1):
        if k % i == 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
    T -= 1
