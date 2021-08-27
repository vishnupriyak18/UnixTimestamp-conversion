#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


f1 = pd.read_csv("f (1).csv")
print(f1.shape)
f1.head()


# In[6]:


f3 = pd.read_csv("f (3).csv")
print(f3.shape)
f3.head()


# In[7]:


f2 = pd.read_csv("f (2).csv")
print(f2.shape)
f2.head()


# In[8]:


from datetime import *


#  

#  

# **f1 & f3**

# In[9]:


f1 = f1.dropna(subset=['Temperature'])


# In[10]:


f1 = f1[['Timestamp','Temperature']]


# In[11]:


f1.head()


# In[12]:


f3 = f3.dropna(subset=['Temperature'])
f3 = f3[['Timestamp','Temperature']]
f3.head()


# In[13]:


f1.shape, f3.shape


# In[14]:


final_temp = pd.concat([f1,f3])


# In[17]:


f = final_temp
f.head()


# In[18]:


time_stamp = []
for x in f['Timestamp'].tolist():
    temp  = str(x)[:10] + '.' + str(x)[10:]
    time_stamp.append(float(temp))
    


# In[19]:


f = f.drop(['Timestamp'],axis=1)
f.head()


# In[51]:


f['TimeStamp'] = time_stamp


# In[23]:


f.head()


# In[26]:


import time
new_list = []
for x in time_stamp:
    temp  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x))
    new_list.append(temp)
f['TimeStamp'] = new_list


# In[27]:


f


# In[28]:


f.to_csv("merged_initial.csv")


#  

#  

#  

# **Processing f & f2**

# In[ ]:





# In[60]:


f2


# In[3]:


get_ipython().run_line_magic('matplotlib', 'notebook')

 

import pandas as pd
import seaborn as sns
f.head()


# In[ ]:



