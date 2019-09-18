# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from meixiong.settings import IMAGES_STORE
from scrapy import log

class MeixiongPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        # 如果此文件夹已存在 ，则直接放入图片，否则就创建此文件夹
        try:
            if os.path.exists(IMAGES_STORE + item['nickname']):
                imagelink = item['src_link']     # 获取下载链接
                yield scrapy.Request(imagelink)  # 提交给下载器
            else:
                os.makedirs(IMAGES_STORE + item['nickname'])
        except Exception as error:
            log(error)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        try:
            os.rename(IMAGES_STORE + image_path[0], IMAGES_STORE + item['nickname'] + '\\' + item['cur_pic_num'] + '.jpg')
        except FileNotFoundError as fer:
            log(fer)
