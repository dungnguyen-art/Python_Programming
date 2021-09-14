t = int(input())
while t:
    t -= 1
    s = input()
    s = s.split()
    n, x, m = float(s[0]), float(s[1]), float(s[2])
    money = n
    res = 0
    while money < m:
        money = money + money * x/100
        res += 1
    print(res)