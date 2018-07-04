
# coding: utf-8

# In[4]:


import bs4


# In[15]:


from bs4 import BeautifulSoup as soup
import requests


# In[124]:


myUrl = 'https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?ojs=10&key="data+scientist"'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


# In[125]:


page = requests.get(myUrl, timeout=5, headers=headers)


# In[126]:


page_soup = soup(page.text, "html.parser")


# In[45]:


with open("output1.html", "w") as file:
    file.write(page_soup.prettify())


# In[137]:


container = page_soup.findAll("div",{"class":"panel "})


# In[142]:


container = page_soup.findAll("div",{"class":"position-title header-text"})
container[1].a["href"]


# In[139]:


len(container)


# In[134]:


con = container[0].div.findAll("div",{"class":"position-title header-text"})
con[0].a["href"]


# In[144]:


jobLink = []
for con in container:
    
    jobLink.append(con.a["href"])
    
jobLink

