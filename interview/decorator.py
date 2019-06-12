def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock()-t)
        return res
    return wrapper
 
 
def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper
 
 
def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper
 
@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))
'''
print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))
'''
#输出:
#reverse_string ('Able was I ere I saw Elba',) {}
#wrapper 0.0
#wrapper has been used: 1x
#ablE was I ere I saw elbA
'装饰器只能被调用一次,所以第二次调用是接着上一次不是重更新计数'
#reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
#wrapper 0.0
#wrapper has been used: 2x
#!amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A

import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @staticmethod  #静态方法，类直接调用
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

    # @classmethod #改成类方法
    # def now(cls):
    #     t=time.localtime()
    #     return cls(t.tm_year,t.tm_mon,t.tm_mday) #哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)
e=EuroDate.now()
print(e) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
'''
输出结果:
year:2017 month:3 day:3
'''

'''
当不使用类方法时结果为（使用静态方法）：
<__main__.Date object at 0x1013f9d68>
'''

'计算函数运行时间'

from functools import wraps

def calctime(func):
    @wraps(func)
    def inner(*args, **kw):
        start_time = time.time()
        print('func start at:',start_time)
        r = func(*args, **kw)
        run_time =  time.time()-start_time
        print('func run time:',run_time)
        return r
    return inner

@calctime
def testfunc():
    print("start")
    time.sleep(2)
    print('end')

#testfunc()


'staticmethod  静态方法'

class MyClass:

    age = 12

    def __init__(self, name):
        self.name = name


    ' 返回函数的静态方法'
    @staticmethod
    def sum(x,y,z):   #变成了类的方法不需要传递实例
        return x + y + z  
    
    'classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，\
        但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。'
    @classmethod
    def setinit(cls,name):
        return cls(name)

    @staticmethod
    def setinit2(name):
        return MyClass(name)

    def setsum(self):
        return MyClass.sum(2,3,4)
    
    def __str__(self):
        print('hello')

print(MyClass.sum(1,2,3))   #类直接调用不需实例化，先实例化在调用也不报错
b = MyClass.setinit('li')
print(b.name)
c = MyClass.setinit2('wang')
print(c.name)
print(c.age)
s = MyClass('zhang')
print(s.sum(1,2,3))
print(s.setsum())


'闭包作用----保存函数的状态信息，使函数的局部变量信息依然可以保存下来'