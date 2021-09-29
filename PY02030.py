def isPrime(k):
    if k < 2:
        return False
    for i in range(2, int(k // 2) + 1):
        if k % i == 0:
            return False
    return True


T = int(input())
s = (input().split())
s = list(map(int, s))
res = []
flag = 1
for i in s:
    if i not in res:
        res.append(i)

k = sum(res)
tmp = 0
for i in range(len(res)):
    tmp += res[i]
    if isPrime(tmp) and isPrime(k - tmp):
        print(i)
        flag = 0
        break
if flag:
    print("NOT FOUND")
