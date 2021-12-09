#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
import numpy as np
import pandas as pd

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


# In[4]:


filepath = os.path.join("mars.html")
with open(filepath, encoding='utf-8') as file:
    html = file.read()


# In[5]:


# Parse html / format
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


print(soup.prettify())


# In[7]:


# results list
results = soup.find_all('div', class_='list_text')


# In[8]:


results[1]


# In[9]:


results[0]


# In[11]:


# Loop results - Find titles div/class
for result in results:
    title = result.find('div', class_='content_title').text
    title_text = result.find('div', class_='article_teaser_body').text

    try:
            print(title)
            print(title_text)

    except AttributeError as e:
        print(e)


# In[12]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[13]:


#Set URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[20]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# Set featured image
featured_image = soup.find('img', class_='headerimage fade-in')
featured_image


# In[21]:


#Finding the url for the featured image.
featured_image_url = featured_image['src']
featured_image_url


# In[22]:


#Writing out the full url of the featured image.
url_df = pd.Series([url,featured_image_url])

featured_image_full_url = url_df.str.cat()
featured_image_full_url


# In[32]:


#Reading tables from galaxy facts into pandas
url = 'https://galaxyfacts-mars.com'


# In[33]:


tables = pd.read_html(url)
df = tables[0]
df.head()


# In[34]:


#Set column headers
df.columns = df.iloc[0] 
df.drop(index=df.index[0], 
        axis=0, 
        inplace=True)
df


# In[35]:


df.set_index('Mars - Earth Comparison')


# In[38]:


#Convert html table
html_table = df.to_html()
html_table


# In[39]:


html_table.replace('\n', '')


# In[40]:


df.to_html('table.html')


# In[41]:


print(html_table)


# In[42]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[43]:


# Set URL
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[49]:


#Grab title 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# find results class
results = soup.find_all('div', class_='description')

titles = []
for result in results:
    title = result.find('h3').text
    titles.append(title)
        
#grab first title
first_word = []

for title in titles: 
    titled_word = title.split()[0]
    first_word.append(titled_word)
  
#routes case sensitive
for i in range(len(first_word)):
    first_word[i] = first_word[i].lower()
print(first_word)


# In[51]:


#set empty variable to grab image url
images_url = []

for title in first_titles:
    
    url_df = pd.Series([url,title,'.html'])

    image_url = url_df.str.cat()
    browser.visit(image_url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    full_image_url = soup.find('img', class_ = 'wide-image')['src']
    image_url_df = pd.Series([url,full_image_url])
    final_image_url = image_url_df.str.cat()
    images_url.append(final_image_url)

images_url


# In[52]:


hemisphere_image_urls = []
for x in range(0,4):
    hemisphere_dict = {'title': titles[x], 'img_url': images_url[x]}
    hemisphere_image_urls.append(hemisphere_dict)
    
hemisphere_image_urls


# In[ ]:




