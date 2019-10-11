#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def kaprekarNumbers(p, q):
    count = 0
    for i in range(p,q+1):
        sqr = i*i
        d = len(str(i))
        s = str(sqr)
        l = len(str(sqr))
        if(d == 1 and len(s)<=2):
            if(len(s)== 1):
                if(i==1):
                    print(1,end=" ")
                    continue
                continue
            else:
                
                ans = int(s[0]) + int(s[1])
                if(ans == i):
                    print(i,end=" ")
                    count+=1
        else:
            #print('i = ',i)
            #print('sqr = ',s,' ',sqr, ' ',l,' ',d)
            #print
            i1 = s[l-d:l]
            #print('i1 = ',i1)
            i2 = s[:l-d]
            #print('i2 = ',i2)
            i1 = int(i1)
            i2 = int(i2)
            if(i1+i2 == i):
                print(i,end=" ")
                count+=1
    if(count == 0):
        print('INVALID RANGE')

            
            
        


            
            
p = int(input())
q = int(input())
kaprekarNumbers(p, q)

