from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://chuxia:ddfeed.2541@117.50.46.232:25412/qquser',
)
CORS(app)
mongo = PyMongo(app)
errmsg = '出错，请联系管理员'