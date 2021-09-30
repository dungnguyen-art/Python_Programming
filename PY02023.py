T = int(input())

def cntDict(s):
    sm = 0
    for i in range(len(s)):
        sm += int(s[i])
    return sm


while T > 0:
    T -= 1
    n = int(input())
    arr = input().split()
    map_object = list(map(int, arr))
    map_object.sort()
    list_string = list(map(str,map_object))
    # print(list_string)
    dct = {}
    for i in list_string:
        if i not in dct:
            dct[i] = cntDict(i)

    tmp = {k: v for k, v in sorted(dct.items(), key=lambda x: x[1])}
    # l = []
    for i in tmp.keys():
        print(i,end=" ")
    print()
