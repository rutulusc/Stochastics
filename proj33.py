# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:41:51 2018

@author: RBPandya
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


u=np.zeros(5000)
v=np.zeros(5000)
for j in range(0,5000):
    r=np.random.random_sample((50,1))
    for i in range(1,49):
        if(r[i]>r[0]):
            u[j]=i
            for k in range(2,49):
                if(r[k]>r[i]):
                      v[j]=k-i
                      break
            break
x2=np.mean(u)
x3=np.mean(v)
f1=plt.figure()
plt.hist(u)
plt.xlabel('X2')
plt.ylabel('Frequency')

f2=plt.figure()
plt.hist(v)
plt.xlabel('X3')
plt.ylabel('Frequency')

f3=plt.figure()
sns.distplot(u)
plt.xlabel('X2')
plt.ylabel('Prabability')

f4=plt.figure()
sns.distplot(u)
plt.xlabel('X3')
plt.ylabel('Prabability')



