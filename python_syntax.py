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
            print(n,p) 
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

