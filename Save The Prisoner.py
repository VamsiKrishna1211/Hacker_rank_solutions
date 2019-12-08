#!/usr/bin/env python
# coding: utf-8

# In[15]:


def saveThePrisoner(n,m,s):
    n_clone=n
    m_clone=m
    div = m_clone/n_clone
    div = int(div)
    if (m_clone>n_clone):
        n_clone=m_clone-(n_clone*((div)))
        if (s+n_clone-1>n):
            return s+n_clone-1-n
            
            
            #return (s+n_clone-1)
        else:
            
            return s+n_clone-1
    
    elif(m_clone==n_clone):
        return n_clone
    else:
        if (s+m<=n):
            return m+s-1
        else:
            return s+m-n-1
        
    
        


if __name__=="__main__":

    no_itr=int(input())
    for i in range(no_itr):
        prisoners,sweets,start_chair=map(int, input().rstrip().split())
        warning_chair= saveThePrisoner(prisoners,sweets,start_chair)
        print(warning_chair)


# In[ ]:




