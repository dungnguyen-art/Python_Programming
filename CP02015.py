s = input().split()
n, m = int(s[0]), int(s[1])
a = input().split()
a = list(map(int,a))
mul_a = 1
for i in a:
    mul_a *= i
index, cnt = [],0
k = 1
while m > 0:
    m -= 1
    b = input().split()
    b = list(map(int,b))
    mul_b = 1
    for i in b:
        mul_b *= i
    if mul_a % mul_b == 0:
        cnt += 1
        index.append(k)
    k += 1
print(cnt)
for i in index:
    print(i,end=" ")