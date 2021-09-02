# -------------------------------------
# create by: Nguyen Tien Dung         -
# Date: 11:24 PM 30/8/2021            -
# -------------------------------------
T = int(input())
while T>0:
    str = input()
    k = len(str)
    if(str[k-1] == '6' and str[k-2] == '8'):
        print("YES")
    else:
        print("NO")
    T = T-1
