str1 = input()
str2 = input()
index = int(input())
index = index-1
# def insert_sequence(str1, str2, index):
str = str1[:index] + str2 + str1[index:]
print(str)