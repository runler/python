import json
import re
import requests


def get_songid():
    url = 'http://music.taihe.com/search?key=%E9%99%88%E7%B2%92'
    response = requests.get(url=url)
    html = response.text
    sids = re.findall(r'sid&quot;:(\d+),', html)
    return sids


def get_music_url(songid):
    api_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery17206453751179783578_1544942124991&songid={songid}&from=web'
    response = requests.get(api_url.format(songid=songid))
    print(response.status_code)

    str_json = re.findall(r'{.*}', response.text)[0]
    data = json.loads(str_json)
    music_name = data['songinfo']['title']
    music_url = data['bitrate']['file_link']
    yield music_name, music_url
    print(music_url, music_name, "下载完成")


def save_file(filename, content):
    with open(file=filename, mode="wb") as f:
        f.write(content)


def run():
    for songid in ["1390840"]:
        for music_name, music_url in get_music_url(songid=songid):
            save_file(filename=music_name + "mp3", content=requests.get(music_url).content)
            print(music_name + " 下载完成")


if __name__ == "__main__":
    run()
