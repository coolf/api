# -*- coding:utf-8 -*-
import requests
import sys,base64
sys.path.append('../')
from app import mongo
class updataCookie():
    def __init__(self):
        self.qq = '254127401'
        self.pwd = 'chuxia.1122'
        data = {
            'qq': self.qq,
            'pwd': self.pwd
        }
        content = requests.post('https://qqlogin.nuolkj.com/login', data=data).json()
        url =content['loginurl']
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'http://vip.qq.com/'
        }
        self.cookie = requests.get(url, allow_redirects=False).cookies.get_dict()
        self.data  ={
            'qq':self.qq,
            'cookie':self.cookie
        }
        self.content= self.updata()
    def updata(self):
        try:
            if mongo.db.cookie.find_one({'qq':self.qq}):
                mongo.db.cookie.update_one({
                    'qq':self.qq
                }, {"$set": self.data}
                )
            else:
                 mongo.db.cookie.insert(self.data)
            return 'ok'
        except Exception as e:
            print(e)
            return 'no'

        # 更新微博Cookie

class WeiboCookieUpdata():

    def __init__(self):
        self.uin = '254127401@qq.com'
        self.pwd = 'ddfeed.2541'

    def updata(self):
        url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_=1403138799543'
        data = {
            'entry':'sso',
            'gateway':'1',
            'from':'null',
            'savestate':'30',
            'useticket':'0',
            'pagerefer':'',
            'vsnf':'1',
            'su':base64.b64encode(self.uin.encode('utf-8')),
            'service':'sso',
            'sp':self.pwd,
            'sr':'1920*1080',
            'encoding':'UTF-8',
            'cdult':'3',
            'domain':'sina.com.cn',
            'prelt':'0',
            'returntype':'TEXT'
        }
        res = requests.post(url,data=data).cookies
        self.data = {
            'qq':self.uin,
            'cookie':res.get_dict()
        }
        try:
            if mongo.db.cookie.find_one({'qq':self.uin}):
                mongo.db.cookie.update_one({
                    'qq':self.uin
                }, {"$set": self.data}
                )
            else:
                 mongo.db.cookie.insert(self.data)
            return 'ok'
        except Exception as e:
            print(e)
            return 'no'
updataCookie().content