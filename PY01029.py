import math

T = int(input())
while T > 0:
    T -= 1
    num = input()
    nb = int(num)
    num = num[::-1]
    nb_1 = int(num)
    GCD = math.gcd(nb, nb_1)
    if GCD == 1:
        print("YES")
    else:
        print("NO")