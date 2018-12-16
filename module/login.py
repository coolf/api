import requests, json
import sys, time

sys.path.append('../')
from app import mongo, jsonify


class loginHome():
    def __init__(self, request):
        self.code = request.args.get('code')
        self.ip = request.remote_addr
        self.content = self.home()

    def RtContent(self, errcode=0, errmsg='', data=''):
        return jsonify({
            'errcode': errcode,
            'errmsg': errmsg,
            'data': data
        })

    def home(self):

        def qwbzj(req, x, y):
            a = req.find(x)
            b = req.find(y, int(a + 1))
            return req[a + len(x):b]

        try:
            token = requests.get(
                'https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id=101354643&client_secret=222112e0edfe4c768ff816faf0d4e6ad&code=' +
                self.code + '&redirect_uri=https%3a%2f%2fhulian.teqiyi.com%2findex.php').text
            access_token = qwbzj(token, 'access_token=', '&')
            Openid = qwbzj(requests.get('https://graph.qq.com/oauth2.0/me?access_token=' + access_token).text,
                           'callback( ', ' );')
            Openid = json.loads(Openid)
            # 用户唯一id
            uid = Openid['openid']
            if self.getUserInfo(uid):
                user = requests.get(
                    'https://graph.qq.com/user/get_user_info?access_token=' + access_token + '&oauth_consumer_key=101354643&openid=' +
                    Openid['openid']).json()
                data = {
                    'uid': uid,
                    'name': user['nickname'],
                    'logoUrl': user['figureurl_qq_2']

                }
                return self.RtContent(data=data)
            else:
                return self.RtContent(errcode=400, errmsg='登陆失败')
        except Exception as e:
            return self.RtContent(errcode=400, errmsg=str(e))

    def getUserInfo(self, uid):
        if mongo.db.user.find_one({'uid': uid}):
            if mongo.db.user.update_one({'uid': uid}, {'$set': {'date': int(time.time()), 'ip': self.ip}}):
                return True
        else:
            data = {
                'uid': uid,
                'date': int(time.time()),
                'ip': self.ip,
                'imgUrl': []
            }
            if mongo.db.user.insert(data):
                return True
