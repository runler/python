# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = '强子'
import requests
from settings import *
import cons

dict_station = {}
for i in cons.station.split('@'):
    tmp_list = i.split('|')
    #print(tmp_list)
    if len(tmp_list) > 2:
        dict_station[tmp_list[1]] = tmp_list[2]
#print(dict_station)

from_station = dict_station[FROM_STATION]
to_station = dict_station[TO_STATION]
#print(from_station,to_station)

def queryTicket():#query_ticket
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(TRAIN_DATE, from_station, to_station))
    result = response.json()
    return result['data']['result']

n = 0
'''
23 = 软卧
28 = 硬卧
3 = 车次
'''
for i in queryTicket():
    tmp_list = i.split('|')
    # for ii in tmp_list:
    #     print(n)
    #     print(ii)
    #     n += 1
    set = tmp_list[SET]
    if set == '' or set == '无':
        print('无票',tmp_list[SET],tmp_list[3])
    else:
        print('有票',tmp_list[SET],tmp_list[3])
        #下单