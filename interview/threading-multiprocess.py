'''
首先来说说他两个的区别，进程是资源分配的最小单位，线程则是CPU调度的最小单位，多进程不能共享全局变量，
当使用全局变量的时候势必会造成，race condition(竞争)，而多线程则可以共享全局变量，对于大量需要CPU工作的时候，
进程就显得大有优势，因为多线程需要CPU来不停切线程换大量时间都消耗在，切换线程上，
而对于IO操作上（比如文件存储，网络爬虫），多线程就有巨大优势。
'''
from multiprocessing import process  #进程
import threading   #线程

'''
进程和线程的关系：
(1)一个线程只能属于一个进程，而一个进程可以有多个线程，但至少有一个线程。
(2)资源分配给进程，同一进程的所有线程共享该进程的所有资源。
(3)CPU分给线程，即真正在CPU上运行的是线程。
'''
'''
并行并发：
    并行处理（Parallel Processing）是计算机系统中能同时执行两个或更多个处理的一种计算方法。
    并发处理(concurrency Processing)：指一个时间段中有几个程序都处于已启动运行到运行完毕之间，
        且这几个程序都是在同一个处理机(CPU)上运行，但任一个时刻点上只有一个程序在处理机(CPU)上运行
    并行是并发的子集
'''
'''
协程：
    子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
    协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
    python中协程是通过生成器实现
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

# c = consumer()
# produce(c)
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')