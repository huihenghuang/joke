# -*- coding: utf-8 -*-
import scrapy

from ..items import QiubaiItem

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    # 允许访问哪些网站
    allowed_domains = ['www.qiushibaike.com']

    # 列表爬虫的url
    start_urls = ['https://www.qiushibaike.com/8hr/page/%d/'%(i) for i in range(1,4)]

    # spiders 将url 交给引擎---> 调度器--->(入列，Queue) ----> 队列中取出数据交给了引擎----->
    # 下载器----->联网请求下载数据-----> 引擎-----> 返回给spiders
    # 数据在哪里？？？

    # spider中默认会被回调方法，parse（解析），解析的数据来自网络下载的数据

    # 返回的response数据可以直接使用xpath进行解析
    def parse(self, response):
        divs = response.xpath('//div[contains(@id,"qiushi_tag_")]')

        items = []
        for div in divs:
            nickname = div.xpath('.//h2/text()')[0].extract()
            content = div.xpath('.//div[@class="content"]/span/text()')[0].extract()
            vote = div.xpath('.//span[@class="stats-vote"]/i/text()').extract_first()
            comments = div.xpath('.//span[@class="stats-comments"]/a/i/text()')[0].extract()
            # print('------------------------------------------------------',nickname,content,vote,comments)
            # 将数据保存到字典中
            # item = {}
            # item['nickname'] = nickname
            # item['content'] = content
            # item['vote'] = vote
            # item['comments'] = comments

            item = QiubaiItem()
            item['nickname'] = nickname
            item['content'] = content
            item['vote'] = vote
            item['comment'] = comments

            yield item

            # items.append(item)

        #     spiders 将解析好的数据交个引擎
        # return 数据必须是一个可迭代队列
        # return items