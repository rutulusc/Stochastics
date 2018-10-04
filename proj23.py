# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:23:24 2018

@author: RBPandya
"""
import numpy as np
import scipy.integrate as integrate
from scipy import pi

"Generating 800 random numbers between 0 and 1"
y=np.random.random_sample((800,1))

"Iterative additions"
x=0
for i in range(1,800):
    x=x+(np.sin(pi*y[i])/y[i])
i1=x/800

"Verfiying result of integral"
i2= integrate.quad(lambda y: (np.sin(pi*y))/y, 0, 1)[0]
i3=integrate.quad(lambda x: (np.sin(x))/x, 0, pi)[0]