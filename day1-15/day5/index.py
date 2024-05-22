from random import randint
# 寻找水仙花数。
# // 整除
def findDaffodil():
    # 三位数 [100,1000]
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        # print("num: %d num//10: %d num//10mo10: %dmid: %d"%(num,num // 10, num //10 % 10, mid))
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)

findDaffodil()
print("------------------------")
# 正整数的反转
def reserveInt():
    num = randint(0,100)
    reversed_num = 0
    print(num)
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    print(reversed_num)


reserveInt()

print("------------buyChicken------------")

def  buyChicken():
    for x in range(0,100//5):
        for y in range(0,100//3):
            z = 100 - x - y
            if x * 5 + y * 3 + z / 3 == 100:
                print(x,y,z)

buyChicken()

print("------------兔子方程------------")

#  1  1 2 3 5 8 13
def fibonacci(n):
    # 边界值判断
    if n == 1 or n == 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

print("------------10000以内的完美数------------")

def findPerfectNum():
    for x in range(2,10000):
        perfectNum = 1
        for y in range(2,x):
            if x % y == 0:
                perfectNum += y
        if perfectNum == x:
            print('perfectNum: %d'%x)

findPerfectNum()

print("------------100以内的素数------------")

def findPrimeNumber(n=100):
    isPrimeNumber = True
    for x in range(2,n):
        if  n % x == 0:
            isPrimeNumber = False
            break
    return isPrimeNumber

for x in range(2,100):
    if findPrimeNumber(x):
        print(x)