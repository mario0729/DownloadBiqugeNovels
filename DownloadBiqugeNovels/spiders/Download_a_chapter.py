# -*- coding: utf-8 -*-
import scrapy
import pymongo
import requests
from DownloadBiqugeNovels.items import BookinfoItem
from scrapy import Selector

class DownloadAChapterSpider(scrapy.Spider):
    name = 'Download_a_chapter'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = []
    #从MongoDB.Biqugemenu.GetBiqugemenuItems中匹配url
    client = pymongo .MongoClient(host='localhost',port=27017)
    db = client.Biqugemenu
    collection = db.GetBiqugemenuItems
    for i in range(1,20):
        for j in range(i*1000,i*1000+1000):
            url = 'http://www.biquge.com.tw'+'/'+str(i)+'_'+str(j)+'/'
            #print(url)
            #result = collection.find_one({'book_url':str(url)})
            #print(result)
            start_urls.append(url)



    def parse(self, response):
        chapters = response.css('#list a::attr(href)').extract()
        #print(type(chapters))
        number = 0
        for chapter in chapters:
            url = 'http://www.biquge.com.tw'+ chapter
            bookname = response.css('h1::text').extract_first()
            author = response.css('p::text').extract_first().strip('作\xa0\xa0\xa0\xa0者：')
            #print(url)
            number = number + 1
            yield scrapy.Request(url=url,callback=self.parse_page,meta={'number':number,'bookname':bookname,'author':author})

    def parse_page(self,response):
        item = BookinfoItem()
        content=response.css('#content').extract()[0].replace('<br>','')
        #print(type(content))
        #print(content)
        #a=''.join(list(content))
        item['content']=content.replace('<div id="content">','   ')
        item['chapter_name']=response.css('.bookname h1::text').extract()[0]
        item['bookname']=response.meta['bookname']
        item['author']=response.meta['author']
        item['Number']=response.meta['number']
        #print(item)
        yield item