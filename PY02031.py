st = input()
st = str.split()
n, m = int(str[0]), int(str[1])
matrix = []


def Prime(k):
    k = int(k)
    if k < 2:
        return False
    else:
        for i in range(2, int(k // 2) + 1):
            if k % i == 0:
                return False
    return True


for i in range(0, n):
    tmp = input()
    matrix.insert(i, tmp)
    matrix[i] = matrix[i].split()
    for j in matrix[i]:
        if Prime(j):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
