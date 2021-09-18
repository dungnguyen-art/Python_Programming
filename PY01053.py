t = int(input())
while t:
    t -= 1
    s = input()
    lt = []
    for i in range(len(s)):
        lt.append(int(s[i]))
    sm = sum(lt)
    if sm % 3 == 0:
        print("YES")
    else:
        print("NO")