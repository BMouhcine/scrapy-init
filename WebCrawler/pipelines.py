# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json
class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class JLHesPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

class CsvHesPipeline(object):
    def __init__(self):
        self.csvfile = open('output.csv', 'w', newline='')
        csv_columns = ['article_id', 'author', 'category', 'number_of_comments', 'timestamp', 'title']
        self.writer = csv.DictWriter(self.csvfile, fieldnames=csv_columns)
        self.writer.writeheader()
    def process_item(self, item, spider):
        #item['number_of_comments'] = int(item['number_of_comments'][1:-1])
        self.writer.writerow(dict(item))
        return item
