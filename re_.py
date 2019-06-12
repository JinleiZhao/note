import re

s = '''123 3411,
1e23,  1231,
 3214, 12qq2
'''

pattern = re.compile('(\d{3,4}|\d{0,4}[a-z]\d{0,4})', re.M)

#strs = pattern.findall(s)
#strs = pattern.search(s)
#print(strs.groups())  #groups[返回元组形式]\group 使用于match或者search
strs = re.match(pattern, s)
print(strs.group())  #返回完整匹配,各个子组组成一个字符串
print(strs.group(1))  #返回第一个匹配内容

import os

f = os.popen('tasklist /nh', 'r')  #/nh 不显示标题
for eachline in f:
    #print(eachline.rstrip())
    print(re.findall(r'([\w.]+(?:[\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
            eachline.rstrip()))
f.close()
