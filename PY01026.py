from collections import Counter
from sys import stdin, stdout
from time import perf_counter
T = int(input())
for i in range(1, T + 1):
    s1 = input()
    s2 = input()
    flag = 0
    for j in s1:
        if j in s2:
            c1 = s2.count(j)
            c2 = s1.count(j)
            if c1 != c2:
                flag = 1
                break
        else:
            flag = 1
            break
    t1_stop = perf_counter()
    print("Test",i,end=": ")
    if flag:
        print("NO")
    else:
        print("YES")

