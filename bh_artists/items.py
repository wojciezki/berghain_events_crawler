# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class BhArtistsItem(scrapy.Item):
    event_link = scrapy.Field()
    event_name = scrapy.Field()
    event_date = scrapy.Field()
    lineup = scrapy.Field()


