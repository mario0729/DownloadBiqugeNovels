# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #用于记录章节序号
    Number = scrapy.Field()
    #记录作者
    author = scrapy.Field()
    #记录书名
    bookname = scrapy.Field()
    #章节名
    chapter_name = scrapy.Field()
    #章节内容
    content = scrapy.Field()
    
    
