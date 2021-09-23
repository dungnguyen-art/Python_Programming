n = int(input())
s = input().split()
# Nếu không dùng vòng for này để chuyển data type từ string to int thì WA
for i in range(0,n):
    s[i] = int(s[i])
s.sort()
flag = 1
# print(s)
for i in range(0, n - 1):
    if int(s[i + 1]) - int(s[i]) > 1:
        flag = 0
        print(int(s[i]) + 1)
        break
if flag:
    print(int(s[n - 1]) + 1)
