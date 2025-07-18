#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x=[1,2,3,4,5,6,7,]
y=[50,51,52,48,47,49,46]


# In[4]:


plt.plot(x,y)   #cizgi grafiği


# In[5]:


plt.plot(x,y, 'g+')  # g renk değiştirir, + kesim noktalarına işaret tanımlar.


# In[9]:


plt.plot(x,y, 'g--')           #kesikli çizgi, yeşil.


# In[10]:


plt.plot(x,y, 'g+--')          


# In[11]:


plt.plot(x,y, 'g+-.')           


# In[15]:


plt.plot(x,y, '*--r')           #r= red, kırmızı renge çevirir yani burada sıra önemli değildir.


# In[16]:


plt.plot(x,y, 'rD')           #red, DİMOND


# In[20]:


plt.plot(x,y, color='red', marker='D', linestyle='')          


# In[21]:


plt.plot(x,y, color='red', marker='D', linestyle='--')          


# In[24]:


plt.plot(x,y, color='#008840', marker='D', linestyle='')        # hegza desimal yeşil renk = #008840  


# In[34]:


plt.plot(x,y, color='red', marker='+', linestyle='', markersize=21)    #işaretleyici elmasların büyüklüğünü ayarlayan komut.


# In[41]:


plt.plot(x,y, color='red',alpha=0.3)          #alpha, şeffaflaştırır.


# In[46]:


plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='green',linewidth=4, linestyle='dotted')


# In[ ]:




