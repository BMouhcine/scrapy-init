# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from WebCrawler.items import Article

class HespressSpider(scrapy.Spider):
    name = 'hespress'
    allowed_domains = ['hespress.com']
    start_urls = ['http://www.hespress.com/']
    #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    articles = []
    def parse(self, response):
        nav_xp = "//div[@id='mainNav']//li/a/@href"
        #res = response.xpath(nav_xp).extract()
        #req = [Request(self.start_urls[0]+url) for url in res[1:-1]]
        return (Request(self.start_urls[0] + url, callback=self.parse_articles, headers=response.headers) for  url in response.xpath(nav_xp).extract()[1:-1])


    def parse_articles(self, response):
        for article_section in response.xpath('//h2[@class="section_title"]/a'):
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
        title = response.xpath('//h1[@class="page_title"]/text()').extract_first()

        author = response.xpath('//div[@id="article_body"]//span[@class="story_author"]/text()').extract_first()
        timestamp = response.xpath('//div[@id="article_body"]//span[@class="story_date"]/text()').extract_first()
        number_of_comments = response.xpath('//h4[@class="title_comments"]/span/text()').extract_first()
        href = response.request.url.split('.com/')[1]
        href = href.split('/')
        category = href[0]
        article_id = int(''.join([char for char in href[1] if char.isdigit()]))
        
        article = Article()
        article['title'] = title
        article['category'] = category
        article['article_id'] = article_id
        article['author'] = author
        article['timestamp'] = timestamp
        article['number_of_comments'] = number_of_comments

        yield article
