#  C(M,N) = M! / N! / (M - N)!

# 求阶层
def fac(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0,b=0,c=0):
    return a + b + c

print(roll_dice()) # 有默认值 
print(roll_dice(3)) # 选择传递
print(add()) # 有默认值 0
print(add(1)) # 传A 
print(add(1, 2)) # 传AB
print(add(1, 2, 3))# 传ABC
print(add(c=100,b=20,a=10)) #制定参数传递

# 重写add python没有重载 所以重新定义会覆盖之前的定义
def add(*args):
    total = 0
    for x in args:
        total += x
    return total


#  模块机制 python的每个文件都代表了一个模块
from index_2 import foo

# 或者
import index_2 as id2
id2.foo()

# 引入一个文件后会自动执行上下文内容 如果不需要执行 则可以判断是否是入口
# 判断是否是入口文件
if __name__ == '__main__':
    print('我是入口文件')
else:
    print('我不是入口文件')
