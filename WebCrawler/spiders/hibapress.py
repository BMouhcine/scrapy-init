# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import WebCrawler.xpath_cfg as xp
from WebCrawler.items import HibArticle, HibComment
import json

class HibapressSpider(scrapy.Spider):
    name = 'hibapress'
    allowed_domains = ['hibapress.com']
    start_urls = ['http://hibapress.com/', 'http://ar.hibapress.com/']
    articles = []
    idx_nav_dict = {'3': 'سياسة', '19': 'حوادث', '8': 'فن', '24': 'مهجر', '22': 'رياضة', '10': 'بلا حدود', '2': 'مجتمع', '20': 'إقتصاد', '9': 'آراء', '99': 'متفرقات', '6': 'شؤون دينية', '11': 'فيديوهات'}
    def parse(self, response):
        nav_list = []
        for nav_element in response.xpath(xp.HIB_NAV_XPATH):
            for numpage in range(1, 3):
                nav_list.append(nav_element.xpath('@href').extract_first() + '/page/' + str(numpage))
        return (Request(nav, callback=self.parse_articles, headers=response.headers) for nav in nav_list)


    def parse_articles(self, response):

        category = self.get_category(response.request.url)
        for article_section in response.xpath(xp.HIB_ARTICLES_SECTIONS_XPATH):
            title = article_section.xpath("text()").extract_first()
            article_href = article_section.xpath("@href").extract_first()
            article_id = int(''.join([i for i in article_href if i.isdigit()]))

            article = HibArticle()
            article['category'] = category
            article['article_id'] = article_id
            self.articles.append(article)


        return (Request(self.start_urls[1] + 'details-' + str(art['article_id']) + '.html', callback=self.parse_single_article, headers=response.headers, meta=dict(cat=art['category'], article_id=art['article_id'])) for art in self.articles)

    def parse_single_article(self, response):
        category = response.meta['cat']
        article_id = response.meta['article_id']
        title = response.xpath(xp.HIB_SINGLE_ARTICLE_TITLE_XPATH).extract_first()

        if(category in [self.idx_nav_dict['99'], self.idx_nav_dict['11']]):
            author = ""
        else:
            #author = response.xpath(xp.HIB_AUTHOR_XPATH).extract_first()
            prefix = xp.HIB_AUTHOR_XPATH_PREFIX
            for suffix in xp.HIB_AUTHOR_XPATHS_SUFFIX_LIST:
                author_xpath_exp = prefix + suffix
                author = response.xpath(author_xpath_exp)
                if len(author)>0:
                    author = author.extract_first()
                    break
        date = response.xpath(xp.HIB_TIMESTAMP_XPATH).extract_first()
        number_of_comments = response.xpath(xp.HIB_NUMBER_OF_COMMENTS_XPATH).extract_first()

        json_data = response.xpath(xp.HIB_WRITER_XPATH).extract_first()
        json_data = json.loads(json_data)
        writer = json_data['@graph'][-1]['name']
        article_link = response.request.url


        article = HibArticle()
        article['article_id'] = article_id
        article['author'] = author
        article['category'] = category
        article['number_of_comments'] = number_of_comments
        article['timestamp'] = date
        article['title'] = title
        article['writer'] = writer
        article['article_link'] = article_link
        comments_set = self.parse_comments(response, article_id)

        article['comments'] = comments_set



        yield article



    def parse_comments(self, response, article_id):
        comments_set = []
        for comment_section in response.xpath(xp.HIB_COMMENTS_SECTIONS_XPATH):
            comment = HibComment()
            comment_number_buffer = comment_section.xpath(xp.HIB_COMMENT_NUMBER_XPATH).extract_first()
            comment_number = int(''.join([char for char in comment_number_buffer if char.isdigit()]))

            comment_author = comment_section.xpath(xp.HIB_COMMENT_AUTHOR).extract_first()

            comment_timestamp = comment_section.xpath(xp.HIB_COMMENT_DATE).extract_first()
            comment_content = comment_section.xpath(xp.HIB_COMMENT_CONTENT).extract_first()
            comment_appreciation = comment_section.xpath('.//div[@class="comment_actions"]/div[@class="result"]/text()').extract_first()


            comment['article_id'] = article_id
            comment['comment_number'] = comment_number
            comment['comment_content'] = comment_content
            comment['comment_author'] = comment_author
            comment['comment_timestamp'] = comment_timestamp
            #comment['comment_appreciation'] = comment_appreciation

            comments_set.append(comment)
        return comments_set


    def get_category(self, url):
        start_index = url.find('-') + 1
        end_index = url.find('.html')
        idx = url[start_index:end_index]
        return self.idx_nav_dict[idx]
