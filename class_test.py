class Student:
    #def __init__(self, name, score):
    #    self.name = name
    #    self.__score = score   #__value/_value  则此属性不能直接被赋值，只能通过下面的方法

    @property  # @property装饰器的作用是吧方法变成属性调用
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    # 第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，用@score.setter装饰
    # 第二个是第一个装饰器的副产品

    @property
    def name(self):
        return 100 - self.__score  #此name方法不能赋值，所以__name无法读取，直接调用会报错

    # @name.setter
    # def name(self, name):  # 若没有此方法则name只有可读属性
    #     self.__name = name

student = Student()   #实例化，需要加（）,若不加（），则实际上是个类，不是一个实例
#student= Student  实际是将类Student指向了类student

student.score = 12
print(student.score)
print(student.name)
# student.name = 33



class NewClass(object):
    num_count = 0  # 所有的实例都共享此变量，即不单独为每个实例分配

    def __init__(self, name): #构造函数
        self.name = name
        #self.num_count +=1   #则num_count不是相当于全局变量
        NewClass.num_count += 1  #则num_count相当于全局变量
        print(name, NewClass.num_count)

    def __del__(self):  #析构函数
        NewClass.num_count -= 1
        print("Del", self.name, NewClass.num_count)

    def test():
        print("aa")


aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("Aaaa")
print("Over")
#当分别实例化三个对像的时候首先会执行__init__既构造函数，则会执行print
#当执行到print('Over')时程序执行完毕，就会自动执行析构函数


class ss(object):   #此类只有a、b两个属性，但是可以给它没有的c属性赋值
    def __init__(self, a, b):
        self.a = a
        self.b = b

s = ss(1,2)
print(s.a,s.b)
s.c = 2
print(s.c)

class tt(object):
    __slots__ = ('a','b')  #限制了tt只能有a，b两个属性
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = tt(1,2)
print(t.a,t.b)
#t.c = 5


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B(A):
    __slots__ = ('c',)
    def __init__(self, a, b, c):
        # A.__init__(self, a, b)
        super(B,self).__init__(a, b)
        self.c = c  #B中只有c这个属性，若不基层A则b.a,会报B没有这个属性

b = B(3,4,3)
print(b.a,b.b,b.c)


class Person(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, friend):
        print('My name is %s,my friend is %s'%(self.name,friend))

person = Person('zhang')
person('li')