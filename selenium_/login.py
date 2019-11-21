from datetime import datetime
import json
import time
from driver import Driver
import logging

'''
def get_time():
    now_time = datetime.now()
    week =  now_time.weekday() + 1
    hour = now_time.hour
    minute = now_time.minute
    sencond = now_time.second
    return week,hour,minute,sencond

def do_driver(week):
    with open(r'C:/user.json', 'r') as u_j:
        user_dict = json.load(u_j)
    today_users = user_dict.get(str(week), None)
    if today_users:
        for today_user in today_users:
            driver = Driver(today_user['username'], today_user['passwd'])
            time.sleep(5)

def run():
    run_time_list = ['9:35:0', '13:30:0','17:30:0']
    while True:
        args = get_time()
        now_time_str = '%s:%s:%s'%(args[1],args[2],args[3])
        logging.info(msg=now_time_str)
        if now_time_str in run_time_list:
            logging.info(msg='run at %s'%now_time_str)
            do_driver(args[0])
        elif now_time_str == '18:30:0':
            break
        time.sleep(1)
'''

def run():
    import random
    week = datetime.now().weekday()+1
    if week in [1,2,3,4,5]:
        with open(r'E:/WorkNote/note/selenium_/user.json', 'r') as u_j:
            user_dict = json.load(u_j)
        today_num = random.sample(user_dict.keys(),2)
        today_users = [user_dict[num] for num in today_num]
        print "today_user__",today_users
        for today_user in today_users:
            driver = Driver(today_user['username'], today_user['passwd'])
            time.sleep(3)
