# -*- coding: utf-8 -*-
import scrapy
from ..items import FirstscrapyItem


class LthSpider(scrapy.Spider):
    name = "lth"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_123175.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_260_50032.html/d/#p=1',
                  'http://news.sina.com.cn/china/xlxw/2017-04-22/doc-ifyepsch2529468.shtml']

    urls2 = ["http://www.jd.com",
             "http://sina.com.cn",
             "http://yum.iqianyue.com"]


    def __init__(self, myurl=None, *args, **kwargs):
        super(LthSpider, self).__init__(*args, **kwargs)
        myurllist = myurl.split("|")
        for i in myurllist:
            print("要爬取的网址是： %s" %i)
        self.start_urls = myurllist

    '''
    def start_requests(self):
        for url in self.urls2:
            yield self.make_requests_from_url(url)
            '''


    def parse(self, response):
        item = FirstscrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下显示的为爬取网址的标题：")
        print(item["urlname"])
