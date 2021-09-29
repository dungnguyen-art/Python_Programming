from sys import stdin, stdout

T = stdin.readline()
T = int(T)


def cntDict(s):
    sm = 0
    for i in range(len(s)):
        sm += int(s[i])
    return sm


while T > 0:
    T -= 1
    n = stdin.readline()
    n = int(n)
    arr = stdin.readline().split()
    map_object = list(map(int, arr))  # huyen mang strinh sang mang int
    map_object.sort()
    list_string = list(map(str, map_object)) # chuyen mang in sang mang string
    dct = {}
    for i in list_string:
        if i not in dct:
            dct[i] = cntDict(i)     # dua cap key i value cntDic(i) vao dictionary

    tmp = {k: v for k, v in sorted(dct.items(), key=lambda x: x[1])} # sap xep theo value tang dan
    for i in tmp.keys():
        stdout.write(i + " ")
    print()
