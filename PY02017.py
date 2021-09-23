T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    s = input().split()
    Hash = dict()
    for i in range(len(s)):
        Hash[s[i]] = Hash.get(s[i], 0) + 1
    for i in Hash:
        if Hash[i] % 2 != 0:
            print(i)
            break
