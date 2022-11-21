#Question -2 Soluction
str1 = input()
str2 = input()
key = str2[-1]
count = 0
for i in str1:
    if i == key:
        count = count+1
print(count)