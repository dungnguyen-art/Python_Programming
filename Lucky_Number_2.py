T = int(input())
while T>0:
    check = 0
    str = input()
    for i in range(len(str)):
        if str[i] != '4' and str[i] != '7':
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
    T = T - 1