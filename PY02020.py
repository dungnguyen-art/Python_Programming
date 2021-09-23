n = int(input())
s = input().split()
l = []
for i in range(len(s)):
    l.append(float(s[i]))
l_1 = []
mx = max(l)
l_1.append(mx)
mn = min(l)
l_1.append(mn)
cnt = 0
sm = 0
for i in range(len(s)):
    if l[i] not in l_1:
        sm += l[i]
        cnt += 1
print("%.2f" % float(sm/cnt))