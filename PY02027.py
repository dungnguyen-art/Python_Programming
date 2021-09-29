import re
T = int(input())
res = []
while T > 0:
    T -= 1
    s = input()
    m = re.findall(r'\d+',s)
    res.append(m)
flattened = [val for sublist in res for val in sublist]
res_end = []
for i in flattened:
    res_end.append(int(i))
res_end.sort()
for i in res_end:
    print(i)