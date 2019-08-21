# coding: utf-8
import pymongo

from configs.config import mongodb

def create_conn():
    conn = pymongo.MongoClient(mongodb['HOST'], mongodb['PORT'])
    return conn[mongodb['NAME']]