# dung List and set in collection.
from collections import Counter
from sys import stdin, stdout
from time import perf_counter

T = int(stdin.readline())
while T > 0:
    T -= 1
    st = input().split()
    n, m, k = int(st[0]), int(st[1]), int(st[2])
    # N, M, K = map(list,input().split())
    N = input().split()
    M = input().split()
    K = input().split()
    # res = N.intersection(M).intersection(K)
    res = list((Counter(N) & Counter(M) & Counter(K)).elements())
    t1_stop = perf_counter()
    if not res:  # kiem tra xem list co rong hay khong.
        print("NO", end="")
    else:
        for i in res:
            print(i, end=" ")
    print()
