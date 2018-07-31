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
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.Biqugemenu
    collection = db.GetBiqugemenuItems
    for i in range(1,20):
        for j in range(i*1000,i*1000+1000):
            url = 'http://www.biquge.com.tw'+'/'+str(i)+'_'+str(j)+'/'
            #将匹配到的url存入start_urls中，供scrapy调用下载
            if collection.find_one({'book_url':url}) != None:
                start_urls.append(url)
            else:
                print('此网站不存在！！%s'%url)

    def parse(self, response):
        #通过bookurl提取所有章节urls
        chapters = response.css('#list a::attr(href)').extract()
        number = 0
        Max_chapters = len(chapters)
        for chapter in chapters:
            #获取章节地址
            url = 'http://www.biquge.com.tw'+ chapter
            #从章节url中获得小说名称与作者名字
            bookname = response.css('h1::text').extract_first()
            author = response.css('p::text').extract_first().strip('作\xa0\xa0\xa0\xa0者：')
    
            #当Number计数到最大章节时，向表MongoDB.Biqugemenu.GetBiqugemenuItems中添加{'Download':'Complete！'}
            while number <= Max_chapters:
                #章节计数单位number加1，保证存入mongodb后，能够通过'number'来确定章节顺序
                number = number + 1
                #通过章节数判断是否章节已存在，若存在，则跳过，不返回item
                client = pymongo.MongoClient(host='localhost',port=27017)
                db = client.BiqugeNovels
                collection = db[str(author)+'_'+str(bookname)]
                if collection.find_one({'Number':number}) == None:
                    #调用parse_page函数，并且通过meta方法传入bookname，number，author
                    yield scrapy.Request(url=url,callback=self.parse_page,meta={'number':number,'bookname':bookname,'author':author,'Max_chapters':Max_chapters})
                else:
                    chapter_info = str(author)+'_'+str(bookname)+'_'+str(number)
                    print('%s 章节已存在!'%chapter_info)
            else:
                client = pymongo.MongoClient(host='localhost',port=27017)
                db = client.Biqugemenu
                collection = db.GetBiqugemenuItems
                condition = {'book_url':response.url}
                book = collection.find_one(condition)
                book['Download'] = 'Complete!'
                collection.update(condition,book)

    def parse_page(self,response):
        #通过章节url获取文章内容

        #初始化item
        item = BookinfoItem()
        #获得正文及章节名称
        content=response.css('#content').extract()[0].replace('<br>','')
        item['content']=content.replace('<div id="content">','   ')
        item['chapter_name']=response.css('.bookname h1::text').extract()[0]
        #将meta方法传入的参数给到item
        item['bookname']=response.meta['bookname']
        item['author']=response.meta['author']
        item['Number']=response.meta['number']
        item['Max_chapters']=response.meta['Max_chapters']
        #返回item供pipelines调用
        yield item
        