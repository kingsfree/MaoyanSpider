# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['time'],item['star'])
        return item

import pymysql
from .settings import *
# 数据存入mysql管道类
class MaoyanMysqlPipeline(object):
    # 监听爬虫,爬虫启动时只执行1次,一般用于数据库连接
    def open_spider(self,spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
        print('我是open_spider')

    def process_item(self,item,spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        L = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    # 监听爬虫,爬虫结束时只执行1次,一般用于数据库断开
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print('我是close_spider')

import pymongo
# 数据存入mongodb管道类
class MaoyanMongoPipeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        d = dict(item)
        self.myset.insert_one(d)

        return item




