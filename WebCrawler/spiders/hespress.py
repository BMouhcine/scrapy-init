# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http.response.html import HtmlResponse
from WebCrawler.items import HesArticle, HesComment
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
        categories = response.xpath(xp.HES_NAV_XPATH).extract()[1:-5]
        navigation = []
        numpages = 11
        for numpage in range(1, numpages):
            for cat in categories:
                cat = cat.replace('.' + str(1) + '.html', '.' +str(numpage)+ '.html')
                navigation.append(cat)
        return (Request(self.start_urls[0] + nav, callback=self.parse_articles, headers=response.headers) for nav in navigation)
        #return (Request(self.start_urls[0] + url, callback=self.parse_articles, headers=response.headers) for url in response.xpath(xp.HES_NAV_XPATH).extract()[1:-5])


    def parse_articles(self, response):
        for article_section in response.xpath(xp.HES_ARTICLES_SECTIONS_XPATH):
            title = article_section.xpath('text()').extract_first()
            href = article_section.xpath('@href').extract_first()
            href_splitted = article_section.xpath('@href').extract_first().split('/')[1:]
            category = href_splitted[0]

            article_id = int(''.join([char for char in href_splitted[1] if char.isdigit()]))
            article = HesArticle()
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
        article_link = response.request.url

        article = HesArticle()
        article['article_id'] = article_id
        article['author'] = author
        article['category'] = category
        article['number_of_comments'] = int(number_of_comments[1: -1])
        article['timestamp'] = timestamp
        article['title'] = title
        article['article_link'] = article_link
        comments_set = self.parse_comments(response, article_id)
        article['comments'] = comments_set

        yield article




    def parse_comments(self, response, article_id):
        comments_set = []

        for comment_section in response.xpath(xp.HES_COMMENT_SECTION):
            comment = HesComment()
            #comment_section = comment_section.xpath(xp.HES_COMMENT_BODY)
            comment_number_buffer = comment_section.xpath('.//a/@name').extract_first()
            comment_number = int(''.join([char for char in comment_number_buffer if char.isdigit()]))

            comment_author = comment_section.xpath('.//div[@class="comment_header"]/strong/text()').extract_first()
            if(comment_author is None):
                comment_author = comment_section.xpath('.//div[@class="comment_header"]/text()').extract_first()
                comment_author = comment_author[comment_author.find('-')+1:]
            comment_timestamp = comment_section.xpath('.//div[@class="comment_header"]/span/text()').extract_first()
            comment_content = comment_section.xpath('.//div[@class="comment_text"]/text()').extract_first()
            comment_appreciation = comment_section.xpath('.//div[@class="comment_actions"]/div[@class="result"]/text()').extract_first()


            comment['article_id'] = article_id
            comment['comment_number'] = comment_number
            comment['comment_content'] = comment_content
            comment['comment_author'] = comment_author
            comment['comment_timestamp'] = comment_timestamp
            comment['comment_appreciation'] = comment_appreciation

            comments_set.append(comment)
        return comments_set
