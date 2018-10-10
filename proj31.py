# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:46:32 2018

@author: RBPandya
"""

import numpy as np

N=np.zeros(5000)
for i in range(0,len(N)-1):
    samp=np.random.random_sample((20,1))
    sum=0
    for j in range(0,19):
        sum=sum+samp[j]
        if(sum>1):
            N[i]=j+1;
            break
        else:
            continue
print(N)
print(np.mean(N))