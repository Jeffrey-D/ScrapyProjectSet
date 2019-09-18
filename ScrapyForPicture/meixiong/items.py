# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MeixiongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()
    # imagelink = scrapy.Field()
    srclink = scrapy.Field()


class MXTDetails(scrapy.Item):
    src_link = scrapy.Field()
    max_pic_num = scrapy.Field()
    cur_pic_num = scrapy.Field()
    nickname = scrapy.Field()