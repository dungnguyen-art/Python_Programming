T = int(input())
while T>0:
    str = input()
    sum = 0
    check = 1
    # t = abs(int(str[0]) - int(str[1]))
    # print(type(t))
    for index in range(len(str)-1):
        if abs(int(str[index]) - int(str[index+1])) == 2:
            sum = sum + int(str[index])
        else:
            check = 0
            break
    if(check == 0):
        print("NO")
    else:
        sum = sum + int(str[len(str)-1])
        if sum % 10 == 0:
            print("YES")
        else:
            print("NO")
    # print(sum)
    T = T-1
