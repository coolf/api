from module.dwz import dwz
from module.tao import TaoText
from module.yuming import YmTool
from module.music import MusicScript
from module.qq import QQ
from module.updateCookie import updataCookie
from app import app,errmsg,request




# 短网址API 路由
@app.route('/dwz',methods=['GET'])
def index():
    try:
        url = request.args.get('url')
        code = request.args.get('code')
        return dwz(url,code).content
    except Exception as e:
        return errmsg
# 淘口令API
@app.route('/tao')
def tao():
    try:
        text = request.args.get('text')
        url = request.args.get('url')
        logo = request.args.get('logo')
        return TaoText(text,url,logo).content
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
        return MusicScript(uid,id).content
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

#更新cookie
@app.route('/update')
def update():
    return updataCookie().content

if __name__ == '__main__':
    app.run(debug=True)