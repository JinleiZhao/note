from myThread import MyThread
from time import ctime, sleep

def fib(x): #斐波那契
    sleep(0.005)
    if x < 2: return 1
    return fib(x-1)+fib(x-2)

def fac(x):#阶乘
    sleep(0.1)
    if x < 2 : return 1
    return x*fac(x-1)

def sum_(x):#累加
    sleep(0.2)
    if x < 2 : return  1
    return x + sum_(x-1)

funcs = [fib, fac, sum_]
x = 12

def main():
    funcindex = range(len(funcs))

    print('**** SINGLE THREAD')
    for i in funcindex:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](x))
        print(funcs[i].__name__, 'finished at:', ctime())
    
    print('\n ***** MULTIPLE THREADS')
    threads = []
    for i in funcindex:
        t = MyThread(funcs[i], (x,), funcs[i].__name__)
        threads.append(t)
    
    for i in funcindex:
        threads[i].start()
    
    for i in funcindex:
        threads[i].join()
        print(threads[i].getResult())
    
    print('all Done')

if __name__ == '__main__':
    main()