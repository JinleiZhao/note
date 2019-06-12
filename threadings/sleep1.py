#派生Thread子类，并创建子类的实例

import threading
from time import sleep, ctime

loops = [4,2]

class MyThread(threading.Thread):   #继承thread类
    def __init__(self, func, args, name = ''):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args
    
    # def __call__
    def run(self):   #Threa中的方法
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    for i in range(len(loops)):   #生成对应的线程，统一放在列表中
        # t = MyThread(loop, (i, loops[i]), loop.__name__)
        t = threading.Thread(target=loop, args=(i, loops[i]), name=loop.__name__)
        threads.append(t)

    for thread_ in threads: #执行所有的线程
        thread_.start()

    for thread_ in threads: #等待线程结束
        thread_.join()
    print("all Done at:", ctime())

if __name__ == '__main__':
    main()
