t = int(input())
while t:
    t -= 1
    n = input()
    n = n.split()
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")