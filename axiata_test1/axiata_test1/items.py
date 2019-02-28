# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class yangonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Category = scrapy.Field()
    Address = scrapy.Field()
    Township = scrapy.Field()
    State = scrapy.Field()
    Phone = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()






