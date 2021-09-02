# T = int(input())
# while T > 0:
#     n = int(input())
#     str = input()
#     str = str.replace(" ","")
#     maxi  = 0
#     for i in range(0,len(str),1):
#         d[str[i]] = d[str[i]] + 1
#         if d[str[i]] >  maxi:
#             maxi = d[str[i]]
#     T = T - 1
#     print(maxi)
#     TLE
T = int(input())
while T>0:
    n = int(input())
    str = input()
    str = str.split()
    list_1 = []
    list_1[:0] = str
    dict = {}
    count,itm = 0,''
    for item in reversed(list_1):
        dict[item] = dict.get(item,0)+1
        if dict[item] >= count:
            count,itm = dict[item],item

    k = list_1.count(itm)
    if k > len(str)//2:
        print(itm)
    else:
        print("NO")
    T = T - 1
