#!/usr/bin/env python
# coding: utf-8

# In[18]:


def permutationEquation(p):
    s=sorted(p)
    ret=[]
    for i in s:
        p_in=p.index(i)
        p_out=p.index(p_in+1)
        ret.append(p_out+1)
    return ret
if __name__=="__main__":
    l=int(input())
    p=list(map(int, input().rstrip().split()))
    result=permutationEquation(p)
    print('\n'.join(map(str, result)))


# In[ ]:




