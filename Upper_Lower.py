# -------------------------------------
# create by: Nguyen Tien Dung         -
# Date: 11:42 PM 30/8/2021            -
# -------------------------------------
str = input()
up,lo = 0,0
for index in range(len(str)):
    if str[index] >= 'a':
        lo = lo + 1
    else:
        up = up + 1
if up > lo:
    print(str.upper())
elif lo >= up:
    print(str.lower())


