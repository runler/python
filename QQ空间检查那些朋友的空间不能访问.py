import csv
from urllib import parse
from selenium import webdriver
import requests
import json
from json import loads
import time
import datetime

QQ_count = 'QQ账号'
QQ_password = 'QQ密码'

def get_key_values(body, key, end=';'):
    return body[body.find(key) + len(key): body.find(';', body.find(key))]


def get_key(cookies):
    key = get_key_values(cookies, 'p_skey=')
    h = 5381
    for i in key:
        h += (h << 5) + ord(i)
    return h & 2147483647


def web_login_cookie():
    driver = webdriver.Chrome()
    qq_account = QQ_count
    qq_password = QQ_password
    login(driver, qq_account, qq_password)
    time.sleep(10)
    driver.get('https://user.qzone.qq.com/{}'.format(qq_account))
    cookie = ''
    for elem in driver.get_cookies():  # 记录相关的Cookie
        cookie += elem["name"] + "=" + elem["value"] + ";"
    return cookie


def login(driver, qq_account, qq_password):
    driver.maximize_window()
    driver.get('http://user.qzone.qq.com')
    driver.switch_to.frame('login_frame')
    time.sleep(1)
    driver.find_element_by_id("switcher_plogin").click()
    driver.find_element_by_id("u").send_keys(qq_account)
    time.sleep(2)
    driver.find_element_by_id("p").send_keys(qq_password)
    time.sleep(2)
    driver.find_element_by_id("login_button").click()


def send_requests(req, headers, url, params=None):
    if None != params:
        url = url + parse.urlencode(params)
    page = req.get(url=url, headers=headers)
    return page.text


def get_each_str(req, uin, headers):
    each_url = 'https://user.qzone.qq.com/{}'.format(uin)
    page = req.get(url=each_url, headers=headers)


def friend_db(dicts, name=''):
    if len(str(dicts['birthyear'])) < 4:
        dicts['birthyear'] = '1900'
    if dicts['birthday'][1:2] == '0':
        dicts['birthday'] = '01-01'
    if len(dicts['signature']) > 70:
        dicts['signature'] = ''
    friend_db_dict = {
        'friendInfo': [
            dicts['uin'], name, dicts['age'], '男' if dicts['sex'] == 1 else '女'
            , datetime.datetime.strptime(str(dicts['birthyear']) + '-' + str(dicts['birthday']), '%Y-%m-%d')],
        'friendPlace': [
            dicts['uin'], dicts['company'], dicts['career'], dicts['hco'] + dicts['hp'] + dicts['hc'],
                                                             dicts['country'] + dicts['province'] + dicts['city'],
                                                             dicts['cco'] + dicts['cp'] + dicts['cc'], dicts['cb']],
        'friendNet': [
            dicts['uin'], dicts['nickname'], dicts['spacename'], dicts['desc'], dicts['signature']]
    }
    with open('data.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [friend_db_dict['friendInfo'][0], friend_db_dict['friendInfo'][1], friend_db_dict['friendInfo'][2],
             friend_db_dict['friendInfo'][3], friend_db_dict['friendInfo'][4], friend_db_dict['friendPlace'][0],
             friend_db_dict['friendPlace'][1], friend_db_dict['friendPlace'][2], friend_db_dict['friendPlace'][3],
             friend_db_dict['friendPlace'][4], friend_db_dict['friendPlace'][5], friend_db_dict['friendPlace'][6],
             friend_db_dict['friendNet'][0], friend_db_dict['friendNet'][1], friend_db_dict['friendNet'][2],
             friend_db_dict['friendNet'][3], friend_db_dict['friendNet'][4]]
        )


def main():
    """主要操作

    :return: void
    """
    req = requests.session()
    headers = {'host': 'h5.qzone.qq.com',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.8',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '59.0.3071.115 Safari/537.36',
               'connection': 'keep-alive'}
    cookie = web_login_cookie()
    print('cookie', cookie)
    g_tk = get_key(cookie)
    qzonetoken_friend = get_key_values(cookie, 'ptcz=')
    uin_friend = get_key_values(cookie, 'ptui_loginuin=')
    rd_friend = get_key_values(cookie, '_qpsvr_localtk=')
    print('friend_data', 'qzontoken:%s;uin:%s;rd:%s' % (qzonetoken_friend, uin_friend, rd_friend))
    headers['Cookie'] = cookie
    params_friend = {"uin": uin_friend, "fupdate": 1, "action": 1, "do": 1, "g_tk": g_tk, "rd": rd_friend,
                     'qzonetoken': qzonetoken_friend}
    url_friend = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?'
    data_friend_str = send_requests(req, headers, url_friend, params=params_friend)
    data_friend_dict = loads(data_friend_str[0 + len('_Callback('):data_friend_str.find(');')])
    print('data_friend_dict: ', data_friend_dict)
    if data_friend_dict['code'] != 0:  # code = -3000 message = '请先登录'
        time.sleep(10)
        main()
    else:
        data_friend_list = list(data_friend_dict['data']['items_list'])
        for i in range(len(data_friend_list)):
            each_uin = data_friend_list[i]['uin']
            each_url = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/user/cgi_userinfo_get_all?'
            params_each = {"uin": each_uin, "fupdate": 1, "vuin": uin_friend, "g_tk": g_tk, "rd": rd_friend,
                           'qzonetoken': qzonetoken_friend}
            time.sleep(1)
            data_each_str = send_requests(req, headers, each_url, params_each)
            try:
                data_each_dict = loads(data_each_str[0 + len("_Callback("):data_each_str.find(");")])
            except json.decoder.JSONDecodeError as e:
                with open('leak.txt', 'a', encoding='utf8') as file:  # 数据持久化，统计错误信息
                    file.write('except: ' + str(each_uin) + " " + data_friend_list[i]['name'] + " " + e.msg + "\n")
                    continue
            print('data_each_dict: ', data_each_dict)
            if data_each_dict['code'] == 0:  # code = -4009 message = '没有访问权限'
                friend_db(data_each_dict['data'], name=data_friend_list[i]['name'])
            else:
                with open('leak.txt', 'a', encoding='utf8') as file:  # 数据持久化，统计错误信息
                    file.write(('没有访问权限: ' + str(each_uin) + " " + data_friend_list[i]['name'] + "\n"))


if __name__ == '__main__':
    main()
