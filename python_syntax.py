# 1、yield
#yield： 用在函数中，若不使用在函数中则会抛 outside function错误；含有yield则此函数为生成器
#在循环中每次调用只执行到第一个yield处并记录当前位置，下次调用从当前位置处开始执行。
'''
In[2]: def fun(n=5):
   ...: for i in range(n):
   ...:     yield
In[7]: fun(6)
Out[7]: < generator object fun at 0x7f08addca570 >
In[4]: list(fun(6))
In [11]: next(fun(6))
Out[11]: 0
'''
def yield_test(n):
    for i in range(n):
        yield call(i)     #首次执行到此处，下次执行从此处开始
        print("i=", i)
    #做一些其它的事情
    print("do something.")
    print("end.")
def call(i):
    return i*2
'''
In [17]: next(n)
Out[17]: 0
In [18]: next(n)
i= 0
Out[18]: 2
'''
#2、lambda 
    #a、内置函数
from functools import reduce
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: x % 3 == 0, foo))) #[18, 9, 24, 12, 27],filter有比较等式需要返回ture或false
print(list(map(lambda x: x * 2 + 10, foo)))#[14, 46, 28, 54, 44, 58, 26, 34, 64]，map返回每个传入变量返回的值
print(reduce(lambda x, y: x + y, foo))#139
'reduce原理：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)\
            reduce把结果继续和序列的下一个元素做累积计算'

#b、应用在闭包中
def get_y(a, b):                  
     return lambda x: a*x+b      
y1 = get_y(1, 1)
print(y1(1))  #2        
#等价于
def get_y(a, b):
    def func(x):
        return a*x+b
    return func
y1 = get_y(1, 1)
y1(1)  # 结果为2

#c、函数中
list1 = [3, 5, -4, -1, 0, -2, -6]
sorted(list1, key=lambda x: abs(x))
#等价：
def get_abs(x):
    return abs(x)
sorted(list1, key=get_abs)

#d、字典排序
d = {'a': 1, 'b': 4, 'c': 2}
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
#转成字典
dict(d)  # / {k[0]:k[1] for k in d }
'''
2 psutil模块（获取cpu内存等硬件信息）
'''
import psutil
from time import sleep
def get_process():
    # pid_list = []
    for pid in psutil.pids():
        process = psutil.Process(pid)
        yield process
def show_cpu():        
    # pro = []
    for process in get_process():
        try:
            __cpu = process.cpu_percent(None),process.name() #第一次获取没有值，延迟后在获取有值？？？
            sleep(1)               #cpu_percent获取的是一个时间段中的数据，不是一个时间点,所以调用两次
            cpu_process = (process.cpu_percent(None), process.name())
            yield cpu_process
        except:  #并未捕获到异常
            pass
         
# for i in show_cpu():
#     print(i)

'''
3、collections 模块
 a、OrderedDict 有序字典
 b、defaultdict 缺省值
 c、nametuple  
'''
from collections import OrderedDict
l1 = [1,4,2,3]
l2 = ['a','c','d','b']

d1 = dict(zip(l2,l1)) #随机
d2 = OrderedDict(zip(l2,l1))  #按加入的顺序排序

print(d1,d2)
print(d2['b'])
'''
字典排序：
d = {"a":2,"b":3,"d":4,"c":1}
排序：
a = sorted(d.items(), key=lambda v:v[1] ,reverse = True)
转化成有序字典：
d = OrdereDict(a)
'''

from collections import defaultdict
students = defaultdict(lambda:60) #设置学生这个字典的默认值是60,
students['a'] = 56
students['b'] = 67
print(students)
print(students['c'])  #c不存在字典中，所以他的值是60

d1 = defaultdict(set)  #缺省值设置为set格式
d2 = {}
names = ['Tom','Jack','John']

for index,name in enumerate(names):
    d1[name].add(('boy',60+index))  #add：set的方法，不能添加列表和字典等
    # d2[name].add(['boy',60+index])
print(d1)

from collections import namedtuple

User = namedtuple('User','name,score,sex')  #创建一个实例

john = User(name='john',score=90,sex=0)    #赋值：直接赋值

tom = User._make(('tom',67,1))   #赋值：使用_make方法赋值
print(john)
print(tom)
tom1 = tom._replace(score=89)   #改变属值，将属性值改变赋给新的变量，本身并没有变
print(tom.score)
print(tom1.score)

tom2 = tom1._asdict()  #将元组转化为有序字典
print(tom2)
'''
Counter
 将列表/字符串转化字典，键是元素，值是个数
'''
from collections import Counter
l = [1,2,3,4,3,2,1]   # s = 'progame'
# {i:l.count(i) for i in l}  转化成普通字典
ld = Counter(l)  #Counter(s)
print(ld)

'''
4.concurrent.futures并发库 多进程 多线程
'''
from concurrent.futures import ThreadPoolExecutor
from time import sleep ,time as t
def myfunc(n):
    sleep(1)
    return n
print(t())
with ThreadPoolExecutor(max_workers=5) as exe:  #max_works 创建线程池
    l = []
    for i in range(5):
        res = exe.submit(myfunc,i)     #submit 向线程池中添加任务
                           #函数名，参数
        l.append(res)
    for n in l:
        print(n)
        print(n.result())  #返回任务的结果
print(t())

print('#########################')
'''
print(t())
l = []
for i in range(5):
    l.append(myfunc(i))

for n in l:
    print(n)
print(t()) 
'''

'''
5、logging
'''
import logging
logging.basicConfig(level=logging.WARNING,  #设置日志等级，只能显示此等级以上的日志
                    # filename='mynote.log', #日志存储位置,不设置则在当前终端显示
                    format='%(levelname)s:%(asctime)s:%(message)s')#设置日志格式，参数可见help
logging.critical('This is a critical message')
logging.error("This is an error message")
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')

'''
6、argparse 命令行交互
'''
import argparse

'''
7、例题：
    一个数(abc)遵循a^p+b^(p+1)+c^(p+2) ...  = abc * k  找到对应的abc（n）和p
'''
def arv1(n, p):
    s = 0
    for i, c in enumerate(str(n)): #获取幂的基数和每个位数
        # print(i,c)
        s += pow(int(c), p+i)
    if s % n == 0:
        return "%d,%d,%d" % (s, n,p)
    else:
        return False

def arv2(n,p):
    nums = map(int,str(n))   #把n的每位提出组成列表
    p_ = range(p,p+len(str(n)))   #按位设置对应的幂
    result = sum([pow(x,y) for x,y in zip(nums,p_)])
    return result/n  if result%n==0 else -1
    
for n in range(10,999):
    for p in range(10):
        if arv2(n,p) == -1:
            continue
        else:
            # print(n,p) 
            pass
# print(arv(89,1))
'''
8、for和else:当for正常退出时执行else,否则不执行else(例如for循环被break)
'''
for i in range(10):
    if i == 10:
        print('10 id found!')
        break
else:
    print('10 isn\'t found!')
'''
9、 with:工作于支持上下文管理协议（context management protocol）的对像，这个管理器就是在对象内实现了两个方法：__enter__() 和__exit__()
    with xx [as xx]:
    另外python库中还有一个模块contextlib，使你不用构造含有__enter__, __exit__的类就可以使用with：
    from contextlib import contextmanager

    @contextmanager
    def context():
        xxxx
    如：
        文件操作
        数据库链接
        锁
'''
import threading 

lock = threading.Lock()
with lock:  #无需加锁和解锁
    print('hhhh')

'''
10、列表生成式
'''
a = [(i,j) for i in range(10) for j in range(1, 10) if i != j]
#   先执行第一个for 在执行第二个for ，在if判断

b = [[i for i in range(10) if i != j] for j in range(1, 10)]
# 先执行第二个for 在执行第一个for 在执行if
# print(a)
# print(b)

'''
11、os
'''
import os
'''
os.getcwd() 获取当前工作路径
os.chdir('/bb/')  改变当前工作路径
'''
dirname = os.path.dirname(__file__)  #当前目录
base = os.path.basename(__file__)   #当前工作文件

print(dirname+base)
print(os.path.join(dirname,'/hello/',base)) #'/hello/' 可省略
print(os.path.splitext(base))    #路径+后缀
print(os.path.abspath(__file__))

'''
12、字符串格式化
'''
'#1、通过对应的键获取对应的值'

'%(a)s--%(b)s' % {"a": 1, "b": 2}
'输出结果是：1--2'

reply = "I'm %(name)s,now i study %(work)s!"

person = {'name':'John','work':'Python'}

print(reply % person)
"结果：I'm John,now i study Python! "
'''
#vars() #返回当前工作场景下的所有赋值键值对
'''
'#2 format 格式化  s.format(..)'
print('I am {name},I am {0},and now study {work}'.format(26, name='John', work='Python'))

'format 字典/列表加方法'

import sys
print('{1[name]} is working on {0.platform}'.format(sys, {'name':'John'}))
print('{person[name]} is working on {sys.platform}'.format(sys=sys, person={'name': 'John'}))

dict2 = {'name': 'John', 'work': sys.platform}
print('{0[name]} is working on {0[work]}'.format(dict2))

list2 = ['John','linux']
print('{0[0]} is working on {0[1]}'.format(list2))

'''
13、列表的操作
'''
'1、删除 del pop remove(element) pop(index)'
l = ['a', 'b', 'c', 'd']

del l[1]
del l[1:]
print(l)

'2、追加列表 append <==> l[len(l):] = n, l1+l2产生新的列表速度相对慢'

'''
14、字典
'''
'1、创建字典的方法'
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

dic = dict(zip(l2,l1))  #先利用zip构建键值对，在用dict转化成字典
print(dic)
'2、以集合的形式直接获取字典的键 (py3)'

key_set = dic.keys() & dic.keys()
print(key_set)

'''
15、元组
'''
'1、排序'

t = (2,1,4,3,5)
l = list(t)
l.sort() 
'list排序：list.xxx() 不需重新赋给新的变量，改变原列表，random.shuffle与列表的方法类似'
print(tuple(l)) #现转化为列表排序，在转化为元组

'''
16、文件操作
'''
import pickle

'pickle.dump（date,file） 将数据(二进制)写入文件\
 pickle.load(file) 将文件中的数据取出，返回原格式'

f = open('./pick_test.txt','wb')
data = [1,2,3,4,5]
for i in range(3):
    pickle.dump(str(data)+'\n',f)
f.close()

f = open('./pick_test.txt','rb')
while True:
    try:
        data = pickle.load(f)
        print(data,type(data))
    except EOFError as e:
        f.close()
        print(e.args[0])
        break
'struct 构造并打包解析二进制文件,pack打包，unpack解析'
import struct
a,b,c = 45,b'john',8
data = struct.pack('>i4sh',a,b,c) #i int类型，4s string类型长度为4，h short类型，类型之间相互意义对应
print(data)
data= struct.unpack('>i4sh',data) #前后的类型要一致
print(data)
 
'类似[],{},()'
a = [
    1,
    2,
    3
]

print(a)

'''
17、赋值
'''
s = [1,2,3,4]
l = 'abcd'
'变量前有一个*时，可匹配任意个数的变量，并将其组成列表，没有此项为空列表（函数的可变长参数）'
a,*b,c = s
*x,y,z = l
print(a,b,c,x,y,z)


'函数定义'
'1、默认参数'
def add(L=[1,2,3]):
    L.append('a')
    return L

for i in range(3):
    print(add())

"输出结果:\
    [1, 2, 3, 'a']\
    [1, 2, 3, 'a', 'a']\
    [1, 2, 3, 'a', 'a', 'a']"

"廖雪峰网站：Python函数在定义的时候，默认参数L的值就被计算出来了，即[1,2,3]\
，因为默认参数L也是一个变量，它指向对象[1,2,3]，每次调用该函数，\
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[1,2,3]了"

"个人理解：因为list是可变类型，每次执行函数时，改变是在L上进行，\
既L所引用的值发生了变化，所以下次在调用L的时候L已经发生了变化.\
若参数是不可变类型，L=1,在函数中虽然改变了L的值，但是实际上是改变了L的引用，\
所以原参数并没有变"


'2、可变参数'

def calc(*numbers):
    sum = 0
    print(numbers)  # 参数numbers接收到的是一个tuple
    for n in numbers:  
        sum = sum + n
    return sum

print(calc(1,2,3,4)) 
'使用可变参数，参数长度不固定，并且不用写成列表等形式'

'将一个列表或元组当做可变参数传递过去，只需在列表或者元组前面加上*'
list0 = [1,2,3,4]
print(calc(*list0))

'3、关键字参数'

'键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict'

def person(name, age, **kw):
    result = "name: %s, age: %s, other: %s"%(name, age, kw)
    return result

print(person('Bob', 35, city='Beijing'))
"结果：name: Bob age: 35 other: {'city': 'Beijing'}"

"将字典作为关键字参数传递到函数中,只需在字典前面加上**"
dict0 = {'city': 'Beijing', 'job': 'Teacher'}
print(person('Bob', 34, **dict0))

'4、命名关键字参数（限制关键字参数允许的参数名，如果参数不是可用参数名，则会报错）'
'a、关键字前面没有可变参数需使用*分隔开，*后面的为可以使用的关键字参数名'

def person1(name, age, *, city, job):
    return '%s is %s years old, in %s, work is %s'%(name, age, city, job)

print(person1('Tom', 23, **dict0))

'关键字参数签名有可变参数，不需要加*'
def person2(name, age, *args, city, job):
    return '%s, %s, %s, %s %s' %(name, age, args, city, job)

print(person2('Tom', 12, *list0, **dict0))

'尾递归：尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式'
'阶乘递归'

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1) #return 含有乘法表达式，所以不是尾递归

'尾递归'

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product) #return 只返回函数，表达式作为参数

"迭代器和可迭代对象"
'生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表'
'生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。\
 把list、dict、str等Iterable变成Iterator可以使用iter()函数。'
'可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。\
 可以使用isinstance()判断一个对象是否是Iterator对象。'

'类的定义'

'该类含有单个属性：宽、高和面积，宽高可读可写，面积只读'
class Screen(object):
    
    #__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称, 只能在此类中使用，若被继承则不起作用
    
    @property   #只能读，不能设置
    def width(self):
        return self._width  #前面加上_ 或者__ 表示私有属性，在外面不能直接调用

    @width.setter   #可以对属性进行赋值操作
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
 
    @property   #只读
    def resolution(self):
        return self._width * self._height

screen = Screen()
screen.height = 12
print(screen.height)

class Student(object):
    
    count = 0  # count是类属性，也可以被作为实例属性，但是实例属性不能改变类属性

    def __init__(self, name):
        self.name = name   #实例属性，
        Student.count += 1 #调用类属性 
                           #s = Student()   s.count 类属性作为实例属性调用                
    @property
    def cou(self):
        return self.count
    
    @cou.setter
    def cou(self, value):
        # Student.count = value
        self.count = value

student = Student('tom')
print(student.cou)
student.cou = 67
print(student.cou)
print(Student.count)


"类的继承"

class Car():  # 旧式类      Car(object) 新式类
    def __init__(self, name="q7", year=1998):
        self.name = name
        self.year = year

    def get_year(self):
        return self.year

    def get_name(self):
        return self.name 


class Audi(Car):
    def __init__(self, name, color):
        super().__init__(name) #要修改的属性，若不写则所有的属性都继承父类   
        # self.name = name
        self.year += 10
        self.color = color  #子类新添加的属性
    def get_name(self): #修改父类的方法
        return '#####%s' % self.name

class Daben(Car):
    def __init__(self, name, color):
        super(Daben, self).__init__()   #super的继承与父类没有太大的关系
             #super中写的是本身
        self.name = name
        self.color = color
        self.year += 10
    def get_params(self):
        return "!!!!!%s!!!!!!%s!!!!!%s"%(self.name, self.color, self.year)


au = Audi("a4","blue")
print(au.name, au.year, au.color, au.get_year(), au.get_name())  # a4 2008 2008 #####q7
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
ben = Daben("s500", "red")
print(ben.get_params(), ben.get_name(), ben.get_year())

'枚举'
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan.name) # Jan
print(Month.Jan.value) #1

"Month.__members__: mappingproxy({'Apr': < Month.Apr: 4 >,\
                                  'Sep': < Month.Sep: 9 >})"
for month, value in Month.__members__.items():
    print("%s ==>%s" %(month, value.value))

"类枚举"

from enum import unique
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.__members__) #同上
print(Weekday)
print(Weekday.Sun.value)  #0
print(Weekday.Sun.name) #Sun
week = Weekday(1)
print(week)  # <Weekday.Mon: 1>  <==>  Weekday.Mon
