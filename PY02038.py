n = int(input())
res = 0
matrix = []
for i in range(0, n):
    a = input()
    l = []
    for i in a:
        l.append(i)
    tmp = l.count('C')
    res += int((tmp * (tmp - 1))/2)
    matrix.append(l)
for i in range(0,n):
    tmp = 0
    es = [sub[i] for sub in matrix]
    tmp = es.count('C')
    res += int(tmp*(tmp-1)/2)
# print(es)
# print(matrix)
print(res)

# 4
# CC..
# C..C
# .CC.
# .CC.
