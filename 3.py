#Question -3 Soluction
num = int(input())
inCorrectNums = "347"
count = 0
start = 0

def isCorrect(num, inCorrectNums):
    while(num!=0):
        if str(num%10) in inCorrectNums:
            return False
        num = num//10
    return True

while(count != num):
    if isCorrect(start, inCorrectNums):
        count+=1
    start +=1
print(start)