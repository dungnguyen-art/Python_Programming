from sys import stdin, stdout
from time import perf_counter

s = input()
st = []
# for i in range(len(s)):
#     st.append(s[i])
# res = []
k = len(s)
if k % 2 == 1:
    k -= 1
    # 0 1 2 3 4 5
for i in range(0, k - 1, 2):
    st.append(s[i] + s[i + 1])
st.sort()
res = []
t1_stop = perf_counter()
for i in st:
    if i not in res:
        res.append(i)
for i in res:
    print(i, end=" ")
