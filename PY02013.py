t = 10
while t>0:
    n = int(input())
    if n == 0:
        break
    res = []
    if n == 1:
        print(1)
    else:
        while n != 1:
            if n%2 == 0:
                n /= 2
                if n not in res:
                    res.append(n)
            else:
                n = n*3 + 1
                if n not in res:
                    res.append(n)
        res.append(1)
        print(len(res))