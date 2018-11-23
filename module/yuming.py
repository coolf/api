import requests,json
from flask.json import jsonify

class YmTool():
    def __init__(self,url):
        self.url = url
        self.content = self.status()
    def RtContent(self,errcode=0,errmsg='',data=''):
        return jsonify({
            'errcode':errcode,
            'errmsg':errmsg,
            'data':data
        })
    def qwbzj(self,req, x, y):
        a = req.find(x)
        b = req.find(y, int(a + 1))
        return req[a + len(x):b]

    def status(self):
        headers = {
            'Pragma': 'no-cache',
            'Referer': 'https://guanjia.qq.com/online_server/result.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

        }
        r = requests.get(
            'https://cgi.urlsec.qq.com/index.php?m=check&a=check&callback=jQuery172007243194546452014_1542281322694&url=' + self.url + '&_=1542281323623',
            headers=headers).text
        r = self.qwbzj(r, '(', ')')
        r = json.loads(r)
        if r['reCode']  == 0:
            return self.RtContent(data=r['data'])
        else:
            return self.RtContent(errcode=400,errmsg=r['data'])