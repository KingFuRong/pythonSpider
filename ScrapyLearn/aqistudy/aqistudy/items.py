# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AqistudyItem(scrapy.Item):
    # define the fields for your item here like:
    city_name = scrapy.Field()
    city_url = scrapy.Field()
    city_month = scrapy.Field()
    request_status = scrapy.Field()
    date = scrapy.Field()
    AQI = scrapy.Field()
    quality = scrapy.Field()
    PM2_5 = scrapy.Field()
    PM10 = scrapy.Field()
    SO2 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3_8h = scrapy.Field()
    pass
