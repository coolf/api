from flask import Flask,request
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://chuxia:ddfeed.2541@117.50.46.232:25412/qquser',
)
mongo = PyMongo(app)
errmsg = '出错，请联系管理员'