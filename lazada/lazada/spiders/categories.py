# -*- coding: utf-8 -*-
import scrapy


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['lazada.com.my']
    start_urls = ['http://lazada.com.my/']

    def parse(self, response):
        for row in response.css('div.categorydetail_subblock'):
            print('testing')

