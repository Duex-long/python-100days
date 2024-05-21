import random
from math import sqrt
sum = 0
# for x in range(101):
#     print(x)
# print(sum)

for x in range(2,101,2):
    sum += x
print(sum)

def getRandomNumber():
    return random.randint(1,100)
counter = 0

answer = getRandomNumber()
# while True:
#     counter += 1
#     number = int(input("请输入"))
#     if number > answer :
#         print('小一点')
#     elif number < answer:
#          print('大一点')
#     elif number == answer:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

def assertIsPrimeNumber():
    is_prime = True

    num = int(input('请输入一个正整数: '))

    for x in range(2,num + 1):
        if num % x == 0 and not x == num:
            is_prime = False
            break

    print(is_prime,num)
    if is_prime and not num == 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)   
# assertIsPrimeNumber()


# 计算最大公约数
def computedMaxDivisor(num1,num2):
    maxDivisor = 1
    for x in range(maxDivisor,min(num1,num2)+1):
        if not num1 % x and not num2 % x:
            maxDivisor = x
    print("%d和%d的最大公约数是%d"%( num1, num2 ,maxDivisor))
    return maxDivisor

# 计算最小公倍数
def computedMinMultiple(num1,num2):
    minMultiple = 1
    maxDivisor = computedMaxDivisor(num1,num2)
    minMultiple = num1 * num2 / maxDivisor
    print("%d和%d的最小公倍数是%d"%( num1, num2 ,minMultiple))

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# computedMinMultiple(num1, num2)

# 打印如下所示的三角形

row = int(input("rows: "))
for i in range(1,row+1):
    printList = [] + ["*"] * i
    print("".join(printList))

print('---------')
for i in range(row):
    for j in range(row):
        if(i + j + 1 >= row):
            print("*",end="")
        else:
            print(' ',end="")
    print()

print('---------')
#  0 0 + 1 + 0  1  1 + 1 + 1 2 2 + 1 + 2 3  3 + 1 + 3
maxLen = 2 * row - 1
for i in range(0,row):
    printLen = 2 * i + 1
    patchNum = int((maxLen - printLen) / 2)
    printList = [" "] * patchNum + ["*"] * printLen + [" "] * patchNum
    print("".join(printList))
     
