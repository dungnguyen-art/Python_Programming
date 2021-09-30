T = int(input())
matrix = []
k = T
a = []
while T > 0:
    T -= 1
    s = input().split()
    s = list(map(int, s))
    matrix.append(s)

if k <= 2:
    print(matrix[1][0] / 2, matrix[1][0] / 2)
else:
    a1 = int((matrix[2][1] + (matrix[1][0] - matrix[2][0])) / 2)
    a2 = int(matrix[2][1] - a1)
    a0 = int(matrix[1][0] - a1)
    a.append(a0)
    a.append(a1)
    a.append(a2)
    for i in range(3, k):
        x = matrix[i][0] - a[0]
        a.append(x)
    for i in a:
        print(i, end=" ")
