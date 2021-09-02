# create by: Nguyen Tien Dung         -
# Date: 10:35 PM 31/8/2021            -
# -------------------------------------
# import array as arr
#
# a = arr.array('i', [])
#
# k = int(input("Enter size of array:"))
# for i in range(0, k):
#     num = int(input())
#     a.append(num)
# cnt = 0
# for i in range(0,k-1):
#     for j in range(i,k):
#         if a[i] > a[j]:
#             cnt = cnt + 1
# print(cnt)
T = int(input())
str = [int(x) for x in input().split()]
cnt = 0
for i in range(len(str)-1):
    for j in range(i+1,len(str)):
        if int(str[i]) > int(str[j]):
            cnt = cnt + 1
print(cnt)