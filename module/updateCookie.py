import requests
import sys
sys.path.append('../')
from app import mongo
class updataCookie():
    def __init__(self):
        self.qq = '254127401'
        self.pwd = 'chuxia.2211'
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