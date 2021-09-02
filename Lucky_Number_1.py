str = input()
cnt = 0
for i in range(len(str)):
    if str[i] == '4' or str[i] == '7':
        cnt = cnt+1
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")