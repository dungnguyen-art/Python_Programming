
s = input().split()
n, m = int(s[0]), int(s[1])
flag = 1
if n < m:
    k = m - n
    flag = 0
else:
    k = n - m
    flag = 1

matrix = []
for i in range(n):
    st = input().split()
    matrix.append(st)
r1 = []
r2 = [[]]
if flag:
    t = 0
    for i in range(n):
        if i % 2 == 0 and t < k:
            r1.append(matrix[i])
            t += 1
            if t == k:
                break
    for i in matrix:
        if i not in r1:
            for x in range(m):
                print(i[x],end=" ")
            print()
else:
    for i in matrix:
        t = 0
        for j in range(m):
            if j % 2 == 0 and t <= k:
                print(i[j],end=" ")
                t += 1
            elif t > k:
                print(i[j],end=" ")

        print()

