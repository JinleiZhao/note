'''
迭代器含有__iter__, __next__
可以使用next()
'''

class MyRange(object):
    def __init__(self, n):
        self.idx = 0
        self.n = n
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()


range_ = MyRange(5)
print(type(range_))
# for i in range(10):
#     print(next(range_))

for i in range_:
    print('i',i)
for j in range_:
    print('j',j)

'上述两次循环只有第一次有输出，解决：分离迭代对象与可迭代对象'

class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)

class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):    #py2 中是next
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

            
zrange = Zrange(3)
print(zrange is iter(zrange), dir(zrange))
# next(zrange)  #zrange 只是可迭代对象，不能调用next()函数
print([i for i in zrange])
print([i for i in zrange])
