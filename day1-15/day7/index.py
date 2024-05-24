import sys
s1 = r'\'hello, world!\''

s2 = r'\n\\hello, world!\\\n'

# print(s1, s2,  end='')


a1 = 1 * 2
a2 = '1' * 2
a3 = [1,2] * 2
print(a1)
print(a2)
print(a3)

at = 'test ' * 3
print(at[0:])
print(at[1:])
print(at[2:])
print(at[2::2]) # 从第二个开始取 idx+=2 
print(at[::2])
print(at[::-1]) # 倒叙
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

# list
list1 = [1, 3, 5, 5,7, 100]

listLen = len(list1)

# append
list1.append(200) #
print("append {0}".format(list1))
list1.insert(1,400)
print("insert {0}".format(list1))
list1.remove(5) # 按值remove 但是只能remove一个
print("remove {0}".format(list1))
# 判断remove
if 5 in list1:
    list1.remove(5)
print("remove {0}".format(list1))

list1.pop(0)
print("pop {0}".format(list1))

list1.pop(4)
print("pop {0}".format(list1))

objt = {a:1}
listobj1 = [1,objt,3,4,5]
listobj2 = listobj1[1:4]
print(listobj1)
print(listobj2)
objt["b"] = '333'
print(listobj1)
print(listobj2)
# 反转list
listobj3 = listobj1[-1::-1]
print(listobj3)
# 反转list
listobj4 = listobj1[::-1]
print(listobj4)

listobj5 = listobj1[-5:-4]
print(listobj5)

# sort
sortobj = {b:'c'}
slist1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
slist2 = sorted(slist1)
print('sort',slist2)
slist3 = sorted(slist1, reverse=True)
print('sort',slist3)

# 生成器
def printRet(f):
    print(f)
    return f
f = [printRet(x) for x in range(1,10)]
f2 = (x for x in range(1,10))
f3 = [x for x in range(1,10)]
f1 = [1,2,3,4,5,6,7,8,9]
print(sys.getsizeof(f))
print(sys.getsizeof(f1))
print(sys.getsizeof(f2))
print(sys.getsizeof(f3))
print(f2)

print(f3)



