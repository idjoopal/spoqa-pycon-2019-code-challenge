#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import math
import random


# In[2]:


data = pd.read_csv('./dataset.csv', header=None)
data2 = pd.read_csv('./dataset2.csv', header=None)


# In[3]:


flatrows,flatrows2 = [],[]
for y, col in data.iterrows():
    for x, row in col.iteritems():
        # if isinstance(row, float)
        if math.isnan(data[x][y])==0:
            if 1<x<61 and 1<y<19:
                flatrows.append((x, -y, random.randint(1,64)*data[x][y]))
            else:
                flatrows.append((x, -y, data[x][y]))

for y, col in data2.iterrows():
    for x, row in col.iteritems():
        # if isinstance(row, float)
        if math.isnan(data[x][y])==0:
            if 1<x<63 and 1<y<19:
                pass
                #flatrows.append((x, -y, random.randint(1,64)*data[x][y]))
            else:
                flatrows2.append((x, -y, x))
        else:
            flatrows2.append((x, -y, x))


# In[4]:


pdData = pd.DataFrame(flatrows, columns=('x', 'y', 'value'))
pdData2 = pd.DataFrame(flatrows2, columns=('x', 'y', 'value'))


# In[5]:


fig = plt.figure(figsize=(16, 12))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.scatter(pdData.x,pdData.y, c=pdData.value, s=100, marker='s')
ax2.scatter(pdData2.x,pdData2.y, c=pdData2.value, s=100, marker='s')

