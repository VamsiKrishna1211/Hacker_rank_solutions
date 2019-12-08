#!/usr/bin/env python
# coding: utf-8

# In[10]:


def saveThePrisoner(n,m,s):
    war=s
    for i in range(m):
        war+=1
        if(war>n):
            war=1
    if (war==1):
        return n
    else:
        return war-1


if __name__=="__main__":
    no_itr=int(input())
    for i in range(no_itr):
        prisoners,sweets,start_chair=map(int, input().rstrip().split())
        warning_chair= saveThePrisoner(prisoners,sweets,start_chair)
        print(warning_chair)


# In[ ]:




