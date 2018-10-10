# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:25:03 2018

@author: RBPandya
"""

import numpy as np

N=np.zeros(10000)
for i in range(0,len(N)-1):
    "Generating 100 random numbers between 0 and 1"
    samp=np.random.random_sample((100,1))
    for j in range(0,98):
        if(samp[j]>samp[j+1]):
            N[i]=j+2
            break
        else:
            N[i]=1
            continue
print(N)
print(np.mean(N))