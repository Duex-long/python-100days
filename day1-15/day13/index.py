# 进程和线程

# 进程就是操作系统中执行的程序，分配空间和地址
# 线程就是cpu调度的执行单元

#  模拟下载
from random import randint
from time import time, sleep
from multiprocessing import Process
from threading import Thread,Lock

from os import getpid


def download_task(filename):
    print("当前进程的pid为：%d"%getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))



def main():
    start = time()
    # 当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，
    # p1 = Process(target=download_task,args=("Python从入门到住院.pdf", ))
    # p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p1 = Thread(target=download_task,args=("Python从入门到住院.pdf", ))
    p2 = Thread(target=download_task, args=('Peking Hot.avi', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join() # join 表示等待进程结束
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

counter = 0
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

def main1():
    p1 = Process(target=sub_task,args=('ping',))
    p2 = Process(target=sub_task,args=('pong',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# if __name__ == '__main__':
    # main()
    # main1()


# 自定义线程
class DownloadTask(Thread):
    def __init__(self,filename):
        super.__init__()
        self.__filename = filename



class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self.__account = account
        self._money = money
    def run(self):
        self.__account.deposit(self._money)

# class Account:
#     def __init__(self):
#         self.__balance = 0
#         self._lock = Lock()
#     def deposit(self,money):
#         self._lock.acquire()
#         try:
#             new_balance = self.__balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             self._lock.release()
#     @property
#     def balance(self):
#         return self.__balance


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代s码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

    
def main3():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(account.balance)


def main4():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    # main3()
    main4()
    # main1()