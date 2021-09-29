import sys
input = sys.stdin.readline
s = input().split()
n, m = int(s[0]), int(s[1])
a = set(input().split())
b = set(input().split())
flag = 1

if len(a) == len(b):
    for i in a:
        if i not in b:
            flag = 0
            break
else:
    flag = 0
if flag:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")