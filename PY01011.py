t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(22,n,22):
        check, check_1, check_2 = True, True, True
        st = str(i)
        k = len(st)
        if k % 2 == 1:
            check = False
        if check:
            for j in st:
                # print(j)
                if int(j) % 2 == 1:
                    check_1 = False
                    break
            if check_1:
                # print(st)
                for x in range(int(k/2)):
                    if st[x] != st[k-x-1]:
                        check_2 = False
                        break
                if check_2:
                    print(i,end=" ")

    print()