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

HIB_AUTHOR_XPATH = '//div[@class="entry-content entry clearfix"]/p/span/text()' ## TO EXTRACT ARTICLE AUTHOR SECTION.

HIB_TIMESTAMP_XPATH = '//span[@class="date meta-item fa-before"]/text()' ## TO EXTRACT ARTICLE TIME STORY SECTION.

HIB_NUMBER_OF_COMMENTS_XPATH = '//span[@class="meta-comment meta-item fa-before"]/text()'

HIB_COMMENTS_SECTIONS_XPATH = '//ol[@class="comment-list"]/li' ## TO EXTRACT COMMENTS SECTIONS.

HIB_COMMENT_NUMBER_XPATH = './/@id' ## TO EXTRACT COMMENT NUMBER.

HIB_COMMENT_AUTHOR = './/article/footer/div/b[@class="fn"]/text()' ## TO EXTRACT COMMENT AUTHOR.

HIB_COMMENT_CONTENT = './/article/div[@class="comment-content"]/p/text()' ## TO EXTRACT COMMENT CONTENT.

HIB_COMMENT_DATE = './/article/footer/div[@class="comment-metadata"]/a/time/@datetime' ## TO EXTRACT COMMENT DATE.
