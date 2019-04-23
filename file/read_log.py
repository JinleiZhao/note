from time import ctime, sleep
def read_log(log):
    with open(log, 'r') as f:
        while True:
            # data = f.read(512)
            data = f.readline()
            sleep(0.1)
            if data:
                yield data
            else:
                return None

# print(list(read_log('log.log')))
def write_log():
    with open ('grep_log', 'a') as f:
        for log_file in ['log.log', 'log1.log']:
            for i,log in enumerate(read_log(log_file)):
            # print(i+1,'time read log is:', log)
                if '123' in log:
                    f.write(log)
            f.write('\n')
         
import threading

class MyThreading(threading.Thread):
    def __init__(self, func, args, name):
        super(MyThreading,self).__init__()
        self.name = name
        self.args = args
        self.func = func
    
    def run(self):
        self.write_log()

    def write_log(self):
        print(self.name, 'is start now:', ctime())
        with open('grep_log', 'a') as f:
            for log in self.func(*self.args):
                if '123' in log:
                     f.write(log)
        print(self.name, 'is done now',ctime())

def main():
    log_files = ['log.log', 'log1.log']
    threads = []
    print('all start now:', ctime())

    for i in range(len(log_files)):
        t = MyThreading(read_log, (log_files[i],), log_files[i])
        threads.append(t)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    print('all run done now', ctime())

if __name__ == "__main__":
    main()
    
