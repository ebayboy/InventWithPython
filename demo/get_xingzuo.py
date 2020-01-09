#!/usr/bin/python3

# /****************************************************************************
# @f:get_xingzuo.py
# @author:ebayboy@163.com
# @date:2019-12-26 18:16
# @version 1.0
# @description: python f
# @Copyright (c)  all right reserved
# **************************************************************************/

import os
from flask_restful import fields, marshal
from requests import get, put, post
import json

'''
# response:
{
    "code": 0,
    "data": {
        "date": 20191226,
        "name": "水瓶座",
        "datetime": "2019年12月26日",
        "all": "60",
        "color": "金色",
        "health": "80",
        "love": "90",
        "money": "60",
        "number": 2,
        "QFriend": "天秤座",
        "summary": "今天在学业中会遇到一些难题，你可能不能很快理解一些概念。此外有些同学对你不是非常友好，总喜欢自顾自发表一些观点，让你觉得不耐烦。不过财务上很顺利，有进账的机会。",
        "work": "60",
        "resultcode": "200",
        "error_code": 0
    },
    "message": ""
}
'''

xzs = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座',
       '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']

resource_fields = {
    "date": fields.Integer,
    "name": fields.String,
    "datetime": fields.String,
    "all": fields.String,
    "color": fields.String,
    "health": fields.String,
    "love": fields.String,
    "money": fields.String,
    "number": fields.Integer,
    "QFriend": fields.String,
    "summary": fields.String,
    "work": fields.String
}

for x in xzs:
    url = 'https://uneedzf.com/wepyBook/api/getConstellation?constellation='
    url += format(x)
    resp = get(url).json()
    dic_filter = marshal(resp['data'], resource_fields)
    r = post('http://localhost:5000/Constellation', dic_filter)
    print("%s: status:%d" %(format(dic_filter['name']), r.status_code))
