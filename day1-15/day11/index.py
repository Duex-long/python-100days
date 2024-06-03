from time import sleep
# 文件和异常
def main():
    json_path = './test.json'
    with open(json_path,'r',encoding="utf-8") as f:
        # 逐行读取
        for i in f:
            print(i)
            sleep(.5)
        
        # 表格读取
        lines = f.readlines()

    print(lines)  
   


if __name__ == '__main__':
    # main()

# 异常的行为可能导致程序出错崩溃，需要使用错误处理

def main1():
    #打开一个不存在的文件
    f = None
    try:
        with open('./none.json','r',encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
 

if __name__ == '__main__':
    main1()


from day5 import findPrimeNumber

def main2():
    file_names=('a.txt', 'b.txt','c.txt')
    fils_list=[]
    try:
        for file_name in file_names:
            fils_list.append(open(file_name,'w','utf-8'))
        for i in range(1,10000):
            if findPrimeNumber(i):
                if i < 100:
                    fils_list[0].write(str(i) + '\n')
                elif i < 1000:
                     fils_list[1].write(str(i) + '\n')
                elif i < 10000:
                    fils_list[2].write(str(i) + '\n')
    finally:
        for fs in file_names:
            if f:
                f.close()
        print('finally')



if __name__ == '__main__':
    main2()
