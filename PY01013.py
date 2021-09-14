import math

t = int(input())
while t>0:
    st = input()
    st = st.split()
    a, b = int(st[0]), int(st[1])
    GCD = math.gcd(a, b)
    GCD = str(GCD)
    k = len(GCD)
    sum = 0
    for i in range(k):
        sum += int(GCD[i])
    check = True
    if sum < 2:
        check = False
    else:
        for i in range(2,int(sum // 2)+1):
            if sum % i == 0:
                check = False
                break

    if check:
        print("YES")
    else:
        print("NO")
    t -= 1