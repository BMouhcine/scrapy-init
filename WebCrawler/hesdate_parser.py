#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
import datetime


# In[161]:


days_list = ["الخميس", "الجمعة", "الاثنين", "الأربعاء","السبت", "الأحد", "الثلاثاء"]

months_dict = {"يناير":"01",
              "فبراير":"02",
              "مارس":"03",
              "أبريل":"04",
              "ماي":"05",
              "يونيو":"06",
              "يوليوز":"07",
              "غشت":"08",
              "شتنبر":"09",
              "أكتوبر":"10",
              "نونبر":"11",
              "دجنبر":"12",}


# In[162]:


hes_articles_df = pd.read_csv("output/hes_articles.csv")
hes_comments_df = pd.read_csv("output/hes_comments.csv")


# In[163]:


def parse_date(row, days_list=days_list, months_dict=months_dict):

    for k in days_list:
        if k in row:
            row = row.replace(k, '')

    for k, v in months_dict.items():
        if k in row:
            row = row.replace(k ,v)
    return datetime.datetime.strptime(row, ' %d %m %Y - %H:%M')



# In[164]:


hes_articles_timestamp = hes_articles_df['timestamp']


# In[165]:


for i, row in enumerate(hes_articles_timestamp):
    hes_articles_timestamp[i] = str(parse_date(row))


# In[166]:


hes_comments_timestamp = hes_comments_df['comment_timestamp']


# In[167]:


for i, row in enumerate(hes_comments_timestamp):
    hes_comments_timestamp[i] = str(parse_date(row))


# In[168]:


hes_articles_df.to_csv("output/hes_articles.csv")
hes_comments_df.to_csv("output/hes_comments.csv")


# In[ ]:
