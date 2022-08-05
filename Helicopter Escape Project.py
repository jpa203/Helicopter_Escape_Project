#!/usr/bin/env python
# coding: utf-8

# In[1]:


from helper import *


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# In[3]:


index = 0 
for row in data:
    data[index] = row[:-1]
    index += 1 


# In[4]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date
print (data[:4])


# In[5]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]
years = []
for y in range(min_year, max_year+1):
    years.append(y)
attempts_per_year =[]
for y in years:
    attempts_per_year.append([y,0])
print(attempts_per_year)


# In[6]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1 
print(attempts_per_year)


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[8]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




