t = int(input())
AZ = "0123456789ABCDEFGHỊJKLMNOPQRSTUVWXYZ"
for i in range(t):
    str = input().split()
    m, n = int(str[0]), int(str[1])
    res = ""
    while True:
        if m == 0:
            break
        res = AZ[int(m % n)] + res
        m = int(m/n)
    print(res)
