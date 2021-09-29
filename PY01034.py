import itertools

T = int(input())
while T > 0:
    T -= 1
    s = input()
    tmp = int(s)
    tmp_1 = len(s)
    s = list(s)
    per = list(itertools.permutations(s))
    l_1 = [''.join(permutation) for permutation in per]
    l_1 = list(map(int, l_1))
    l_1.sort(reverse=True)
    flag = 1
    res = 0
    for i in l_1:
        if i < tmp:
            res = i
            break
    if len(str(res)) == tmp_1 and tmp_1 > 1:
        print(res)
    else:
        print("-1")
