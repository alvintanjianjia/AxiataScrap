# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myanmaryp.items import MyanmarypItem
from scrapy.http import Request
import random

class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['www.myanmaryp.com']


    start_urls = ['https://www.myanmaryp.com/category/Architectural_services']
    # start_urls = ['https://www.myanmaryp.com/company/85491/Conceptine_Myanmar_Co_Ltd_Draka_Prysmian']
    def init(self, *args, **kwargs):
        super(CategoriesSpider, self).init(*args, **kwargs)
        self.proxy_pool = ['45.225.138.118:53281']

    def parse(self, response):
        print("--------------parse1")
        category_extension = []
        site = ['https://www.myanmaryp.com/category/Architectural_services']
        # site = 'https://www.myanmaryp.com/company/85491/Conceptine_Myanmar_Co_Ltd_Draka_Prysmian'

        # response.xpath("//div[@id='map_canvas']").xpath("@data-map-ltd").extract()
        print('extracton taking place')


        extension = response.css("div.company.g_0 a::attr(href)").extract()
        print(extension, "Extension is here")
        for element in extension:
            tempE = element.split('/')
            if len(tempE) == 4:
                if tempE[1] == "company":
                    print(element, 'company url is being added')
                    category_extension.append(element)
        category_extension = set(category_extension)


        # extension = response.css('div.listings div.company.g_0 a::attr(href)').extract()

        print('extraction finish')
        for s in category_extension:
            site = ("https://www.myanmaryp.com" + s)
            yield scrapy.Request(url=site, callback=self.parse2, dont_filter=True)
        next_page = response.css("div.pages_container a[rel='next']::attr(href)").extract_first()
        if next_page:
            print('Next page url is: ', next_page)
            site = ("https://www.myanmaryp.com" + next_page)
            yield Request(url=site, callback=self.parse, dont_filter=True)
        ###################################################################################
        # print()
        # extension = response.css('div.listings div.company g_0 a::attr(href)').extract()
        # print(extension,"Extension")
        # for s in extension:
        #     site = response.urljoin('http://www.myanmaryp.com' + s)
        #     print(site, "Site Visited")
        #     yield scrapy.Request(url=site, callback=self.parse2)
        #
        # next_page = response.css("div.listings div.company g_0 a::attr(href)").extract()
        # if next_page:
        #     url = response.urljoin('http://www.myanmaryp.com' + next_page)
        #     print("--------------------------------------------")
        #     print(url)
        #     yield Request(url=url, callback=self.parse)
        #     print("++++++++++++++++++++++++++++++++++++++++++++")
    ############################################################################################

    def parse2(self, response):
        print("--------------parse2")
        item = MyanmarypItem()
        for row in response.css('div.tp'):
            try:
                temp = row.css('ul li:nth-child(3)').extract()
                temp = temp[0].split(">")
                temp = temp[3]
                temp = temp.split("<")
                temp = temp[0]
                print(temp)
                item["Category"] = temp
            except:
                pass
        for row in response.css('div.cmp_details'):
            # item = MyanmarypItem()
            try:
                #span id is unique
                item["Name"] = row.css('span#company_name::text').extract_first()
            except:
                pass
            try:
                item["Address"] = row.css("div.cmp_details_in div.info div.text.location::text").extract_first()
            except:
                pass
            try:
                item["Phone"] = row.css('div.cmp_details_in div.info div.text.phone::text').extract_first()
            except:
                pass
            # try:
            #     item["Latitude"] = row.css('div.cmp_more div.info.info_map div.map_canvas data-map-lng::text').extract_first()
            # except:
            #     pass
            # try:
            #     item["Longitude"] = row.css('div.info.info_map data-map-ltd::text').extract_first()
            # except:
            #     pass
        for row in response.css('div.info.info_map'):
            try:
                # item["Latitude"] = row.css('div.map_canvas').extract_first()
                item["Latitude"] = response.xpath("//div[@id='map_canvas']").xpath("@data-map-ltd").extract()
            except:
                pass
            try:
                # item["Longitude"] = row.css('div.map_canvas').extract_first()
                item["Longitude"] = response.xpath("//div[@id='map_canvas']").xpath("@data-map-lng").extract()
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

    def get_request(self, url):
        req = Request(url=url)
        if self.proxy_pool:
            req.meta['proxy'] = random.choice(self.proxy_pool)
        return req



