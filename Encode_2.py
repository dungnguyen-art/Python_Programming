P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
T = 5
while T > 0:
    inp = input()
    if inp == '0':
        break
    else:
        li = inp.split() # chuyển string về dạng list
        k = int(li[0])
        s1 = str(li[1])
        l = len(s1)
        for i in range(l):
            j = P.index(s1[i]) #tim index cua s1[i] trong P
            x = (j+k) % 28
            s1 = s1[:i]+P[x]+s1[i+1:] # thay đổi giá trị tại vị trí thứ i
        s1 = s1[::-1] # đảo ngược chuỗi số.
        print(s1)
    
