import math
t = int(input())
ar = [int(x) for x in input().split()]
ar.sort()
for i in range(0,len(ar)-1):
    for j in range(i+1,len(ar)):
        if math.gcd(ar[i],ar[j]) == 1:
            print(ar[i],end=" ")
            print(ar[j])

