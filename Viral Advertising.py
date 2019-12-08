#!/usr/bin/env python
# coding: utf-8

# In[10]:


from math import floor

def viralAdvertising(days):
    recipients=5
    total_likes=0
    for i in range(days):
        if (i==0):
            liked=2
            total_likes+=liked
            recipients=floor(recipients/2)*3
            continue
        liked=liked+floor(recipients/2)
        recipients=floor(recipients/2)*3
    return liked
        
        

if __name__=="__main__":
    days=int(input())
    result = viralAdvertising(days)
    print(result)


# In[7]:


2/2


# In[ ]:




