s = input()
k = len(s)
if k % 2 == 1:
    k -= 1
l = []
l_1 = []
for i in range(0,k,2):
    tmp = s[i]+s[i+1]
    if tmp not in l:
        l.append(tmp)
    l_1.append(tmp)
for i in l:
    print(i,l_1.count(i))


