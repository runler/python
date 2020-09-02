#爬虫登录开心网的账号，并且爬取个人主页内容

from urllib import request,parse
from http import cookiejar
import ssl

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

#登录
def login(account,password):
    #（1）
    login_url='https://security.kaixin001.com/login/login_post.php'
    data={
        'email':account,
        'password':password
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
    html=html.decode('utf-8')
    # print(html)


    # 在一个页面html中查找特定子串 uid=
    location = html.find('uid=')
    print(location)
    uid=html[location+4:location+4+9]
    print(uid)

    gerenpage(uid)

def gerenpage(uid):
    # basu_url='http://www.kaixin001.com/home/?_profileuid=181701569&t=71'
    #扩展功能，任何登录的个人都可以访问属于他们自己的个人主页
    basu_url = 'http://www.kaixin001.com/home/?_profileuid=%s&t=71%(uid)'
    headers = {

        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    req = request.Request(url=basu_url, headers=headers)

    # 2
    response = opener.open(req)
    html = response.read()
    html = html.decode('utf-8')
    with open('kaixingerenpage','w',encoding='utf-8') as f:
        f.write(html)
    print(html)




if __name__=='__main__':
    account = input("请输入账号：")
    password = input("请输入密码：")
    login(account, password)

    #登录后访问个人主页
    # gerenpage(uid)
