import time
from threading import Thread

def change_time(second):
    hours = second // 3600
    mins = second % 3600 // 60
    sec = second % 3600 % 60 // 60
    return hours,mins,sec

def start_time(st, name, stop=True):
    while stop:
        now = time.time()
    second = now - st
    hours, mins, sec =  change_time(second) 
    print('%s task time is %s:%s:%s'%(name, hours, mins, sec))

def main():
    st = time.time()


