from urllib import request, error, parse, robotparser
import json
# urllib.request可以用来发送request和获取request的结果
# urllib.error包含了urllib.request产生的异常
# urllib.parse用来解析和处理URL  
# urllib.robotparse用来解析页面的robots.txt文件
print('1\###########################################')
from urllib.request import urlopen
# urllib.request.urlopen() 发送请求，获取到的数据为bytes需用decode('utf-8')解码
req = urlopen('https://www.baidu.com')  
#req是response对象含有read()、readinto()、getheader(name)、
# getheaders()、fileno()等函数和 msg、version、status、reason、debuglevel、closed 等属性。
print(req.getheaders()) 
data = req.read().decode('utf-8') #返回网页内容
print(type(req),data)
#urlopen 更多参数:
  #urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
   # data需是字节型bytes，可以用urllib.parse.urlencode(data).encode('utf-8')转化成字节
   #context 参数，它必须是 ssl.SSLContext 类型，用来指定 SSL 设置。cafile 和 capath 两个参数是指定CA证书和它的路径，这个在请求 HTTPS 链接时会有用
print('2\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
from urllib.parse import urlencode
#对data转化成字符串（将中文转化成url形式），在进行编码
data = {'word':'hello'}
data = urlencode(data).encode('utf-8') # 或bytes(urlencode({'word': 'hello'}), encoding='utf8')  
response = urlopen('http://httpbin.org/post', data=data)#加入data参数后为post请求,传递的参数在form中
print(response.read().decode('utf-8'))

print('3\$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

from urllib.request import Request

req = Request('https://www.baidu.com')
# req.add_header(headers)
response = urlopen(req)
print(response.read().decode('utf-8'))

print('4\%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

#Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
#data字节型
#headers请求头是个字典，也可以通过Request对象add_header()添加，请求头如User-Agent是伪装浏览器访问
headers = {
    #伪装一个火狐浏览器
    "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host": 'httpbin.org' 
}
url = "http://httpbin.org/post"
dict = {
    "name": "Germey"
}
data = urlencode(dict).encode('utf-8')
req = Request(url=url, data=data, headers=headers, method="POST")
response = urlopen(req)
print(json.load(response))  #response对象需要用load，(??字符创字节用loads)
print('json')
# print(response.read().decode("utf-8"))

print('5***************************')

from urllib.request import BaseHandler
'''
HTTPDefaultErrorHandler 用于处理HTTP响应错误，错误都会抛出 HTTPError 类型的异常。
HTTPRedirectHandler 用于处理重定向。
HTTPCookieProcessor 用于处理 Cookie 。
ProxyHandler 用于设置代理，默认代理为空。
HTTPPasswordMgr 用于管理密码，它维护了用户名密码的表。
HTTPBasicAuthHandler 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题
'''
#代理
'''
import urllib.request
proxy_handler = urllib.request.ProxyHandler({  #设置代理，字典格式
    'https': 'https://221.6.85.171:80'
})
# build_opener() 方法利用这个 Handler 构造一个 Opener
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('https://www.baidu.com')  # Opener 的 open() 方法打开链接
print(response.read())
'''
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
data = parse.urlencode(data).encode('utf-8')
proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
page = opener.open(url, data).read()
page = page.decode('utf-8')
print(page)

print('6^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
import http.cookiejar
import urllib.request
cookie = http.cookiejar.CookieJar()
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar【LWPCookieJar】(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True) #把cookie以文本的形式保存
for item in cookie:
   print(item.name+"="+item.value)
