#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[6]:


df2 = pd.read_csv('sample_data_1.csv', header = None)
df2.columns = ["id", "state", "Population","murder_rate"]
df2


# In[7]:


df2.head()


# In[8]:


df2.tail()


# In[9]:


df2.describe()


# In[10]:


df2.iloc[5][3]


# In[12]:


df2.iloc[1]['state']


# In[14]:


df2.iloc[1]['Population']


# In[17]:


df3=df2[['state', 'Population']]
df3


# In[20]:


df4=df2.iloc[1:3]
df4


# In[21]:


df4=df2.loc[1:3]
df4


# In[22]:


df4 = df2.loc[1:2, ['state', "id"]]
df4


# In[ ]:


df5 = df.append()

