#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def breakingRecords(scores):
    mx=scores[0]
    mn=scores[0]
    mxcount = 0
    mncount = 0
    for i in scores:
        print(i,"i")
        if (i>mx):
            mxcount+=1
            print(mxcount)
            mx=i
        if (i<mn):
            mncount+=1
            print(mncount,"mncount")
            mn=i
        else:
            continue
    return(mxcount,mncount)

