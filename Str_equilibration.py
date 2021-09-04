T = int(input())
while T > 0:
    s1 = input()
    s2 = s1[::-1]
    k = int(len(s1)/2)
    check = True
    for i in range(1, k+1):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
    T -= 1

