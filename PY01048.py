T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    # //12 =  3 4 6
    # ((đầu + cuối) * (cuối - đầu +1)) == 18
    # cuối ** - đầu** == 18
    cnt = 0
    c , d = int(n/2) + 1, 1
    for i in range(1,int(n/2)+1):
        for j in range(i+1,int(n/2)+1):
            res = (i + j) * (j - i + 1)
            if res == n*2:
                cnt += 1
    print(cnt)
