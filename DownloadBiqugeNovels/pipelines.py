# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings
import pymongo

class MongoPipeline(object):

    def process_item(self, item, spider):
        client = pymongo .MongoClient(host='localhost',port=27017)
        db = client.BiqugeNovels
        #根据书名来创建表名，用collection=db[变量]来创建
        collection = db[item['author']+'_'+item['bookname']]  
        bookinfo = dict(item)
        #将item写入表中
        collection.insert(bookinfo)
        return item