#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


obj = pd.Series([4,10,-5,15])
obj


# In[4]:


type(obj)


# In[5]:


obj + 5


# In[6]:


obj + 2


# In[7]:


obj % 2


# In[8]:


obj[obj%2==0]


# In[13]:


data = {"EWU":1212, "DU" : 1211, "KUET" : 7455, "KU": 7456, "KUET": 7454}
obj1 = pd.Series(data)
obj1


# In[17]:


list1 = [['Sujon', 12, 3.5, 10],['Mehedi', 20,15,13.5],['Kashem', 11, 13, 7.6887]]
df = pd.DataFrame(list1)
df.columns = ['name', 'Age', 'Street', 'Math']
df


# In[18]:


dict1 = {'id':[1,2,3], 'name': ['alice', 'bob', 'charlie'], 'age': [20,25,30]}
df1 = pd.DataFrame(dict1)
df1


# In[ ]:




