#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


days=[1,2,3,4,5,6,7,]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,38,46,40,42,41]


# In[29]:


plt.plot(days,max_t)
plt.plot(days,min_t)
plt.plot(days,avg_t)


# In[30]:


plt.xlabel("DAYS")
plt.ylabel("TEMPERATURE")
plt.title("WEATHER")

plt.plot(days,max_t)                #x,y label 
plt.plot(days,min_t)
plt.plot(days,avg_t)


# In[32]:


plt.xlabel("DAYS")
plt.ylabel("TEMPERATURE")
plt.title("WEATHER")

plt.plot(days,max_t, label="max")                #atama yapmak için = operatörü mutlaka konulmalıdır.
plt.plot(days,min_t, label="min")                # legend() ile renk isimleri adlandırılır. 
plt.plot(days,avg_t,label="avg")                 # loc konum belirtmek için tanımlanır. loc=best komutunda sistem koyacağı
                                                #lejyonu kendisi seçer
                                           
plt.legend(loc="upper right")


# In[39]:


plt.xlabel("DAYS")
plt.ylabel("TEMPERATURE")
plt.title("WEATHER")

plt.plot(days,max_t, label="max")                
plt.plot(days,min_t, label="min")               
plt.plot(days,avg_t,label="avg")                
                                               
plt.legend(loc="best", shadow="True", fontsize="small")  #göze hoş gelen küçük gölge ayrıntıları ekledim.

plt.grid()         #ızgara eklemek.


# In[ ]:




