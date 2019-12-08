#!/usr/bin/env python
# coding: utf-8

# In[95]:


import math as m

def unique(socks_pile):
    unique_pile=[]
    for i in socks_pile:
        if i not in unique_pile:
            unique_pile.append(i)
        else:
            continue
    return unique_pile

def sockCount(unique_pile, ar):
    pair_count=[]
    for i in range(len(unique_pile)):
        pair_count.append(0)
        
    for i in ar:
        index=unique_pile.index(i)
        pair_count[index]+=1
        
    return pair_count

def organized(pairs_unorganized):
    ans=0
    for i in pairs_unorganized:
        ans+=m.floor(i/2)
    return ans

if __name__=='__main__':
    n=int(input())
    ar=list(map(int, input().rstrip().split()))
    unique_pile=unique(ar)
    pairs_unorganized=sockCount(unique_pile,ar)
    print(organized(pairs_unorganized))
    
    
    

