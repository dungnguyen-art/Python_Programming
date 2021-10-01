t = int(input())
while t > 0:
    t -= 1
    s = input().split()
    a,b = int(s[0]), int(s[1])
    res = 0
    for i in range(1,a+1):
        res += i**b
    print(res)