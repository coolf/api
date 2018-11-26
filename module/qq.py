import requests, json
from flask import jsonify
import sys
sys.path.append('../')
from app import mongo
class QQ():
    def __init__(self, code, qq):
        self.qq = qq
        self.cookie = mongo.db.cookie.find_one({'qq':'254127401'})['cookie']
        self.headers = {
            'referer': 'http://ti.qq.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 AliApp(TT/8.1.0) TTPodClient/8.1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if code == 'level':
            self.content = self.level()
        elif code == 'daren':
            self.content = self.daren()
        elif code == 'info':
            self.content = self.QqInfo()

    def qwbzj(self, req, x, y):
        a = req.find(x)
        b = req.find(y, int(a + 1))
        return req[a + len(x):b]

    def getGTK(self, p_skey):
        hashes = 5381
        for letter in p_skey:
            hashes += (hashes << 5) + ord(letter)
        return hashes & 0x7fffffff

    def getGtk1(self, skey):
        e = 5381
        for i in range(len(skey)):
            e = e + (e << 5) + ord(skey[i])
        bkn = str(2147483647 & e)
        return bkn

    def RtContent(self, errcode=0, errmsg='', data=''):
        return jsonify({
            'errcode': errcode,
            'errmsg': errmsg,
            'data': data
        })

    # 取QQ等级
    def level(self):
        url = 'https://h5.vip.qq.com/p/mc/cardv2/other?_wv=1031&platform=1&qq=' + self.qq + '&adtag=geren&aid=mvip.pingtai.mobileqq.androidziliaoka.fromqita'
        res = requests.get(url, cookies=self.cookie).text
        content = self.qwbzj(res, '<p><small>LV</small>', '</p>')
        return self.RtContent(data=content)

    def QqInfo(self):
        url = 'http://ti.qq.com/cgi-bin/more_profile_card/more_profile_card'
        data = '_q=' + self.qq + '&bkn=' + str(self.getGTK(self.cookie['skey'])) + '&src=mobile'
        r = requests.post(url, data=data, headers=self.headers, cookies=self.cookie).json()
        if r['ec'] == 0:
            r = r['profile'][0]
            data = {
                'nick': r.get('nick'),
                'age': r.get('age'),
                'birthday': {'day': r['birthday']['day'], 'month': r['birthday']['month'],
                             'year': r['birthday']['year']},
                'gender': r.get('gender'),
                'personal': r.get('personal'),
                'constellation': r.get('constellation'),
                "hometown_area": r.get('hometown_area'),
                "hometown_city": r.get('hometown_city'),
                "hometown_country": r.get('hometown_country'),
                "hometown_state": r.get('hometown_state'),
                "location_area": r.get('location_area'),
                "location_city": r.get('location_city'),
                "location_country": r.get('location_country'),
                "location_state": r.get('location_state'),

            }
            return self.RtContent(data=data)
        else:
            return self.RtContent(errcode=400, errmsg='接口出错。请联系管理员')

    def daren(self):
        url = 'http://ti.qq.com/cgi-bin/daren/get_daren_info'
        data = 'bkn=' + str(self.getGTK(self.cookie['skey'])) + '&src=mobile&gu=' + self.qq
        r = requests.post(url, data=data, headers=self.headers, cookies=self.cookie).json()
        if r['ec'] == 0:
            data = {
                'nick': r['guest_nick'],
                'login_days': r['guest_info']['login_days']
            }
            return self.RtContent(data=data)
        else:
            return self.RtContent(errcode=400, errmsg='接口出错。请联系管理员')
