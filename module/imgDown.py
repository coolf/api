import requests, time, random, string, base64, os, sys, re
from flask import jsonify

sys.path.append('../')
from app import mongo


class ImgDown():
    '''
    图片外链模块

    '''

    def __init__(self, code, imgCode):
        self.code = code
        self.imgCode = imgCode

        if code == 'sogou':
            self.content = self.Sogou()
        if code == 'taobao':
            self.content = self.Taobao()
        if code == 'baidu':
            self.content = self.Baidu()
        if code == 'qihu':
            self.content = self.Qihu360()
        if code == 'weibo':
            self.content = self.Weibo()

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
            return self.RtContent(data=r)
        else:
            return self.RtContent(errcode=400, errmsg='上传失败')

        # 淘宝图床

    def Taobao(self):
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
            return self.RtContent(data='https:' + r['url'])

    def Baidu(self):
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
            return self.RtContent(data=r['url'])
        else:
            return self.RtContent(errmsg='上传失败', errcode=400)

    def Qihu360(self):
        url = 'https://user.btime.com/uploadHead'
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        qrcodePath = str(int(time.time() * 1000)) + salt + '.png'
        imgData = base64.b64decode(self.imgCode)
        with open(qrcodePath, 'wb') as f:
            f.write(imgData)
        files = {'file': ('qrcode', open(qrcodePath, 'rb'), 'image/png')}
        r = requests.post(url, data=None, files=files).json()
        os.remove(qrcodePath)
        if r['code'] == 0:
            return self.RtContent(data=r['data']['img_arr']['img'])
        else:
            return self.RtContent(errcode=400, errmsg=r['message'])

    def Weibo(self):
        cookie = mongo.db.cookie.find_one({'qq': '254127401@qq.com'})['cookie']
        url = 'http://picupload.service.weibo.com/interface/pic_upload.php' + '?mime=image%2Fjpeg&data=base64&url=0&markpos=1&logo=&nick=0&marks=1&app=miniblog';
        url += '&cb=http://weibo.com/aj/static/upimgback.html?_wv=5&callback=STK_ijax_' + str(time.time())
        data = {'b64_data': self.imgCode}
        r = requests.post(url, data=data, cookies=cookie, allow_redirects=True).text.replace('\n', '').strip().replace(
            ' ', '')
        r = self.qwbzj(r, 'pid":', '}}}}')
        r = self.qwbzj(r, '\"', '\"')
        if r != '':
            return self.RtContent(data='https://ws3.sinaimg.cn/large/' + r + '.jpg')
        else:
            return self.RtContent(errcode=400, errmsg='上传失败')

# 'http://ws3.sinaimg.cn/large/6865c12dgy1fxupcwzdosj21da0u0dlm.jpg'
