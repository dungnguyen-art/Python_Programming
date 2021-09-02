# -------------------------------------
# create by: Nguyen Tien Dung         -
# Date: 10:30 PM 30/8/2021            -
# -------------------------------------
T = int(input())
while T>0:
    str = input()
    check = 0
    for index in range(len(str)-1):
        if int(str[index]) > int(str[index+1]):
                check = 1
                break
    if check == 0:
        print("YES")
    else:
        print("NO")
    T = T-1
    print("\n")
