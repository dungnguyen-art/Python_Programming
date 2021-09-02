import math

T = int(input())

while T>0:
    n = int(input())
    check = 0
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i == 0:
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
    T = T - 1