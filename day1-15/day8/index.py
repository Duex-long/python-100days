#  oop

# student函数中的object应该是表示class继承Object
class Student(object):
    # __init__类似于 constructor 用于在实例化的过程中进行初始化操作
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 行为
    def study(self,course_name):
        print("%s正在学习%s"%(self.name,course_name))

# 实例化对象
def main():
    stu1 = Student("张三",20)
    stu2 = Student("李四",21)
    stu1.study("Python")
    stu2.study("C++")
    stu1.study('高等数学')
    stu2.study('低等数学')

if __name__ == '__main__':
    main()


# 私有属性和受保护的属性
class Test:
    def __init__(self,foo):
        self.foo =foo
    def __bar(self):
        print(self.foo)
        print('__bar')

if __name__ == '__main__':
    test = Test('hello')
    test._Test__bar()


# 练习1：定义一个类描述数字时钟。

from time import sleep

class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._open = True
    
        while(self._open):
            self.run()
            self.show()
            sleep(1)
    
    def run(self):
        if(self.time_changed('_second')):
            if self.time_changed('_minute'):
                self.time_changed('_hour',24)
    
    def show(self):
        print("%02d:%02d:%02d"%(self._hour,self._minute,self._second))
    def time_changed(self,state,base=60):
        current_num = getattr(self,state)
        [result,result_state] = Clock.computed_time(current_num,base)
        setattr(self,state,result)
        return result_state

    @staticmethod
    def computed_time(number,base=60):
        num = number + 1
        return [num,False] if not num == base else [0,True]


if __name__ == '__main__':
    clock = Clock(23,59,58)
