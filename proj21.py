# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:44:04 2018

@author: RBPandya
"""
"Monte Carlo method"

import numpy as np
import matplotlib.pyplot as plt
import math as mt

"Randomly picking up points and verfiying if points lie within unit circle or not" 
n=np.arange(1,1001)
pi=np.zeros(1000)
for k in range(0,len(n)-1):
    for j in range(0,k):
        x=np.random.random_sample(n[j])
        y=np.random.random_sample(n[j])
        count=0
        z=np.zeros(len(x))
        for i in range(0,len(x)):
            z[i]=x[i]**2 + y[i]**2
            if(z[i]<1):
                count=count+1
            else:
                count=count         
        pi[k]=(4*count)/(i+1)
        "print(pi[k])"
"Plotting the values of pi"
plt.ylim(2,4)
plt.plot(n,pi)
plt.show()

m=np.mean(pi)
s=np.std(pi)
"Calculating confidence intervals"
ci1=np.zeros(5)
ci2=np.zeros(5)
samp=[46,52,389,594,784]
for z in range(0,5):
    ci1[z]=m-(1.96*s/mt.sqrt(samp[z]))
    ci2[z]=m+(1.96*s/mt.sqrt(samp[z]))
