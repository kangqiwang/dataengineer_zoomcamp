#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[10]:


df= pd.read_parquet("yellow_tripdata_2023-01.parquet")


# In[16]:


from sqlalchemy import create_engine
engine= create_engine("postgresql://root:root@localhost:5432/nytaxi")

print(pd.io.sql.get_schema(df,name="yello_taxi_data",con=engine))


# In[19]:


df.head(n=0)
len(df)


# In[21]:


df.to_sql(name="yellow_taxi_data",con=engine,if_exists="append")


# In[22]:


get_ipython().run_line_magic('time', 'df.to_sql(name="yellow_taxi_data",con=engine,if_exists="append")')


# In[ ]:




