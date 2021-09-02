# -------------------------------------
# create by: Nguyen Tien Dung         -
# Date: 11:20 PM 31/8/2021            -
# -------------------------------------
T = int(input())
while T > 0:
    str = input()
    if str[0] == str[len(str)-2] and str[1] == str[len(str)-1]:
        print("YES")
    else:
        print("NO")
    T = T - 1
