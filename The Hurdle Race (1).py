#!/usr/bin/env python
# coding: utf-8

# In[3]:


def hurdleRace(k,h):
    mx=max(h)
    if(mx-k<0):
        return 0
    else:
        return (mx-k)
    
    
if __name__=='__main__':
    n,k=map(int, input().rstrip().split())
    h=list(map(int, input().rstrip().split()))
    print(hurdleRace(k,h))


# In[ ]:




