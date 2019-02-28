# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from getMandalayCategories.items import GetmandalaycategoriesItem
from scrapy.http import Request

class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['mandalaydirectory.com']
    start_urls = ['http://www.mandalaydirectory.com/en/categories-index/list-alpha/a.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/b.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/c.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/d.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/e.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/f.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/g.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/h.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/i.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/j.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/k.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/l.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/m.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/n.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/o.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/p.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/q.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/r.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/s.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/t.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/u.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/v.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/w.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/x.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/y.html',
                  'http://www.mandalaydirectory.com/en/categories-index/list-alpha/z.html'
                  ]


    def parse(self, response):
        print("--------------parse2")

        for row in response.css('div.category.col-md-4.col-sm-6.col-xs-12'):

            item = GetmandalaycategoriesItem()
            try:
                item["Name"] = row.css('a::attr(href)').extract_first()
            except:
                pass

            yield item

        # untuk amik site , semua site
        #  http://www.yangondirectory.com/en/categories-index/chinese-temples.html
        # response.css('div.listing div.row div.col-xs-12 a.first-feature-tag-title::attr(href)').extract()

        # untuk amik company info
        # response.css('div.categorydetail_subblock div.info_block div.row div.col-info').extract_first()

        # untuk amik google key
        # response.css('div.categorydetail_subblock div.map_block div.row div.col-xs-12 div.map script')[0].extract()

        # untuk amik script yg contains lat long
        # response.css('div.categorydetail_subblock div.map_block div.row div.col-xs-12 div.map script')[1].extract()

        # response.css('div.categorydetail_subblock div.map_block div.row div.col-xs-12 div.map script')[1].re(r'locations')

    # def get_request(self, url):
    #    req = Request(url=url)
    #    if self.proxy_pool:
    #        req.meta['proxy'] = random.choice(self.proxy_pool)
    #    return req
