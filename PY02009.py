# T = int(input())
# while T > 0:
#     T -= 1
#     n = int(input())
#     myl = []
#     while n > 0:
#         n-=1
#         k = int(input())
#         myl.append(k)
#
#     mx = -1;
#     #dung count de dem so lan xuat hien cua moi phan tu trong list
#     for i in myl:
#         tmp = myl.count(i)
#         if tmp > mx:
#             mx = tmp
#     #sap xep list theo thu tu tang dan
#     myl.sort()
#     #neu gap phan tu co so lan xuat hien nhieu nhat(=mx) thi in ra
#     for i in myl:
#         tmp = myl.count(i)
#         if tmp == mx:
#             print(i)
#             break
#
#
#
