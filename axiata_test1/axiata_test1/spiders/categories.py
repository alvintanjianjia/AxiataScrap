import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from axiata_test1.items import yangonItem
from scrapy.http import Request



class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['www.yangondirectory.com']
    # start_urls = ['http://www.yangondirectory.com/en/categories-index/accountancy-management-training-centres.html']

    # def init(self, *args, **kwargs):
    #    super(CategoriesSpider, self).init(*args, **kwargs)
    #    self.proxy_pool = ['54.233.85.126','35.227.54.242','34.229.58.223','80.211.189.165','167.99.5.127']

    def parse(self, response):
        # print()
        extension = response.css('div.listing div.row div.col-xs-12 a.first-feature-tag-title::attr(href)').extract()
        print(extension)
        for s in extension:
            site = response.urljoin('http://www.yangondirectory.com' + s)
            print(site)
            yield scrapy.Request(url=site, callback=self.parse2)
            # go to the next page
        next_page = response.css("div.col-md-12 ul.pagination-list li a::attr(href)").extract()[-2]
        if next_page:
            url = response.urljoin('http://www.yangondirectory.com' + next_page)
            # print("--------------------------------------------")
            # print(url)
            yield Request(url=url, callback=self.parse)
            # print("++++++++++++++++++++++++++++++++++++++++++++")

    def parse2(self, response):
        print("--------------parse2")

        for row in response.css('div.categorydetail_subblock'):
            item = yangonItem()
            try:
                item["Name"] = row.css('div.info_block div.row div.col-info h1::text').extract_first()
            except:
                pass
            try:
                item["Category"] = row.css('div.info_block div.row div.col-info p.category::text').extract_first()
            except:
                pass
            try:
                item["Address"] = row.css('div.info_block div.row div.col-info p::text').extract()[1]
            except:
                pass
            try:
                item["Township"] = row.css('div.info_block div.row div.col-info p::text').extract()[3]
            except:
                pass
            try:
                item["State"] = row.css('div.info_block div.row div.col-info p::text').extract()[5]
            except:
                pass
            try:
                item["Phone"] = row.css('div.info_block div.row div.col-info p::text').extract()[7]
            except:
                pass
            try:
                item["Latitude"] = \
                    row.css('div.map_block div.row div.col-xs-12 script::text').re('\(([^)]+)\)')[0].split(',')[0]
            except:
                pass
            try:
                item["Longitude"] = \
                    row.css('div.map_block div.row div.col-xs-12 script::text').re('\(([^)]+)\)')[0].split(',')[1]
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