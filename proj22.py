# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:18:39 2018

@author: RBPandya
"""
import numpy as np

N=[10,52,100,1000,10000]
r=np.zeros(5)
for j in range(0,5):
    cards=np.arange(0,N[j]+1)
    a=np.random.random_integers(1,N[j],size=N[j])
    counts, edges = np.histogram(a, bins=cards)
    num=0
    for i in range(0,N[j]-1):
        if(counts[i]==0):
            num+=1
    r[j]=num/N[j]


