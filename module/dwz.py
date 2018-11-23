import requests
from flask.json import jsonify
class dwz():

    def __init__(self, url,apiCode):
        self.url = url
        if apiCode == 'baidu':
            self.content = self.baidu()
        if apiCode == 'sina':
            self.content = self.sina()
        if apiCode == 'qq':
            self.content = self.qq()
    def RtContent(self,errcode=0,errmsg='',data=''):
        return jsonify({
            'errcode':errcode,
            'errmsg':errmsg,
            'data':data
        })

    def sina(self):
        appkey = '31641035'
        url = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long='+self.url
        # res = requests.get(url).json()[0]
        res = requests.get(url).json()
        try:
            if res[0].get('error_code') is None:
                return self.RtContent(errcode=0,data=res[0]['url_short'])
        except:
            return self.RtContent(errcode=400,errmsg='网址输入错误')
    def baidu(self):
        url ='http://dwz.cn/create.php'
        # print(self.url)
        data = {"url":self.url}
        res =requests.post(url,data=data).json()
        if res.get('status') == 0:
            return self.RtContent(data=res['tinyurl'])
        else:
            return self.RtContent(errmsg=res['err_msg'],errcode=400)
    def qq(self):
        url = 'http://sa.sogou.com/gettiny?url=' + self.url
        res = requests.get(url).text
        return self.RtContent(data=res)