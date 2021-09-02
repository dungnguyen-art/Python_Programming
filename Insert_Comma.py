# for i in range(5,-1,-1):
#     print(i)
# systax
# str = str1[:index] + str2 + str1[index:]
str = input()
# print(len(str))
for i in range(len(str)-3,0,-3):
    str = str[:i] + "," + str[i:]
print(str)