# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json
from WebCrawler.items import Article, Comment
class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class HesArticlePipeline(object):
    def __init__(self):
        self.csvfile = open('hes_articles.csv', 'w', newline='')
        csv_columns = ['article_id', 'author', 'category', 'number_of_comments', 'timestamp', 'title']
        self.writer = csv.DictWriter(self.csvfile, fieldnames=csv_columns)
        self.writer.writeheader()

        self.csvfile_comments = open('hes_comments.csv', 'w', newline='')
        csv_columns_comments = ['article_id', 'comment_number', 'comment_content', 'comment_author', 'comment_timestamp', 'comment_appreciation']
        self.writer_comments = csv.DictWriter(self.csvfile_comments, fieldnames=csv_columns_comments)
        self.writer_comments.writeheader()



    def process_item(self, item, spider):
        #if(type(item).__name__=='Article'):
        if spider.name == 'hespress':
            if isinstance(item, Article):
                comments_set = item['comments']
                dict_item = dict(item)
                dict_item.pop('comments')
                self.writer.writerow(dict_item)

                for comment in comments_set:
                    self.writer_comments.writerow(dict(comment))
                return item


class HibPipeline(object):
    def __init__(self):

        self.csvfile = open('hib_articles.csv', 'w', newline='')
        csv_columns = ['article_id', 'author', 'category', 'number_of_comments', 'timestamp', 'title']
        self.writer = csv.DictWriter(self.csvfile, fieldnames=csv_columns)
        self.writer.writeheader()

        self.csvfile_comments = open('hib_comments.csv', 'w', newline='')
        csv_columns_comments = ['article_id', 'comment_number', 'comment_content', 'comment_author', 'comment_timestamp', 'comment_appreciation']
        self.writer_comments = csv.DictWriter(self.csvfile_comments, fieldnames=csv_columns_comments)
        self.writer_comments.writeheader()

    def process_item(self, item, spider):
        if spider.name == 'hibapress':
            comments_set = item['comments']
            dict_item = dict(item)
            dict_item.pop('comments')

            a = self.writer.writerow(dict_item)
            for comment in comments_set:
                self.writer_comments.writerow(dict(comment))

            return item
