# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:07:16 2017

@author: vinoth.balu
"""

# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


from math import sqrt

#returns distance based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
    #Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if(item in prefs[person2]):
            si[item]=1
    
    if(len(si)==0):return 0;
    
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))

#Returns the pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
    #Get the mutually rated items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    #Number of similar elements
    n = len(si)
    
    #if there are no common items, return 0
    if n == 0: return 0
    
    #Add the ratings of p1,p2 prefrences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    
    #sum up the squares
    sum1sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2sq = sum([pow(prefs[p2][it],2) for it in si])
    
    #sum of the products
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    #Calculate Pearson Score
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den == 0: return 0
    
    r = num/den
    return r
    
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other), other )
                        for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

#reload(recommendations)
print("***********","Euclidean Distance","***********")
for key in critics:
    if key != 'Lisa Rose':
        print("Lisa Rose - ",key," : ",sim_distance(critics,key,'Lisa Rose'))
print("***********","Pearson Correlation Covariance","***********")
for key in critics:
    if key != 'Lisa Rose':
        print("Lisa Rose - ",key," : ",sim_pearson(critics,key,'Lisa Rose'))
print("***********","Top Matches","***********")
print(topMatches(critics,'Toby',n=3))
print("***********","Top Matches","***********")
print(topMatches(critics,'Toby',n=3,similarity=sim_distance))