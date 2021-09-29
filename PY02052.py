n = int(input())
sm, sm_1 = 0,0
for i in range(0,n):
    st = input().split()
    for k in range(0,n):
        if i < k:
            sm += int(st[k])
        elif i > k:
            sm_1 += int(st[k])
c = int(input())
if abs(sm - sm_1) <= c:
    print("YES")
else:
    print("NO")

print(abs(sm-sm_1))