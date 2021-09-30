# def desciption_city(city,country= 'VietNam'):
#     print(f"{city} là thủ đô của {country}")
#
# desciption_city(city="Ha Noi",country="Viet Nam")
# desciption_city(city="NY",country="USA")
# desciption_city(city="London",country="EL")
#
# def Mx(a,b,c):
#     res = max(a,b,c)
#     return  res
# print(Mx(5,20,16))

# def F(k):
#     if k == 0 or k == 1:
#         return 1
#     else:
#         return  k * F(k-1)
#
# while True:
#     k = int(input())
#     if k > 0:
#         break
# print(F(k))

# def S(s):
#     k = sum((1 for c in s if c.islower()))
#     K = sum((1 for c in s if c.isupper()))
#     print(k,K)
# S("HELlo aASFAFdsfsfq")

# def C(c):
#     if type(c) == int or type(c) == float:
#         return abs(c)
#     else:
#         return "NONE"
# print(C(-10.5))

# def check_perfect_number(k):
#     sm = 0
#     for i in range(1, k):
#         if k % i == 0:
#             sm += i
#     if sm == k:
#         print("YES")
#     else:
#         print("NO")
#
# check_perfect_number(15)