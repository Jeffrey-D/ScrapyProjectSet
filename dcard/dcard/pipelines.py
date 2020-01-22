# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class DcardPipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json', 'w+', encoding="utf-8")

    def process_item(self, item, spider):
        line =  json.dumps(item['line'],ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_close(self, spider):
        self.file.close()