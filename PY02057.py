# import numpy as np

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
mx = max(flat_list)
mn = min(flat_list)
r = mx - mn
flag = 0
flag_1 = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == r:
            if flag_1 == 1:
                print(r)
                flag_1 = 0
            t = "Vi tri [" + str(i) + "]" + "[" + str(j) + "]"
            print(t)
            flag = 1
if flag == 0:
    print("NOT FOUND")