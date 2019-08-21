# coding: utf-8
from databases.mongodb import create_conn as mongo_create
mongo_conn = mongo_create()

def hello():
    list = mongo_conn['sites']
    for l in list.find():
        print l