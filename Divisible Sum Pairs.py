#!/usr/bin/env python
# coding: utf-8

# In[3]:


def divisibleSumPairs(n, k, ar):
    count = 0
    for j in range(n):
        for i in range(j):
            if((ar[j]+ar[i])%k==0 and i<j):
                count+=1
    return(count)


# In[4]:


ar=list(map(int, input().rstrip().split()))
print(divisibleSumPairs(6,3,ar))


# In[ ]:




