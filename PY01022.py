from sys import stdin, stdout
st = input()
flag = 1

cnt = 0
if len(st) == 1:
    cnt = 1
else:
    while len(st) > 1:
        sm = 0
        for i in range(len(st)):
            if st[i] == '-':
                sm += ord('-')-ord('0')
            else:
                sm += int(st[i])
        st = f"{sm}"
        cnt += 1
print(cnt)

