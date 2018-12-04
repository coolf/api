import time
import urllib
import hashlib
import urllib.parse
import urllib.request
import requests
from flask.json import jsonify

# 淘口令生成


app_key = '25289227'
appSecret = 'efe3396c8689392dfe46511cd7e25ac3'


# 淘口令
class TaoText():
    def __init__(self, text, url, logo='https://blog.teqiyi.com/log.png'):
        self.text = text
        self.url = url
        self.logo = logo
        self.content = self.content()

    def RtContent(self, errcode=0, errmsg='', data=''):
        return jsonify({
            'errcode': errcode,
            'errmsg': errmsg,
            'data': data
        })

    def ksort(self, d):
        return [(k, d[k]) for k in sorted(d.keys())]

    def md5(self, s, raw_output=False):
        """Calculates the md5 hash of a given string"""
        res = hashlib.md5(s.encode())
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def createSign(self, paramArr):
        sign = appSecret
        paramArr = self.ksort(paramArr)
        paramArr = dict(paramArr)
        for k, v in paramArr.items():
            if k != '' and v != '':
                sign += k + v
        sign += appSecret
        sign = self.md5(sign).upper()
        return sign

    def createStrParam(self, paramArr):
        strParam = ''
        for k, v in paramArr.items():
            if k != '' and v != '':
                strParam += k + '=' + urllib.parse.quote_plus(v) + '&'
        return strParam

    def content(self):

        # 淘口令
        paramArr = {'app_key': app_key, 'v': '2.0', 'sign_method': 'md5', 'format': 'json',
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'method': 'taobao.tbk.tpwd.create',
                    'text': self.text,
                    'url': self.url,
                    'logo': self.logo
                    }
        sign = self.createSign(paramArr)
        strParam = self.createStrParam(paramArr)
        strParam += 'sign=' + sign
        url = 'https://eco.taobao.com/router/rest?' + strParam
        res = requests.get(url).json()
        if not 'error_response' in res:
            data = res['tbk_tpwd_create_response']['data']['model']
            return self.RtContent(data=data)
        else:
            errmsg = res['error_response']['sub_msg']
            return self.RtContent(errcode=400, errmsg=errmsg)


