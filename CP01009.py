import operator
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = input().split()
    dct = {}
    for i in s:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    sorted_d = dict(sorted(dct.items(), key=operator.itemgetter(1), reverse=True))
    for i in sorted_d:
        k = sorted_d[i]
        while k > 0:
            k -= 1
            print(i,end=" ")
    print()
