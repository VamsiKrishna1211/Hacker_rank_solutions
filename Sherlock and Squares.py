#!/usr/bin/env python
# coding: utf-8

# In[14]:


def squares(a,b):
    from math import sqrt, ceil, floor
    lower_limit=ceil(sqrt(a))
    upper_limit=floor(sqrt(b))
    int_count=0
    if (lower_limit==sqrt(a)):
        int_count+=1
    if (upper_limit==sqrt(b)):
        int_count+=1
    int_count=int_count+(upper_limit-lower_limit)
    if (int_count<=0):
        return 0
    else:
        return int_count


if __name__=="__main__":
    q_iter=int(input())
    for i in range(q_iter):
        a,b=map(int, input().strip().split())
        print(squares(a,b))
        


# In[10]:





# In[ ]:




