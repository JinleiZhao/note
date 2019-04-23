#线程
import time, threading

lock = threading.Lock()
def loop():
    print('Thread %s is running...'%threading.current_thread().name)
    for i in range(5):
        print('Thread %s >> %s'%(threading.current_thread().name, i))
        time.sleep(1)
    print('Thread %s ended.'%threading.current_thread().name)

print('Thread %s is running...' %threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)


'''666666666666666666666666666666666666666666666666666666666'''

import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)%s' % (std, threading.current_thread().name, time.time()))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    time.sleep(1)
    process_student()

a = time.time()
thread = []
for i in range(10):
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-%s'%i)
    # t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    thread.append(t1)
for i in thread:
    i.start()
for i in thread:
    i.join()
print('end-time:%s'%(time.time()-a))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

