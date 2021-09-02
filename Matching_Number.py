T = int(input())
while T>0:
    n = int(input())
    str1 = [int(x) for x in input().split()]
    str2 = [int(x) for x in input().split()]
    str1.sort()
    str2.sort()
    check = 0
    for i in range(0,n,1):
        if str1[i] > str2[i]:
            check = 1
            break

    if check == 1:
        print("NO")
    else:
        print("YES")
    T = T - 1