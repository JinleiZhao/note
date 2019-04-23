#!/usr/bin/python

import os
import subprocess
#import sys

#os.system('export ALL_PROXY=""')
#os.system("export all_proxy=\"\"")

#os.system('ls')
		
os.environ["ALL_PROXY"]=""
#os.system('env')
#os.putenv('ALL_PROXY','')
os.system('cd /home/yaya/Desktop/promoter-admin')
#os.environ['PWD'] = '/home/yaya/Desktop/promoter-admin'
#print(os.environ['PWD'])
os.system('git status')
#print(os.environ["ALL_PROXY"])
#subprocess.Popen('export',close_fds=True,shell=True,env=None)
#print(os.environ)
