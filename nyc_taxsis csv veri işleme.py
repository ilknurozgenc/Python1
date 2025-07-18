#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


taxi=np.genfromtxt('nyc_taxis.csv',delimiter= ',', skip_header=True)


# In[7]:


speed=taxi[:,7]/ (taxi[:,8 ]/3600)


# In[8]:


mean_speed=speed.mean()
print(mean_speed)


# In[10]:


rides_feb=taxi[taxi[:,1]==2,1]
print(rides_feb.shape[0])


# In[11]:


print(taxi[taxi[:,-3]>50, -3].shape[0])


# In[12]:


taxi[taxi[:,6]==2,6].shape[0]

