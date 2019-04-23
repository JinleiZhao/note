
1、两个装饰器的执行流程：

from functools import wraps


def outer1(func):
    print('The first entrance')
    @wraps(func)
    def inner1(*args, **kw):
        print("1111111")
        rs = func(*args, **kw)
        print('1-----1')
        return rs
    return inner1

def outer2(func):
    print('The second entrance')
    @wraps(func)
    def inner2(*args, **kw):
        print("2222222")
        rst = func(*args, **kw)
        print('2-----2')
        return rst
    return inner2

@outer1
@outer2
def myfunc():
    print('Hello World')

>>> The second entrance
>>> The first entrance
myfunc()
1111111    外
2222222    里
Hello World   函数
2-----2    里
1-----1    外

总结：装饰器装饰是从里到外，而调用是:从外到里-->被装饰函数-->丛里到外

#装饰修饰类方法
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # 女性福音 :-)
        return method_to_decorate(self, lie)
    return wrapper
 
class Lucy(object):
 
    def __init__(self):
        self.age = 32
 
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)
