# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class QiubaiPipeline(object):
    def open_spider(self, spider):
    #     打开文件
        self.fp = open('./糗事百科2.txt',mode='a',encoding='utf-8')

    def process_item(self, item, spider):

        data = {}

        data['nickname'] = item['nickname']
        data['content'] = item['content']
        data['vote'] = item['vote']
        data['comment'] = item['comment']
        # 向文件中保存数据
        self.fp.write(json.dumps(data,ensure_ascii=False)+'\n')

        return data


    def close_spider(self,spider):
#         爬虫结束
        self.fp.close()



# QiubaiPipeline2中的process_item(self, item, spider): item数据来自于QiubaiPipeline
# 为什么？？？ 因为settings
class QiubaiPipeline2(object):
    def open_spider(self, spider):
    #     打开文件
        self.fp = open('./qiushibaike2.txt',mode='a',encoding='utf-8')

    def process_item(self, item, spider):

        # data = {}
        #
        # data['nickname'] = item['nickname']
        # data['content'] = item['content']
        # data['vote'] = item['vote']
        # data['comment'] = item['comment']
        # 向文件中保存数据
        self.fp.write(json.dumps(item,ensure_ascii=False)+'\n')

        return item


    def close_spider(self,spider):
#         爬虫结束
        self.fp.close()
