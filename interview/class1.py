'class 的__new__ 和__init__'
'__new__是在类实例化时执行__init__之前执行的'

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
    def run(self):
        print('name',self.name)
    
myclass = MyClass("param", 'zhangsan')
myclass.run()
'''
This is new func
Bye
This is init func param zhangsan
'''

'新式类和旧式类'
'新式类广度优先'
#eg：
class A:
    var =1

class B(A):
    var = 2

class C(A):
    pass

class D(C,B):
    pass

d = D()
print(d.var)
#Out[7]: 2  D > C > B  => 2
'旧式类深度优先'
#Out[7]: 2  D > C > A  => 1

"""
深度优先算法：

（1）访问初始顶点v并标记顶点v已访问。
（2）查找顶点v的第一个邻接顶点w。
（3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
（4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。
（5）继续查找顶点  w的下一个邻接顶点wi  ，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。

广度优先算法：

（1）顶点v入队列。
（2）当队列非空时则继续执行，否则算法结束。
（3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
（4）查找顶点v的第一个邻接顶点col。
（5）若v的邻接顶点col未被访问过的，则col入队列。
（6）继续查找顶点  v的另一个新的邻接顶点col  ，转到步骤（5）。直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。
"""

class MyList:
    '''自定义一个可迭代对象'''
    def __init__(self):
        self.items = []
    
    def add(self, val):
        self.items.append(val)
    
    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator
    
class MyIterator:
    '''定义一个供可迭代对象MyList使用的迭代器'''
    def __init__(self, mylist):
        self.mylist = mylist
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.mylist.items):
            item = self.mylist.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self

mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)

print(type(mylist))
for num in mylist:
    print(num)
