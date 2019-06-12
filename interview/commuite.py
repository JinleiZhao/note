1、人们选择python的主要原因：面向对象、免费、可移植、功能强大(动态、内置对象类型、内置工具、第三方工具)、可混合、简单易用易学
2、什么是解释器：是一种让其他程序运行起来的程序，是代码与机器的计算机硬件之间的软件逻辑
3、python文件执行过程：py文件 -(解释器)-> PyCodeObject(字节码，写入到内存中) --> PVM(python虚拟机) -->运行结果 [-->.pyc(导入时存储在硬盘上)]
4、什么是字节码：是python将程序编译所得到的底层形式，自动将字节码存到.pyc文件中
5、什么时PVM：python虚拟机，时python运行时引擎解释编译得到的代码
6、作用域：在作用域中定义的变量，一般只在作用域中有效。 
    注：在if-elif-else、for-else、while、try-except\try-finally等关键字的语句块中并不会产成作用域
    类型：
        局部作用域(L)：函数中的变量。
        嵌套作用域(E)：两层函数(闭包)，L是定义在此函数内部的，E是定义在此函数的上一层父级函数的局部作用域。nonlocal修改
        全局作用域(G)：在模块（文件）层次中定义的变量，每个模块都有一个全局作用域。(全局作用域只限于单个模块文件内)/global 修改
        内置作用域(B)：系统固定模块定义的变量，如builtin模块内的变量
    搜索优先级：
        局部作用域 > 嵌套作用域 > 全局作用域 > 内置作用域
    例1：
        In [28]: ex = 'dadsa'  #全局

        In [29]: def fun1():
            ...:     ex = "dad"   #局部
            ...:     print(ex)
            ...:

        In [30]: def fun2():
            ...:     ex = "qwe"  #局部，不是闭包，所以不是E
            ...:     fun1()
            ...:

        In [31]: fun2()
        >>> dad   #优先局部 > 找到

        In [32]: def fun1():
            ...:     #ex = "dad"
            ...:     print(ex)
            ...:

        In [33]: fun2()
        >>>  dadsa # 优先局部未找到 >  嵌套未找到 > 全局

    例2：
        In [37]: bx = 'da'   #全局

        In [38]: def outer1():
            ...:     bx = 'qw'  #嵌套
            ...:     def inner():
            ...:         print(bx)
            ...:     return inner
            ...:

        In [39]: outer1()()
        >>>qw   #优先局部未找到 > 嵌套找到

        In [40]: def outer1():
            ...:     bx = 'qw'
            ...:     def inner():
            ...:         bx = 'zx'  #局部
            ...:         print(bx)
            ...:     return inner
            ...:

        In [41]: outer1()()
        >>>zx

    例3：
        In [54]: dd = 12

        In [56]: def fun5():
            ...:     print(dd)

        In [57]: fun5() #局部未找到 > 找全局找到
        >>>12

        In [58]: def fun5():
            ...:     print(dd)
            ...:     dd = 13

        In [59]: fun5() #抛错，UnboundLocalError: local variable 'dd' referenced before assignment

        'Python中的模块代码在执行之前，并不会经过预编译，但是模块内的函数体代码在运行前会经过预编译，\
                                    因此不管变量名的绑定发生在作用域的那个位置，都能被编译器知道。'
        #在fun5中找到了dd所以使用局部变量，所以应该先定义在使用，所以抛错

7、python函数参数的类型：
    必备参数：须以正确的顺序传入函数。调用时的数量必须和声明时的一样  def func(name)
    关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
                允许函数调用时参数的顺序与声明时不一致  def func(**kwargs)
    默认参数：默认参数的值如果没有传入，则被认为是默认值  def func(name='zhangsan')
    不定长参数： def func(*args)

8、匿名函数 lambda  [参数/可选]：表达式
    eg1:嵌套
    
        def sum_outer(x=0):
            def sum_inner(y):
            return x + y
        return sum_outer

        sum_outer()(4) => 4
        '等价'                               #test_lamdba2 <==> sum_outer 
        def test_lamdba2(x=0):               #lambda y <==> sum_inner(y)
            return lambda y: x + y           

        test_lamdba2()(4) => 4
        '等价'
        a = lambda x=0:lambda y: x+y
        a()(4)  => 4

    eg2: for + lambda:
        '第一种'
        In [43]: lam1 = [lambda x: x*i for i in range(9)]
        In [44]: lam1[0](2)
        Out[44]: 16
        In [45]: lam1[8](2)
        Out[45]: 16
        
        '因为在每次循环中 lambda函数都未绑定 i 的值，所以直到循环结束，i 的值为8，并将 lambda 中所用到的 i 值定为 8'
        '等价'

        def func():
            fs = []
            for i in range(9):
                def lam(x):
                    return x*i
                fs.append(lam)
            return fs
        
        lam1_ = func()
        lam1_[0](2)  => 16
        lam1_[8](2)  => 16

        '第二种'
        lam2 = [lambda :i for i in range(9)]  
        In [56]: lam2[0]() #lambda接受传递参数为空，所以无需传参
        Out[56]: 8

        '第三种'

        lam3 = [lambda x=i:x for i in range(9)]
        In [60]: lam3[0]()
        Out[60]: 0
        In [61]: lam3[8]()
        Out[61]: 8

        '每次循环中lambda函数都将i值绑定到了x上，所以直到循环结束，不同地址的 lambda 函数的x值为都不一样'
        '等价'

        def func():
            fs = []
            for i in range(4)
                def lam(x=i):   
                    return x   #
                fs.append(lam)
            return fs

        '第四种，和第三种写法相似，结果不同'

        In [62]: lam3 = [lambda x =i:i for i in range(9) ]
        In [63]: lam3[8]()
        Out[63]: 8
        In [64]: lam3[0]()
        Out[64]: 8

        '原因：虽然将i绑定到x上了，但是内部并未调用x，二十调用的i,所以等到循环结束i值位8'

9、浅拷贝和深拷贝的区别：
    copy/[:]浅拷贝，没有拷贝子对象，所以原始数据子对象改变，新数据子对象会改变
    深拷贝，包含对象里面的子对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变

10、python可变数据类型和不可变数据类型及原理
    不可变类型：数字、字符串和元组
            如果改变了变量的值，相当于新建了一个对象，变量引用的对象地址改变
    可变类型：列表、字典
            改变了变量的值，不会新建对象，变量引用的对象地址不改变

11、列表生成器： 运行方向:运行从左向右
    for / if
    [x for x in range(10) if x > 5]   
    for / for
    [(x, i) for x in range(10) for i in range(x,10)]
    for / for / if 
    [x+str(j) for x in 'abcd' for j in range(10) if j > 5]