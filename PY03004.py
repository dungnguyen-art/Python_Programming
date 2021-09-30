import operator
from string import punctuation
n = int(input())
res = []
sp = set(punctuation)
while n > 0:
    n -= 1
    s = input()
    for i in range(len(s)):
        if s[i] in sp:
            s = s.replace(s[i], " ")
    s = s.lower()
    s = s.split()
    res.append(s)
l = [item for sublist in res for item in sublist]
l.sort()
res_dct = {}

for i in l:
    if i not in res_dct:
        res_dct[i] = l.count(i)
# sap xep dictionary theo value giam dan
sorted_d = dict(sorted(res_dct.items(), key=operator.itemgetter(1), reverse=True))
for i in sorted_d:
    print(i,sorted_d[i])
