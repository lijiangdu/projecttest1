# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = scrapy.Field()
    film_detail = scrapy.Field()
