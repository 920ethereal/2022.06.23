from ast import ImportFrom
from json import dumps
from sqlite3 import Cursor
from unittest import result
from flask import Flask
#引用请求
from flask import request
#解决跨域问题
from flask_cors import CORS
#引用加密库
import hashlib
import pymysql
from datetime import datetime
from datetime import date
import json
#时间转化
class CJsonEncoder(json.JSONEncoder):
      
  def default(self, obj):
      if isinstance(obj, datetime):
          return obj.strftime('%Y-%m-%d %H:%M:%S')
      elif isinstance(obj, date):
          return obj.strftime('%Y-%m-%d')
      else:
          return json.JSONEncoder.default(self, obj)


app=Flask(__name__)
cors=CORS(app)
conn=pymysql.Connect( host="localhost",
                     user='root',
                     port=3306,
                     password='qwerty12',
                     database='shop')
@app.route("/")
def index():
      return "(a:1,b:2)"

@app.route("/user/login",methods=["POST"])
def login():
      #获取用户名和密码
      phone=request.json.get("phone")
      password=request.json.get("password")
      #加密密码
      password=hashlib.sha1(password.encode()).hexdigest()
      #数据库查询数据
      cursor=conn.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT name,uid,avatar,phone,insert_data,last_login_time FROM user_fil WHERE phone='"+phone+"' AND `password`='"+password+"'")
      result=cursor.fetchall()  
      #result就是结果   
      returnmsg={"status":0,'desc':"登录成功",'uid':1}
      #判断当返回结果的长度是0时 此时没有数据 登录失败
      if(len(result)==0):
         returnmsg["status"]=1
         returnmsg["desc"]="用户名和密码不匹配"
         returnmsg["uid"]=0
      else:
         returnmsg["uid"]=result[0]["uid"]
         returnmsg["info"]=result[0]
      return json.dumps(returnmsg,cls=CJsonEncoder)
#获取类别商品
@app.route("/goods/type_lists")
def get_type_lists():
      #数据库查询分类
      cursor=conn.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT type_id,type_name FROM goods_type_fil ORDER BY orderby")
      types=cursor.fetchall()  
      #数据库查询所有商品
      cursor=conn.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT * FROM goods_fil WHERE 'status'=0")
      result=cursor.fetchall()
      for p in types:
            p["data"]=[one for one in result if one["type_id"]==p["type_id"]]
      return json.dumps(types,cls=CJsonEncoder) 
app.run(host="172.17.99.170",port=4444,debug=True)