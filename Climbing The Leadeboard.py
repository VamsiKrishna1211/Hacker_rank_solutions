#!/usr/bin/env python
# coding: utf-8

# In[39]:



# Uncoment bwlow for Custom input
# scores_count = int(input())

# scores = list(map(int, input().rstrip().split()))

# alice_count = int(input())

# alice = list(map(int, input().rstrip().split()))

scores_count=6
scores=[100, 90, 90, 80, 75, 60]
alice_count=5
alice=[50, 65, 77, 90, 102]

def arrangeScoresRank(scores):
    rank_arrange=[scores[0]]
    for i in range(1,len(scores)):
        if(scores[i-1]!=scores[i]):
            rank_arrange.append(int(scores[i]))
    return rank_arrange



scores_singles=arrangeScoresRank(scores)


def climbingLeaderboard(scores_singles, alice):
    ranks_of_alice=[]
    for i in alice:
        for j in range(len(scores_singles)):
            if (i>=scores_singles[j]):
                ranks_of_alice.append(int(j+1))
                break
            if(i<scores_singles[len(scores_singles)-1]):
                ranks_of_alice.append(len(scores_singles)+1)
                break
    return ranks_of_alice
#print(climbingLeaderboard(scores_singles,alice))
print('\n'.join(map(str, climbingLeaderboard(scores_singles,alice))))


# In[ ]:




