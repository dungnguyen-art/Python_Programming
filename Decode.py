# -------------------------------------
# create by: Nguyen Tien Dung         -
# Date: 11:23 PM 30/8/2021            -
# -------------------------------------
#hehelo bebe
T = int(input())
while T>0:
    str = input()
    for index in range(len(str)):
        if index % 2 == 1:
            k = int(str[index])
            # print(str[index])
            while k > 0:
                print(str[index-1],end="")
                k = k-1
    T = T-1
    print("\n")