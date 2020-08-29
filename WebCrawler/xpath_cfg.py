HES_NAV_XPATH = "//div[@id='mainNav']//li/a/@href"

HES_ARTICLES_SECTIONS_XPATH = '//h2[@class="section_title"]/a' ## PARSE HES ARTICLES FOR EACH PAGE OF THE CATEGORIES CHOSEN FROM THE NAVBAR.

HES_SINGLE_ARTICLE_XPATH = '//h1[@class="page_title"]/text()' ## PARSE HES SINGLE ARTICLE.

HES_AUTHOR_XPATH = '//div[@id="article_body"]//span[@class="story_author"]/text()' ## TO EXTRACT ARTICLE AUTHOR SECTION.

HES_TIMESTAMP_XPATH = '//div[@id="article_body"]//span[@class="story_date"]/text()' ## TO EXTRACT ARTICLE TIME STORY SECTION.

HES_NUMBER_OF_COMMENTS_XPATH = '//h4[@class="title_comments"]/span/text()' ## TO EXTRACT NUMBER OF COMMENTS SECTION.

#HES_COMMENT_SECTION = '//div[@class="comment_list"]' ## TO EXTRACT TO COMMENTS LIST SECTION..

HES_COMMENT_SECTION = '//div[@class="comment_body_in"]' ## TO EXTRACT COMMENT BODY.
