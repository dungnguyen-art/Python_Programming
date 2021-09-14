t = int(input())
ar = [int(x) for x in input().split()]


def isPrime(k):
    if k < 2:
        return False
    else:
        for i in range(2, int(k // 2)+1):
            if k % i == 0:
                return False
    return True


s = []
for i in ar:
    if (isPrime(int(i)) == True) and i not in s:
        print(i, end=" ")
        print(ar.count(i))
        s.append(i)
