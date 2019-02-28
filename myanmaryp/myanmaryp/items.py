import scrapy


class MyanmarypItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    Category = scrapy.Field()
    Name = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()

