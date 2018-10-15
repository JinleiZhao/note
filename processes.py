import os

#进程
'''
pid = os.fork()   #linux/unix中可用
print(pid)
if pid == 0:
    print('I am child process (%s) and my parent is %s.' %
          (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
from multiprocessing import Process
'''
def run_proc(name):
    print('Run child process %s(%s)'%(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s'%os.getpid())
    p = Process(target=run_proc, args=('test',))  #创建子进程实例
    print('Child process will start') 
    p.start()     #start启动
    p.join()      # 等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end')
'''    

from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run task %s(%s)...'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.'%(name, (end-start)))

'''
if __name__ == '__main__':
    st = time.time()
    print('Parent process %s.'%(os.getpid()))
    p = Pool(4)   #默认大小是cpu核数
    for i in range(9):
        # apply_async 是异步非阻塞的。apply方法是阻塞的
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess  done...')
    p.close()  # join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()  # Pool对象调用join()方法会等待所有子进程执行完毕
    en = time.time()
    print('All process done use %0.2f second!'%(en-st))
'''

import subprocess
'''
if __name__ == '__main__':
    print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # r = subprocess.call('nslookup www.python.org', shell=True)
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,\
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'www.python.org\nexit')   #相当于nslookup命令行下输入www.python.org
    print(output.decode('utf-8'))
    print('Exit code:',p.returncode)
    # print('Exit code:',r)
'''

#进程间通信 Process
from multiprocessing import Process, Queue

def write(q):
    print('Process to write:%s' %(os.getpid()))
    for value in ['a','b','c']:
        print('Put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' %os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.'%value)
'''
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()   #等待pw结束
    pr.terminate()  #pr里面是死循环，无法等待其结束，只能强行终止
'''

#进程间通信 Pool
from multiprocessing import Pool, Queue, Manager
import os 

def run_proc(name, q): 
    print('Run Child process %s (%s)' % (name, os.getpid()))    
    q.put('value') 

def get_value(q):
    value = q.get(True)
    print('Get %s from queue.' % value)
    
    
if __name__ == '__main__': 
    print('Parent process %s.' % os.getpid())    
    q = Manager().Queue()    
    p = Pool(2)    
    for l in [1, 2]:
        p.apply_async(run_proc, args=(l, q)) 
        print('Child Process will start')    
    for i in range(2):
        p.apply_async(get_value, args=(q,))
    p.close()    
    p.join() 
    print('Child process end.') 
    # for i in [1,2,3]:
    #     print(q.get(timeout=3))


