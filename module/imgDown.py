import requests, time, random, string, base64, os, sys, json
from flask import jsonify

sys.path.append('../')
from app import mongo


class ImgDown():
    '''
    图片外链模块

    '''

    def __init__(self, code, imgCode, uid):
        self.code = code
        self.imgCode = imgCode.replace('data:image/png;base64,', '').replace('data:image/jpeg;base64,', '')
        self.uid = uid

        if code == 'sogou':
            self.content = self.Sogou()
        if code == 'taobao':
            self.content = self.Taobao()
        if code == 'baidu':
            self.content = self.Baidu()
        if code == 'weibo':
            self.content = self.Weibo()
        if code == 'qq':
            self.content = self.Qq()
        self.urlinfo = self.userUrlInfo()

    def qwbzj(self, req, x, y):
        a = req.find(x)
        b = req.find(y, int(a + 1))
        return req[a + len(x):b]

    def RtContent(self, errcode=0, errmsg='', data=''):
        return jsonify({
            'errcode': errcode,
            'errmsg': errmsg,
            'data': data
        })

    # 搜狗

    def Sogou(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        url = 'http://pic.sogou.com/pic/upload_pic.jsp'
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        qrcodePath = str(int(time.time() * 1000)) + salt + '.png'
        imgData = base64.b64decode(self.imgCode)
        with open(qrcodePath, 'wb') as f:
            f.write(imgData)
        files = {'file': ('qrcode', open(qrcodePath, 'rb'), 'image/png')}
        r = requests.post(url, data=None, files=files).text.replace('http://', 'https://')
        os.remove(qrcodePath)
        if r != 'null':
            self.userUpdateImg(r)
            return self.RtContent(data=r)
        else:
            return self.RtContent(errcode=400, errmsg='上传失败')

        # 淘宝图床

    def Taobao(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        url = 'https://s.taobao.com/image'
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        qrcodePath = str(int(time.time() * 1000)) + salt + '.png'
        imgData = base64.b64decode(self.imgCode)
        with open(qrcodePath, 'wb') as f:
            f.write(imgData)
        files = {'imgfile': ('qrcode', open(qrcodePath, 'rb'), 'image/png')}
        r = requests.post(url, data=None, files=files).json()
        os.remove(qrcodePath)
        if not r['status'] == 1:
            return self.RtContent(errcode=400, errmsg=r['errorMsg'])
        elif r['status'] == 1:
            data = 'https:' + r['url']
            self.userUpdateImg(data)

            return self.RtContent(data=data)

    def Baidu(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        url = 'http://image.baidu.com/pcdutu/a_upload?'
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        qrcodePath = str(int(time.time() * 1000)) + salt + '.png'
        imgData = base64.b64decode(self.imgCode)
        with open(qrcodePath, 'wb') as f:
            f.write(imgData)
        files = {'file': ('qrcode', open(qrcodePath, 'rb'), 'image/png')}
        r = requests.post(url, data=None, files=files).json()
        os.remove(qrcodePath)
        if r['errno'] == 0:
            data = r['url']
            self.userUpdateImg(data)
            return self.RtContent(data=data)
        else:
            return self.RtContent(errmsg='上传失败', errcode=400)

    def Weibo(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        cookie = mongo.db.cookie.find_one({'qq': '254127401@qq.com'})['cookie']
        url = 'http://picupload.service.weibo.com/interface/pic_upload.php' + '?mime=image%2Fjpeg&data=base64&url=0&markpos=1&logo=&nick=0&marks=1&app=miniblog';
        url += '&cb=http://weibo.com/aj/static/upimgback.html?_wv=5&callback=STK_ijax_' + str(time.time())
        data = {'b64_data': self.imgCode}
        r = requests.post(url, data=data, cookies=cookie, allow_redirects=True).text.replace('\n', '').strip().replace(
            ' ', '')
        r = self.qwbzj(r, 'pid":', '}}}}')
        r = self.qwbzj(r, '\"', '\"')
        if r != '':
            data = 'https://ws3.sinaimg.cn/large/' + r + '.jpg'
            self.userUpdateImg(data)
            return self.RtContent(data=data)
        else:
            return self.RtContent(errcode=400, errmsg='上传失败')

    def Qq(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        url = 'http://bar.video.qq.com/cgi-bin/fans_admin_upload_pic'
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        qrcodePath = str(int(time.time() * 1000)) + salt + '.png'
        imgData = base64.b64decode(self.imgCode)
        with open(qrcodePath, 'wb') as f:
            f.write(imgData)
        files = {'picture': ('qrcode', open(qrcodePath, 'rb'), 'image/pngs')}
        r = requests.post(url, data=None, files=files).text.replace(' ', '').replace('\n', '')
        r = self.qwbzj(r, 'fansAdminImgCallback(', ');</script>')
        r = json.loads(r)
        os.remove(qrcodePath)
        if r['errCode'] == 0:
            data = r['data']['strUrl']
            self.userUpdateImg(data)
            return self.RtContent(data=data)
        else:
            return self.RtContent(errcode=400, errmsg='上传失败')

    def getUserInfo(self):
        if mongo.db.user.find_one({'uid': self.uid}):
            return True
        else:
            return self.RtContent(errcode=400, errmsg='用户不存在')

    def userUpdateImg(self, url):
        if mongo.db.user.update_one({'uid': self.uid}, {'$push': {'imgUrl': url}}):
            return True
        else:
            return False

    def userUrlInfo(self):
        if self.getUserInfo() != True:
            return self.getUserInfo()
        content = mongo.db.user.find_one({'uid': self.uid}, {'imgUrl': 1, 'uid': 1, '_id': 0})
        return self.RtContent(data=content)
# 'http://ws3.sinaimg.cn/large/6865c12dgy1fxupcwzdosj21da0u0dlm.jpg'
