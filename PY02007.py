t = 10
re = []
while t>0:
    s = input()
    s = s.split()
    t = t - len(s)
    for i in s:
        k = int(i) % 42
        if k not in re:
            re.append(k)
print(len(re))