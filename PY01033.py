import math

s = input().split()
a, b = int(s[0]), int(s[1])
for i in range(a, b - 1):
    for j in range(i + 1, b):
        for k in range(j + 1, b+1):
            if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(k, i) == 1:
                print("("+str(i)+', '+str(j)+', '+str(k)+")")
