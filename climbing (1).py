#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    li=[]
    lis=[0 for i in range(len(scores))]
    lis[0]=1
    
    for i in range(1,len(scores)):
        #print(i)
        if scores[i]<scores[i-1]:
            lis[i]=lis[i-1]+1
        else:
            lis[i]=lis[i-1]
    #print(lis)
    num=len(scores)-1
    for i in range(len(alice)):
        lis.append(lis[len(lis)-1]+1)
        scores.append(alice[i])
        
        for k in range(num,-1,-1):
            if scores[len(scores)-1]>=scores[k]:
                lis[len(lis)-1]=lis[k]
            else:
                break;
        num=k+1
        li.append(lis[len(lis)-1])
        scores.pop(len(scores)-1)
        lis.pop(len(lis)-1)
        
    return li
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
