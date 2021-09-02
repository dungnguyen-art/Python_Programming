T = int(input())
while T>0:
    s = input()
    n = len(s)
    sum = 0
    s1 = ""
    for i in range(n):
        if s[i].isnumeric() == True:
            sum += int(s[i])
    for i in range(n):
        if s[i].isnumeric() != False:
            continue
        else:
            s1 = s1 + s[i]
    s2 = sorted(s1)
    s1 = "".join(s2)
    print(s1+str(sum))
    T -= 1