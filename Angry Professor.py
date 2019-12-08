#!/usr/bin/env python
# coding: utf-8

# In[9]:


def angryProfessor(k, a):
    threshold=0
    for i in a:
        
        if(i<=0):
            threshold+=1
            if(threshold>=k):
                return "NO"
        if(threshold>=k):
            return "NO"
    return "YES"


if __name__=='__main__':
    num_test_cases=int(input())
    for i in range(num_test_cases):
        n,k=map(int, input().rstrip().split())
        arrival=list(map(int, input().rstrip().split()))
        result=angryProfessor(k, arrival)
        print (result)


# In[ ]:




