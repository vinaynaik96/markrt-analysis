#!/usr/bin/env python
# coding: utf-8

# # Problem 1

# question :
# Based on your understanding of the data, what kind of business is this company in?

# In[11]:


import pandas as pd
df = pd.read_csv('OnlineRetail.csv',header=0,encoding = 'unicode_escape')


# In[12]:


df.head()


# In[16]:


df.shape


# In[17]:


df.columns


# In[18]:


df.info()


# In[19]:


df['InvoiceDate'].value_counts()


# # Answers

# The dataset we are using comes from OnlineRetail.csv.It contains all the transactions occurring between 2010 and 2011 for a UK-based and registered online retail.It's a large retailers which stores the data of 'InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate','UnitPrice', 'CustomerID', 'Country'.
#     
#  company is in online retail business

# In[ ]:




