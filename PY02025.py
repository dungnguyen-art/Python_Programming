s = input().split()
n, m = int(s[0]), int(s[1])
l_1 = set(input().split())
l_2 = set(input().split())
res = sorted(l_1.intersection(l_2))
for i in res:
    print(i,end=" ")
print()
res_1 = []
for i in l_1:
    if i not in l_2:
        res_1.append(i)
res_1.sort()
for i in res_1:
    print(i,end=" ")
print()
res_2 = []
for i in l_2:
    if i not in l_1:
        res_2.append(i)
res_2.sort()
for i in res_2:
    print(i,end=" ")
print()