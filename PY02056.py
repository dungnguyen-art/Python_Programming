def isPrime(k):
    k = str(k)
    if len(k) < 2:
        return False
    tmp = k[::-1]
    if int(tmp) == int(k):
        return True
    return False


s = input().split()
n, m = int(s[0]), int(s[1])
matrix = []
for i in range(n):
    a = input().split()
    l_1 = []
    for i in a:
        l_1.append(int(i))
    matrix.append(l_1)  # Nhập ma trận bằng list

matrix_tmp = matrix.copy()
flat_list = [item for sublist in matrix_tmp for item in sublist]  # chuyển list lồng nhau về list đơn để tim max, min
flat_list.sort(reverse=True)
r = 0
flag = 0
for i in flat_list:
    if isPrime(i):
        flag = 1
        r = i
        break

if flag:
    print(r)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == r:
                t = "Vi tri [" + str(i) + "]" + "[" + str(j) + "]"
                print(t)
else:
    print("NOT FOUND")
