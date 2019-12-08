#!/usr/bin/env python
# coding: utf-8

# In[6]:


def maxHeight(h,text):
    th=0
    for i in text:
        if (h[ord(i)-ord('a')]>th):
            th=h[ord(i)-ord('a')]
    return th

def designerPdfViewer(h, word):
    return (h*len(word))


if __name__=="__main__":
    heights=list(map(int,input().rstrip().split()))
    word=input()
    finalHeight=maxHeight(heights,word)
    print(designerPdfViewer(finalHeight,word))
    


# In[ ]:




