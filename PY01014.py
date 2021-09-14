str = input()
str = str.split()
a, k, n = int(str[0]), int(str[1]), int(str[2])
tmp = n-a
check = False
if tmp <= 0:
    check = False
else:
    i = 1
    b = 0
    while(b<=tmp):
        b = i*k-a
        if 0 < b <= tmp:
            print(b,end=" ")
            check = True
        i+=1
if check == False:
    print(-1)
