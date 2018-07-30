# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Number = scrapy.Field()
    author = scrapy.Field()
    bookname = scrapy.Field()
    chapter_name = scrapy.Field()
    content = scrapy.Field()
    
    
