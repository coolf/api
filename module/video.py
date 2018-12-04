import requests,json
from flask import jsonify
class VideoScript():
    '''
    视频解析

    '''

    def __init__(self,code,url):
        self.codeo = code
        self.url = url
        self.headers = {
            'referer':'http://y.qq.com',
            'Upgrade-Insecure-Requests': '1',
            # 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 AliApp(TT/8.1.0) TTPodClient/8.1.0',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Content-Type':'application/x-www-form-urlencoded'
        }
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
    def kuaishou(self):
        res = requests.get(self.url,headers=self.headers).text.replace(' ','')
        res = self.qwbzj(res,'type="video/mp4"src="','.mp4')
        return self.RtContent(data=res+'.mp4')
    def douyin(self):
        res =  requests.get(self.url,headers=self.headers).text
        Uid = self.qwbzj(res,'video_id=','&')
        if not len(Uid) == 32:
            return self.RtContent(errcode=400,errmsg='解析失败')
        url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id='+Uid+'&line=0&ratio=720p&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0'
        res = requests.get(url,allow_redirects=False,headers=self.headers).headers['Location']
        print(res)
        return self.RtContent(data=res)



