import ctypes

str = input()
str = str.split()
n, x = int(str[0]), int(str[1])
res = []
def Sieve():
    f = []
    f = [True for i in range(n**2)]
    f[0] = False
    f[1] = False
    for i in range(2, 1001):
        if f[i] == True:
            for j in range(i**2, n**2, i):
                f[j] = False

    for i in range(2, n**2):
        if f[i] == True:
            res.append(i)


Sieve()
print(x, end=" ")
tmp = x
for i in range(0, n):
    print(tmp + res[i], end=" ")
    tmp = tmp+res[i]
