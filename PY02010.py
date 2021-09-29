T = 10
while T > 0:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        tmp = int(input())
        l.append(tmp)
    mx = max(l)
    mn = min(l)
    if mx == mn:
        print("BANG NHAU")
    else:
        print(mn, mx)
