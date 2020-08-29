# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    article_id = scrapy.Field()
    author = scrapy.Field()
    timestamp = scrapy.Field()
    number_of_comments = scrapy.Field()
    comments = scrapy.Field()

class Comment(scrapy.Item):
    article_id = scrapy.Field()
    comment_number = scrapy.Field()
    comment_content = scrapy.Field()
    comment_author = scrapy.Field()
    comment_timestamp = scrapy.Field()
    comment_appreciation = scrapy.Field()
