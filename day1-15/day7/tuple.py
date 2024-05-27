t=("a","b")
list_t = list(t)
print(list_t)

cons_t = (x for x in list_t)

set1 = {1,2,3,3,3,2}  #去重 set
print('set',set1)
print(len(set1))
set2 = set(range(1,10))
print('set2',set2)
set3 = { num for num in range(1,100) if not num % 3 }
print('set3',set3)

set1.add(5)
set2.remove(5)

print(set1,set2)
set1.discard(5)
print(set1)
set1.remove(2)
print(set1)
print(set1.pop())
print(set1)


scores = { "a":1,"b":2}

items1 = dict(one=1, two=2, three=3)
items2 = dict(zip(["a","b","c"],"123"))
print(items1,items2)
item3 = {
    num:num ** 2 for num in range(1,10)
}
print(item3)


import os
import time
# 跑马灯
def main():
    content = "describe"
    while True:
        os.system("clear")
        print(content)
        time.sleep(2)
        content = content[1:] + content[0]
        # content
# 验证码
import random
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_len = len(all_chars - 1)
    code = ''
    for i in range(code_len):
        index = random.randint(0,chars_len)
        code += all_chars[index]
    return code
# 设计一个函数返回给定文件名的后缀名。
def get_suffix(filename="",has_dot=False):
    pos = filename.rfind(".")
    print('pos',pos)
    if pos and pos < len(filename):
        index = pos if has_dot else pos + 1 
        print('pos',has_dot,index)
        return filename[index:]
    else:
        return ''

print(get_suffix('test.txt'))
print(get_suffix('test.txt',True))

