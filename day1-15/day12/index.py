# 正则表达式

# 目前正则表达式只是简单的尝试写法，以后需要补课


import re

def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username) # 
    m2 = re.match(r'^[1-9]\d{4,11}$') # 开头是1-9后补4-11位数字
    m3 = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')

    