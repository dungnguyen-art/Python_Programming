n = int(input())
s = input()
s = s.split()
k = len(s)
cnt = 0
for i in range(k-1):
    if s[i] != s[i+1]:
        cnt += 1
print(cnt)