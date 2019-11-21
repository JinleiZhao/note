#coding=utf-8

from selenium import webdriver
import time
import linecache
import logging
import urllib2


logging.basicConfig(filename=r"C:/Users/yaya/Desktop/log.txt", filemode="a", 
    format="%(message)s", level=logging.ERROR)

def now_time():
    import datetime
    now_time = datetime.datetime.now()
    return now_time.strftime('%Y-%m-%d %H:%M:%S')

class Driver():
    def __init__(self, username, passwd):
        #http://npm.taobao.org/mirrors/chromedriver/     chromedirver download
        self.driver = webdriver.Chrome(r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        self.driver.implicitly_wait(15)
        self.username = username
        self.passwd = passwd
        self.login_url = 'http://www.baidu.com'
        self.n = 0
        self.login_user()
        #self.browse_url()

    def login_user(self):

        self.driver.get(self.login_url)
        try:#m
            self.driver.find_element_by_id('login')
        except:
            # check = self.driver.find_element_by_id('logout')
            # check.click()
            # self.driver.get(self.login_url)
            pass
        finally:
            # self.driver.find_element_by_id('username').clear()
            # self.driver.find_element_by_id.send_keys(self.username)
            # self.driver.find_element_by_id('passwd').clear()
            # self.driver.find_element_by_id('passwd').send_keys(self.passwd)
            # time.sleep(1)
            # self.driver.find_element_by_id('login').click()
            self.login_handle = self.driver.current_window_handle
            self.start_time = time.time()
            msg = "%s login at: %s"%(self.username, now_time())
            logging.error(msg = msg)
            time.sleep(1)
            # self.driver.find_element_by_id('submit').click()
            # time.sleep(1)
            self.browse_url()

    def browse_url(self):
        self.driver.execute_script('window.open()')
        for i in range(3):
            url = linecache.getline('url.txt', i+1)
            self.driver.switch_to_window(self.driver.window_handles[1])
            try:
                self.driver.get(url)
                self.n = self.n+1
                msg = 'open %s at %s'%(url[:-1], now_time())
                logging.error(msg = msg))
            except Exception as e:
                print 'dasd',e.message
                pass
            time.sleep(2)
        self.quit_user()
        #self.driver.close()

    def quit_user(self):
        #self.driver.get(self.login_url)
        handles = self.driver.window_handles
        for handle in handles:
            if handle == self.login_handle:
                self.driver.switch_to.window(handle)
        time.sleep(1)
        self.driver.find_element_by_id('kw').send_keys('python')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        msg = '%s logout at %s, total time %s S,total number %s'%(self.username, now_time(),int(time.time()-self.start_time),self.n)
        logging.error(msg=msg)
        logging.error(msg='--------------------------------------------------------------------------------')
        self.driver.quit()
