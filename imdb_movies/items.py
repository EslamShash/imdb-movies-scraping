# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    director = scrapy.Field()
    votes = scrapy.Field()
    url = scrapy.Field()


    pass
