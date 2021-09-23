import math
s = input().split()
n, k = int(s[0]), int(s[1])
cnt = 0
# print(math.pow(10,k-1))
for i in range(int(math.pow(10,k-1)),int(math.pow(10,k))):
    if cnt == 10:
        print("\n")
        cnt = 0
    if math.gcd(i,n) == 1:
        print(i,end=" ")
        cnt += 1
# print(math.gcd(56,123))
