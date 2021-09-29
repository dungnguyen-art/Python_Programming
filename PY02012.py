from collections import Counter
from sys import stdin, stdout
from time import perf_counter

n = int(input())
odd = []
even = []
t = n
st_1 = []
st = []
while t > 0:
    s = input().split()
    st_1.append(s)
    t = t - len(s)
for elem in st_1:
    st.extend(elem)

for i in st:
    if int(i) % 2 == 0:
        even.append(int(i))
    else:
        odd.append(int(i))

even.sort()
odd.sort(reverse=True)
k, h = 0, 0
t1_stop = perf_counter()

for i in st:
    if int(i) % 2 == 0:
        print(even[k], end=" ")
        k += 1
    elif int(i) % 2 == 1:
        print(odd[h], end=" ")
        h += 1
