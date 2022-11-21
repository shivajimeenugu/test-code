#Question -1 Soluction
num = int(input())
out = ""
while(num!=0):
    rem=num%3
    out = str(rem) + out
    num = num // 3
print(out)