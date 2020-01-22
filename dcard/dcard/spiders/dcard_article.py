# -*- coding: utf-8 -*-
import time
import scrapy
import json,codecs
from dcard.items import DcardItem

count = 0
class DcardArticleSpider(scrapy.Spider):
    name = 'dcard_article'
    allowed_domains = ['dcard.tw']
    start_urls = ['https://www.dcard.tw/_api/forums/sex/posts?popular=false&limit=100']

    def parse(self, response):
        global count
        # file = codecs.open('data.json','w',encoding='utf-8')
        line = json.loads(response.text,encoding='utf-8')
        count +=  len(line) # 计数

        if count % 500==0:
            print("临时中止，减轻服务器压力")
            time.sleep(60)

        last_id = line[99]["id"]
        print("最后一个id是 {0}".format(last_id))
        # file.write(line)
        item = DcardItem()
        item['line'] = line
        yield item

        new_url = "https://www.dcard.tw/_api/forums/sex/posts?popular=false&limit=100&before=" + str(last_id)
        yield scrapy.Request(new_url,callback=self.parse)


