import requests,json,re,time
from flask import jsonify

class MusicScript():

    def __init__(self,Uid,id):
        self.id = id
        self.Uid = Uid
        if Uid == 'qq':
            self.content = self.QqMusic()
        elif Uid == 'wy':
            self.content = self.WyMusic()
    def qwbzj(self,req, x, y):
        a = req.find(x)
        b = req.find(y, int(a + 1))
        return req[a + len(x):b]
    def RtContent(self,errcode=0,errmsg='',data=''):
        return jsonify({
            'errcode':errcode,
            'errmsg':errmsg,
            'data':data
        })
    def QqMusic(self):
        gid = int(time.time()*1000)
        url ='https://c.y.qq.com/base/fcgi-bin/fcg_musicexpress.fcg?json=3&guid=%d' % gid
        headers = {
            'referer':'http://y.qq.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 AliApp(TT/8.1.0) TTPodClient/8.1.0',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        r = requests.get(url,headers=headers).text
        res = json.loads(self.qwbzj(r, '(', ')'))
        key = res['key']
        mp3link = ('http://dl.stream.qqmusic.qq.com/M800'+self.id+'.mp3?vkey='+key+'&guid='+str(gid)+'&fromtag=30')
        return self.RtContent(data=mp3link)
    def WyMusic(self):
        url = 'http://music.163.com/song/media/outer/url?id='+self.id+'.mp3'
        return self.RtContent(data=url)


