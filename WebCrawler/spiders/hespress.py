# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from WebCrawler.items import Article
import WebCrawler.xpath_cfg as xp
class HespressSpider(scrapy.Spider):
    name = 'hespress'
    allowed_domains = ['hespress.com']
    start_urls = ['http://www.hespress.com/']
    #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    articles = []
    def parse(self, response):
        #res = response.xpath(nav_xp).extract()
        #req = [Request(self.start_urls[0]+url) for url in res[1:-1]]
        return (Request(self.start_urls[0] + url, callback=self.parse_articles, headers=response.headers) for  url in response.xpath(xp.HES_NAV_XPATH).extract()[1:-1])


    def parse_articles(self, response):
        for article_section in response.xpath(xp.HES_ARTICLES_SECTIONS_XPATH):
            title = article_section.xpath('text()').extract_first()
            href = article_section.xpath('@href').extract_first()
            href_splitted = article_section.xpath('@href').extract_first().split('/')[1:]
            category = href_splitted[0]
            article_id = int(''.join([char for char in href_splitted[1] if char.isdigit()]))
            article = Article()
            article['title'] = title
            article['category'] = category
            article['article_id'] = article_id

            self.articles.append(article)
        return (Request(self.start_urls[0] + art['category'] + '/' + str(art['article_id']) + '.html', callback=self.parse_single_article, headers=response.headers) for art in self.articles)

    def parse_single_article(self, response):
        title = response.xpath(xp.HES_SINGLE_ARTICLE_XPATH).extract_first()

        author = response.xpath(xp.HES_AUTHOR_XPATH).extract_first()
        timestamp = response.xpath(xp.HES_TIMESTAMP_XPATH).extract_first()
        number_of_comments = response.xpath(xp.HES_NUMBER_OF_COMMENTS_XPATH).extract_first()
        href = response.request.url.split('.com/')[1]
        href = href.split('/')
        category = href[0]
        article_id = int(''.join([char for char in href[1] if char.isdigit()]))

        article = Article()
        article['article_id'] = article_id
        article['author'] = author
        article['category'] = category
        article['number_of_comments'] = number_of_comments
        article['timestamp'] = timestamp
        article['title'] = title


        yield article
