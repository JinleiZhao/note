import re

s = '''
123 3411,
1e23,  1231,
 3214
'''

pattern = re.compile('[\d|\w]{1,4}', re.M)

strs = pattern.findall(s)

print(strs)