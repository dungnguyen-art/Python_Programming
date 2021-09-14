t = int(input())
while t > 0:
    s = input()
    s = s.split() #String là một đối tượng nên phải tái tạo lại s.
    a, b = int(s[0]), int(s[1])
    f = [] #chỉ số của list bắt đầu từ 0 nên phạm vị kết quá là a-1:b-1
    f.append(1)
    f.append(1)
    for i in range(2, 93):
        f.append(f[i - 1] + f[i - 2])
        # print(f[i],end=" ")
    for i in range(a-1,b-1):
        print(f[i],end=" ")
    print(f[b-1])
    t -= 1

