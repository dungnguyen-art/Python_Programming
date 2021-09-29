s = input()
k = len(s)
if k % 2 == 1:
    k -= 1
l = []
for i in range(0, k, 2):
    tmp = s[i] + s[i + 1]
    l.append(int(tmp))
t = int(input())
l.sort()
flag = 0
flag = 0
l_1 = []
for i in l:
    if i not in l_1:
        l_1.append(i)
        c = l.count(i)
        if c >= t:
            print(i,c)
            flag = 1
if flag == 0:
    print("NOT FOUND")