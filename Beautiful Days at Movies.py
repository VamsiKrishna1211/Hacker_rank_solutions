#!/usr/bin/env python
# coding: utf-8

# In[27]:


def numberReverse(num):
    num=str(num)
    rev=''
    for i in range(len(num)-1,-1,-1):
        rev=rev+num[i]
    print(num,rev)
    return int(rev)

def beautifulDays(start, end, check):
    beautiful_days_count=0
    for i in range(start, end+1):
        if(abs((i-numberReverse(i))%check)==0):
            beautiful_days_count+=1
        else:
            continue
    return beautiful_days_count

if __name__=="__main__":
    i,j,k=map(int, input().split())
    result = beautifulDays(i,j,k)
    print(result)


# In[21]:


k=int('02')


# In[22]:


k


# In[ ]:




