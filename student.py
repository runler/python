import requests
from bs4 import BeautifulSoup
import re
import json
res = requests.get(
 'https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111204369690274915774_1554164761226&cre=tianyi&mod=pctech&merge=3&statics=1&length=15')
res.encoding = 'utf-8'
data=re.search('{\"data\".*', res.text)
jsondata=json.loads(data.group().rstrip(');'))
for news in jsondata['data']:
 print('标题：'+news['title']+'---作者：'+news['author'])