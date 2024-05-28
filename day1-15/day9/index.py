# 装饰器
class Person:
    __slots__ = ('_name','_age')
    # 在上述示例中，Person只能拥有_name一个属性，而不能添加其他属性。
    _test = 'default'
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name
    
    @classmethod
    def test(cls):
        print(cls)
        print('%s'%cls._test)
    

if __name__ == '__main__':
    p = Person('张三',20)
    print(p.name)
    p.name = '李四'
    print(p.name)
    Person.test()

from abc import ABCMeta,abstractmethod

# 抽象类 实现后会报错
class Pet(metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        pass

# p = Pet('monkey') error
# 继承抽象类要实现抽象方法
class Monkey(Pet):
    def __init__(self,name):
        super().__init__(name)
    
    def make_voice(self):
        print('gegegegeggeg')

monkey = Monkey('kong')
monkey.make_voice()