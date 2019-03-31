# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import json
import codecs
from items import ImagedemoItem
from items import MenuImageItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImagedemoPipeline(object):
    #初始化时指定要操作的文件

    def __init__(self):
        self.file = codecs.open('restaurant_name.json', 'w', encoding='utf-8')

    # 存储数据，将 Item 实例作为 json 数据写入到文件中
    def process_item(self, item, spider):
        if isinstance(item, ImagedemoItem):
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(lines)
            return item

    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.file.close()

class MenuImagePipeline(object):
    #初始化时指定要操作的文件

    def __init__(self):
        self.file = codecs.open('menu.json', 'w', encoding='utf-8')

    # 存储数据，将 Item 实例作为 json 数据写入到文件中
    def process_item(self, item, spider):
        if isinstance(item, MenuImageItem):
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(lines)
            return item

    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.file.close()

class SubDoubanImgDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item, 'index': item['image_urls'].index(image_url)})

    def file_path(self, request, response=None, info=None):
        print '---------------'

        item = request.meta['item']  # 通过上面的meta传递过来item
        index = request.meta['index']  # 通过上面的index传递过来列表中当前下载图片的下标

        # 图片文件名，item['carname'][index]得到汽车名称，request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png
        image_guid = request.url.split('/')[-2] + '.jpg'
        # image_guid = request.url.split('/')[-1].split('.')[-1]
        print image_guid
        print '<<<<<<<<<<<<<'

            # os.path.splitext()[0]
        # 图片下载目录 此处item['country']即需要前面item['country']=''.join()......,否则目录名会变成\u97e9\u56fd\u6c7d\u8f66\u6807\u5fd7\xxx.jpg
        down_file_name = u'source/{0}/images/{1}'.format(item['image_name'],image_guid)

        return down_file_name

