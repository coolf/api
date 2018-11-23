from module.dwz import dwz
from module.tao import TaoText
from module.yuming import YmTool
from flask import Flask,request

app = Flask(__name__)



# 短网址API 路由
@app.route('/dwz',methods=['GET'])
def index():
    url = request.args.get('url')
    code = request.args.get('code')
    return dwz(url,code).content

# 淘口令API
@app.route('/tao')
def tao():
    text = request.args.get('text')
    url = request.args.get('url')
    logo = request.args.get('logo')
    return TaoText(text,url,logo).content

@app.route('/ym')
def ym():
    url = request.args.get('url')
    return YmTool(url).content

if __name__ == '__main__':
    app.run(debug=True)