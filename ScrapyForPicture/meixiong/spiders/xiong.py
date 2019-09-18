# -*- coding: utf-8 -*-
import scrapy
# from scrapy import log
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from meixiong.items import MeixiongItem
from meixiong.items import MXTDetails

import re


class XiongSpider(CrawlSpider):
    name = 'xiong'
    allowed_domains = ['www.5857.com']
    BASE_URL = "http://www.5857.com/meixiong/index_"
    offset = 2
    image_num = 0
    current_num = 0
    start_urls = [BASE_URL + str(offset) + ".html"]
    rules = (
        Rule(LinkExtractor(allow=r"/meixiong/index_(\d+).html"), callback="prase_total"),
        Rule(LinkExtractor(allow=r"/sjbz/\d{5}.html"), callback="prase_detail", follow=False),
    )


    def prase_total(self, response):
        node_list = response.xpath("//li/div/a")
        for node in node_list:
            item = MeixiongItem()
            item['nickname'] = node.xpath("./span/text()").extract()[0]
            item['srclink'] = node.xpath("./@href").extract()[0]

            yield item

    def prase_detail(self, response):
        item = MXTDetails()
        item['src_link'] = response.xpath("//div[@class='main_center_img']/a[2]/img/@src").extract()[0]
        item['max_pic_num'] = response.xpath("//div[@class='main_center']/h1/span/em/text()").extract()[0].strip('/')
        item['cur_pic_num'] = response.xpath("//div[@class='main_center']/h1/span/em/b/text()").extract()[0]
        item['nickname'] = response.xpath("//div[@class='main_center']/h1/text()").extract()[0]
        
        
        yield item

        next_page = response.xpath("//div[@class='main_center_img']/a[3]/@href").extract()[0]
        self.image_num = int(item['max_pic_num'])
        self.current_num = int(item['cur_pic_num'])
        if self.current_num <= self.image_num:
            yield scrapy.Request(next_page, callback=self.prase_detail)