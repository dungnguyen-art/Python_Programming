t = int(input())
while t:
    t -= 1
    n = int(input())
    cnt = 0
    print(1,end=" * ")
    while n%2 == 0:
        cnt += 1
        n /= 2
    if cnt > 0:
        if n > 1:
            print(str(2) + "^" + str(cnt), end=" * ")
        else:
            print(str(2) + "^" + str(cnt), end="")

    for i in range(3,int(n//2)+1,2):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
        if cnt > 0:
            if n > 1:
                print(str(i)+"^"+str(cnt),end=" * ")
            else:
                print(str(i)+"^"+str(cnt),end="")
    if n>2:
        print(str(int(n))+"^"+str(1),end="")
    print()
