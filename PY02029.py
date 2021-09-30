s = input().split()
n, m = int(s[0]), int(s[1])
l_1 = input().split()
l_1 = list(map(int, l_1))
dct = {}
for i in l_1:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
tmp = {k: v for k, v in sorted(dct.items(), key=lambda x: x[1])}
l = []
l = set(list(tmp.values()))
mx = max(l)
res, flag = 0, 0
while len(l) > 0:
    mxTmp = max(l)
    if mxTmp == mx:
        l.remove(mxTmp)
    else:
        flag = 1
        res = mxTmp
        break
if flag == 1:
    for i in range(1, m + 1):
        if l_1.count(i) == res:
            print(i)
            break
else:
    print("NONE")
