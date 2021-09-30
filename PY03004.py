import operator
from string import punctuation
n = int(input())
res = []
sp = set(punctuation)   # tap ki tu dac biet
while n > 0:
    n -= 1
    s = input()
    for i in range(len(s)):
        if s[i] in sp:
            s = s.replace(s[i], " ")    # thay doi ki tu dac biet bang " "
    s = s.lower()
    s = s.split()
    res.append(s)

l = [item for sublist in res for item in sublist]   # convert nested list to list
l.sort()        # sap xep theo thu tu tu dien
res_dct = {}

for i in l:
    if i not in res_dct:
        res_dct[i] = l.count(i)

sorted_d = dict(sorted(res_dct.items(), key=operator.itemgetter(1), reverse=True)) # sap xep dictionary theo value giam dan
for i in sorted_d:
    print(i,sorted_d[i])
