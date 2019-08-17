#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import math
import random


# In[2]:


data = pd.read_csv('./dataset.csv', header=None)


# In[3]:


flatrows = []
for y, col in data.iterrows():
    for x, row in col.iteritems():
        # if isinstance(row, float)
        if math.isnan(data[x][y])==0:
            if 1<x<61 and 1<y<19:
                flatrows.append((x, -y, random.randint(1,64)*data[x][y]))
            else:
                flatrows.append((x, -y, data[x][y]))


# In[4]:


pdData = pd.DataFrame(flatrows, columns=('x', 'y', 'value'))


# In[5]:


plt.figure(figsize=(16, 6))
plt.scatter(pdData.x,pdData.y, c=pdData.value, s=50, marker='s')

