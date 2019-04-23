#!/home/yaya/.pyenv/plugins/python

'''
列出除了os_mk_dir中的test[1-9]
'''
import os
import fnmatch

exit_dir = 'os_mk_dir'
file_list = []
for root,dirnames,filenames in os.walk(os.path.expanduser('~/pyenv_test')):
    #print(6)
    for filename in filenames:
        #print(2)
        if fnmatch.fnmatch(filename,'*[1-9]'):
            #print(1)
            file_list.append(os.path.join(root,filename))
    if exit_dir in dirnames: #移除不遍历的目录
        #print(3)
        dirnames.remove(exit_dir)

print(file_list)
