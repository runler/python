import requests
from urllib import request,parse
from http import cookiejar
import ssl
from bs4 import BeautifulSoup
import re
import json
# res = requests.get( 'http://190.5.58.1/ybhos/toLogon.do')
# res.encoding = 'utf-8'
# print(res.text)
# data=re.search('{\"data\".*', res.text)
# jsondata=json.loads(data.group().rstrip(');'))
# for news in jsondata['data']:
#  print('标题：'+news['title']+'---作者：'+news['author'])

#取消SSL验证
ssl._create_default_https_context=ssl._create_unverified_context

#定义请求管理器
#url.request.urlopen() 并不能保存cookie
http_handler=request.HTTPHandler()
https_handler=request.HTTPSHandler()
cookie=cookiejar.CookieJar()
#cookie管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
##生成一个请求管理器
opener=request.build_opener(https_handler,http_handler,cookie_handler)

# 登录
def login():
    #（1）
    login_url='http://190.5.58.1/ybhos/toLogon.do'
    data={
        'username':'42486506700',
        'password':'12345678'
    }
    data=parse.urlencode(data)
    headers = {
        "Content-Length": len(data),
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    req=request.Request(url=login_url,data=bytes(data,encoding='utf-8'),headers=headers)

    # 2
    response=opener.open(req)
    html=response.read()
    # html.encoding = 'utf-8'
    html=html.decode('GBK')
    print(html)

if __name__=='__main__':
    login()