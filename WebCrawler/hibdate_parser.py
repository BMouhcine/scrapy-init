#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import datetime


# In[50]:


hib_articles_df = pd.read_csv("output/hib_articles.csv")
hib_comments_df = pd.read_csv("output/hib_comments.csv")


# In[51]:


hib_articles_timestamp = hib_articles_df['timestamp']
hib_comments_timestamp = hib_comments_df['comment_timestamp']


# In[52]:


def parse_date(row):
    return datetime.datetime.strptime(row, '%Y-%m-%dT%H:%M:%S%z')


# In[53]:


for i, row in enumerate(hib_articles_timestamp):
    hib_articles_timestamp[i] = str(parse_date(row))


# In[54]:


for i, row in enumerate(hib_comments_timestamp):
    hib_comments_timestamp[i] = str(parse_date(row))


# In[55]:


hib_comments_df.to_csv("output/hib_comments.csv")
hib_articles_df.to_csv("output/hib_articles.csv")


# In[ ]:




