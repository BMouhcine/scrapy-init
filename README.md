#scrapy-init

# Description

#### This project is made using the framework **Scrapy v1.6.0**  to scrape data from two main websites: *Hespress* & Hibapress.
##### These data relate primarily to existing articles in each of the two websites mentioned.



---




# Purpose of the project:

### The main purpose of this project is to scrape articles existing in theses two websites: *Hespress* & Hibapress.



> The process of scraping is to navigate through all the categories on the navigation bar, then, for each category, scrape the existing articles in each page by navigating through a desired number of pages by indicating it in a parameter named `numpages` existing in sloc: `hespress.py:20` & `hibapress.py:16`.  

> **Items used in the scraping process are:**
*    HesArticle.
*    HesComment.
*    HibArticle.
*    HibComment.  
They are indicated in `items.py`.

> **Pipelines used in the scraping process are:**
*    HesArticlePipeline.
*    HibPipeline.  
They are enabled in the following setting parameter named `ITEM_PIPELINES` existing in sloc: `settings.py:67`.  
The two pipeline classes are written in `pipelines.py`.

> **XPATH expressions are written in a config file: `xpath_cfg.py`**  .


### 1.   The data & metadata of each article to scrape are of the  following types:

*   Article ID.
*   Author.
*   Writer or article creator/publisher. ( For *Hibapress* only )
*   Category.
*   Number of comments.
*   Date.
*   Title.
*   Article link.

### 2.   The data & metadata of each comment in each article to scrape are of the following types:
*   Article ID.
*   Comment number.
*   Comment content.
*   Comment author.
*   Comment date.
*   Comment appreciation. ( for *Hespress* only )

### For each website, there are two types of output csv files:
*   Articles csv file.
*   Comments csv file.  

> The output files are created in a folder named `output`.



---






# Running the script

> This project uses the Scrapy v1.6.0.

In terminal, run this command to run *hibapress* spider:

```
$ scrapy crawl hibapress
```
or this, to run the *hespress* spider:
```
$ scrapy crawl hespress
```

> The integer values assigned to pipeline classes in the sloc `settings.py:67` setting determine the order in which they run: items go through from lower valued to higher valued classes. The pipeline class associated to the spider to be run must have the lowest integer value.  
> In `settings.py:67`
```
67: ITEM_PIPELINES = {
68:    'WebCrawler.pipelines.HesArticlePipeline': 200,
69:   'WebCrawler.pipelines.HibPipeline': 300,
70: }
```

---





# TO-DO list:

### ------ For *Hibapress*:
For *Hibapress*, the most of the author names are scraped correctly. But there's always an issue regarding this type of data: The author's name does not explicitly exist in a classified or identified HTML tag that contains the author's name, nor, can be found in a recognizable/repeated HTML tags pattern.
For the overwhelming majority of the articles, the author's name does exist under two main formats:

### 1.   1st format:

```
<input type="hidden" name="_wp_http_referer" value="/details-XXXXXX.html">
<p> -- The author's name -- </p>
<p> 1st paragraph of the article body </p>
<p> 2nd paragraph of the article body </p>
...
```

### 2.   2nd format:

```
<input type="hidden" name="_wp_http_referer" value="/details-XXXXXX.html">
<span style="color:#000ff"> -- The author's name -- </span>
<p> 1st paragraph of the article body </p>
<p> 2nd paragraph of the article body </p>
...
```

*    There are also plenty of other formats that are combinations of the two formats mentioned. Thoses combinations are processed by multiple conditions in the **XPATH** expressions used.
*    Sometimes the author's name is in multiple nested `div` & `span` tags with different classnames & ids.
*    Also, the author's name may be missing in some articles. In this case, some conditions in the **XPATH** expressions are used to handle this problem, and avoid scraping the ***1st paragraph of the article body***. ( until now, the **XPATH** expressions can only reduce the number of articles body paragraphs being scraped as author's name using string conditions: ***length, contains ...etc.***).


> *The most of articles having this problem are of the category: شؤون دينية which happens that plenty of articles of this category have missing author names.*







Here's some samples that illustrate the author's name problem that causes ambiguity:  

*   https://ar.hibapress.com/details-238237.html
*   https://ar.hibapress.com/details-248606.html
*   https://ar.hibapress.com/details-251662.html
*   https://ar.hibapress.com/details-239701.html
*   https://ar.hibapress.com/details-250679.html





---


# Extras:
There's two additional scripts:


1.   `hesdate_parser.py`.
2.   `hibdate_parser.py`.

- The 1st script parse ***dates*** in ***Hespress*** output csv files and rewrite them in a standard format.
- The 2nd script parse ***dates*** in ***Hibapress*** output csv files and rewrite them in a standard format.



> Theses two following commands can be used to run the scripts separately:


```
$ python hesdate_parser.py
```
and,
```
$ python hibdate_parser.py
```


