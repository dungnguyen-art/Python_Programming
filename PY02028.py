
def Prime(k):
    if k < 2:
        return False
    for i in range(2, int(k // 2) + 1):
        if k % i == 0:
            return False
    return True

n = int(input())
st = input().split()
l = []
for i in st:
    if Prime(int(i)):
        l.append(i)

l.sort()
h = 0
for i in st:
    if i not in l:
        print(i, end=" ")
    else:
        print(l[h], end=" ")
        h += 1
