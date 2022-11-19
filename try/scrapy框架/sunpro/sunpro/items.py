# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    name = scrapy.Field()

class DetailItem(scrapy.Item):
    new_name = scrapy.Field()
    introduce = scrapy.Field()