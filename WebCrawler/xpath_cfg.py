####################################################################### HESPRESS

HES_NAV_XPATH = "//div[@id='mainNav']//li/a/@href"

HES_ARTICLES_SECTIONS_XPATH = '//h2[@class="section_title"]/a' ## PARSE HES ARTICLES FOR EACH PAGE OF THE CATEGORIES CHOSEN FROM THE NAVBAR.

HES_SINGLE_ARTICLE_XPATH = '//h1[@class="page_title"]/text()' ## PARSE HES SINGLE ARTICLE.

HES_AUTHOR_XPATH = '//div[@id="article_body"]//span[@class="story_author"]/text()' ## TO EXTRACT ARTICLE AUTHOR SECTION.

HES_TIMESTAMP_XPATH = '//div[@id="article_body"]//span[@class="story_date"]/text()' ## TO EXTRACT ARTICLE TIME STORY SECTION.

HES_NUMBER_OF_COMMENTS_XPATH = '//h4[@class="title_comments"]/span/text()' ## TO EXTRACT NUMBER OF COMMENTS SECTION.

#HES_COMMENT_SECTION = '//div[@class="comment_list"]' ## TO EXTRACT TO COMMENTS LIST SECTION..

HES_COMMENT_SECTION = '//div[@class="comment_body_in"]' ## TO EXTRACT COMMENT BODY.


###################################################################### HIBAPRESS

HIB_NAV_XPATH = "//div[@id='main-nav-menu']/ul[@class='menu']/li/a"

HIB_ARTICLES_SECTIONS_XPATH = '//ul[@id="posts-container"]/li/div/h2/a' ## PARSE HIB ARTICLES FOR EACH PAGE OF THE CATEGORIES CHOSEN FROM THE NAVBAR.

HIB_SINGLE_ARTICLE_TITLE_XPATH = '//div[@class="entry-header"]/h1/text()' ## HIB SINGLE ARTICLE TITLE.


HIB_AUTHOR_XPATH = '//div[@class="entry-content entry clearfix"]//input[starts-with(@value,"/details-")]/following-sibling::*[1][self::strong or self::b or self::i]//span[@style="color: #ff0000;"]//text()|//span[contains(@style,"color:")]//text()|//span[@style="color: #0000ff;"]//text()|//span[@style="color: #ff0000;" and contains(text(),"بقلم") or (contains(text(), "هبة") and (contains(text(), "-") or contains(text(), "ـ")))]//text()|//p[contains(text(),"هبة")]//text()|//p[string-length(text()) < 150 and string-length(text()) > 1]//text()|//p//span[@style="color: #ff0000;" and contains(text(), "هبة")]//text()|//div[contains(text(), "هبة") and (contains(text(), "-") or contains(text(), "ـ"))]//text()|//p//span[@style="color: #ff0000;"]//text()|//div[@dir="auto"]//span//text()|//div//span[contains(text(), "هبة")]//text()|//div[@dir="auto" and string-length(text())>1]//text()|//p//strong[string-length(text()) < 20]//text()|//p//span//text()|//p[string-length(text()) > 1]//text()'


HIB_AUTHOR_XPATH_PREFIX = '//div[@class="entry-content entry clearfix"]//input[starts-with(@value,"/details-")]/following-sibling::*[1]'
HIB_AUTHOR_XPATH1 = '//span[@style="color: #ff0000;"]//text()'
HIB_AUTHOR_XPATH2 = '//span[contains(@style,"color:")]//text()'
HIB_AUTHOR_XPATH3 = '//span[@style="color: #0000ff;"]//text()'
HIB_AUTHOR_XPATH4 = '//span[@style="color: #ff0000;" and contains(text(),"بقلم") or (contains(text(), "هبة") and (contains(text(), "-") or contains(text(), "ـ")))]//text()'

#HIB_AUTHOR_XPATH5 = '//p[contains(text(),"هبة")]//text()'
#HIB_AUTHOR_XPATH6 = '//p[string-length(text()) < 150 and string-length(text()) > 1]//text()'
#HIB_AUTHOR_XPATH7 = '//p//span[@style="color: #ff0000;" and contains(text(), "هبة")]//text()'

HIB_AUTHOR_XPATH5 = '[contains(text(),"هبة")]//text()'
HIB_AUTHOR_XPATH6 = '[string-length(text()) < 150 and string-length(text()) > 1]//text()'
HIB_AUTHOR_XPATH7 = '//span[@style="color: #ff0000;" and contains(text(), "هبة")]//text()'


HIB_AUTHOR_XPATH8 = '//div[contains(text(), "هبة") and (contains(text(), "-") or contains(text(), "ـ"))]//text()'
#HIB_AUTHOR_XPATH9 = '//p//span[@style="color: #ff0000;"]//text()'
HIB_AUTHOR_XPATH9 = '//span[@style="color: #ff0000;"]//text()'
HIB_AUTHOR_XPATH10 = '//div[@dir="auto"]//span//text()'
HIB_AUTHOR_XPATH11 = '//div//span[contains(text(), "هبة")]//text()'
HIB_AUTHOR_XPATH12 = '//div[@dir="auto" and string-length(text())>1]//text()'

#HIB_AUTHOR_XPATH13 = '//p//strong[string-length(text()) < 20]//text()'
#HIB_AUTHOR_XPATH14 = '//p//span//text()'
#HIB_AUTHOR_XPATH15 = '//p[string-length(text()) > 1]//text()'

HIB_AUTHOR_XPATH13 = '//strong[string-length(text()) < 20]//text()'
HIB_AUTHOR_XPATH14 = '//span//text()'
HIB_AUTHOR_XPATH15 = '[string-length(text()) > 1]//text()'

HIB_AUTHOR_XPATHS_SUFFIX_LIST = [
                            HIB_AUTHOR_XPATH1, HIB_AUTHOR_XPATH2, HIB_AUTHOR_XPATH3, HIB_AUTHOR_XPATH4, HIB_AUTHOR_XPATH5,
                            HIB_AUTHOR_XPATH6, HIB_AUTHOR_XPATH7, HIB_AUTHOR_XPATH8, HIB_AUTHOR_XPATH9, HIB_AUTHOR_XPATH10,
                            HIB_AUTHOR_XPATH11, HIB_AUTHOR_XPATH12, HIB_AUTHOR_XPATH13, HIB_AUTHOR_XPATH14, HIB_AUTHOR_XPATH15
                                ]





HIB_WRITER_XPATH = '//script[@class="yoast-schema-graph"]/text()'

HIB_OG_DESC = '//meta[@property="og:description"]/@content' ## GET THE ARTICLE DESC (HELPS TO FIND THE AUTHOR'S NAME).

HIB_TIMESTAMP_XPATH = '//meta[@property="article:published_time"]/@content' ## TO EXTRACT ARTICLE TIME STORY SECTION.

HIB_NUMBER_OF_COMMENTS_XPATH = '//span[@class="meta-comment meta-item fa-before"]/text()'

HIB_COMMENTS_SECTIONS_XPATH = '//ol[@class="comment-list"]/li' ## TO EXTRACT COMMENTS SECTIONS.

HIB_COMMENT_NUMBER_XPATH = './/@id' ## TO EXTRACT COMMENT NUMBER.

HIB_COMMENT_AUTHOR = './/article/footer/div/b[@class="fn"]/text()' ## TO EXTRACT COMMENT AUTHOR.

HIB_COMMENT_CONTENT = './/article/div[@class="comment-content"]/p/text()' ## TO EXTRACT COMMENT CONTENT.

HIB_COMMENT_DATE = './/article/footer/div[@class="comment-metadata"]/a/time/@datetime' ## TO EXTRACT COMMENT DATE.
