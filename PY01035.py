from sys import stdin, stdout
from time import perf_counter
s = input()
leng = len(s)
lg = leng % 3
tmp = (3 - lg) % 3
while tmp > 0:
    tmp -= 1
    s = "0" + s
t1_stop = perf_counter()
for i in range(0,len(s),3):
    sm = int(s[i])*4 + int(s[i+1])*2 + int(s[i+2])
    print(sm,end="")
