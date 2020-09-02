from requests import get
from urllib import parse

pictureName = input('输入要下载的图片类型:')
pictureNumber = int(input('输入需要下载的图片页数/每页三十:'))
if __name__ =='__main__':
    word = parse.quote(pictureName)
    for m in range(0,pictureNumber):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&' \
              'ipn=rj&ct=201326592&is=&fp=result&queryWord='+word+'&cl=2&lm' \
              '=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word='+word+'&' \
              's=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn' \
               '='+str(m*30)+'&rn=30'
        html_response = get(url)
        for n in range(30):
            pictureUrl = html_response.json()['data'][n]['middleURL']
            print(pictureUrl[-20:])
            picture = get(pictureUrl).content
            with open('百度图片/'+pictureUrl[-20:],'wb') as f:
                f.write(picture)
