import time
import threading

def change_time(second):
    hours = second // 3600
    mins = second % 3600 // 60
    sec = second % 3600 % 60 // 60
    return hours,mins,sec

def start_time(st, name, stop=True):
    while stop:
        now = time.time()
    second = now - st
    hours, mins, sec = change_time(second) 
    print('%s task time is %s:%s:%s'%(name, hours, mins, sec))

def main():
    st = time.time()
    timers = []
    for i in range(10):
        t = threading.Thread(target=start_time, args=(st, 'player%s'%i,True))
        timers.append(t)
    for th in timers:
        th.start()



