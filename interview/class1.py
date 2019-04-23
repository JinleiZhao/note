'class 的__new__ 和__init__'

class MyClass:
    
    def __init__(self, param, name):  #_init__有一个参数self，就是这个__new__返回的实例
        self.param = param
        self.name = name
        print('This is init func', self.param, self.name) #3
    
    def __new__(cls,*args, **kwargs):   #__new__至少要有一个参数cls，代表要实例化的类
        print('This is new func')  #1
        res =  object.__new__(cls)
        print('Bye')               #2
        return res   #__new__必须要有返回值，返回实例化出来的实例
    
myclass = MyClass("param", 'zhangsan')

'''
This is new func
Bye
This is init func param zhangsan
'''