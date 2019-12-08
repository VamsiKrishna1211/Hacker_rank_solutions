#!/usr/bin/env python
# coding: utf-8

# In[2]:


def utopianTree(cycles):
    h=1
    for cyc_no in range(cycles):
        if (cyc_no%2==0):
            h=h*2
        elif (cyc_no):
            h+=1
    return h
if __name__=='__main__':
    n=int(input())
    for itr in range(n):
        cycles=int(input())
        print(utopianTree(cycles))
        


# In[ ]:




